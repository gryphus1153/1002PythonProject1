import csv
import os
import PAClasses
import requests
from bs4 import BeautifulSoup
import PAClasses
import re

currentFileDir = os.path.dirname(__file__)
gradeDict = {"A1":2147483647, "A2":85000000, "B1":40000000, "B2":13000000, "C1":4000000, "C2":1300000, "C3":650000, "Single Grade":2147483647, "L6":2147483647, "L5":13000000, "L4":6500000, "L3":4000000, "L2":1300000, "L1":650000}

def getFilePath(message): #UNUSED
    cDone = True
    #check if files exist
    while(True):
        try:
            fileInput = raw_input(message)
            assert os.path.exists(fileInput), "File not found. Enter a valid file path."
            assert ".csv" in fileInput, "Input a path to a .csv file"
            return fileInput
        except Exception as e:
            print(e)
            
def processContractors(contractorFilePath): 
    """Read contractors from file, creates a Contractor object. Returns contractorDict. key = company_name"""
    with open(contractorFilePath) as contractorFile:
        reader = csv.DictReader(contractorFile,dialect="excel")
        contractorDict = {}
        for row in reader:
            key = row["company_name"]
            
            if key in contractorDict:
                #gets Contractor obj, appends Workhead/Grade
                contractor = contractorDict[key]
                contractor.workheadGrade[row["workhead"]] = row["grade"]
                
            else:
                address = PAClasses.Address(row["building_no"], row["street_name"], row["unit_no"], row["building_name"], row["postal_code"]) #Create Address object
                workheadGrade = {row["workhead"]:row["grade"]} #workhead as key, grade as value
                contractor = PAClasses.Contractor(row["company_name"], row["uen_no"], workheadGrade, row["additional_info"], row["expiry_date"], address, row["tel_no"]) #Create Contractor Object
                contractorDict[key] = contractor
    
    print("Contractor Listing Loaded")
    print (len(contractorDict))
    return contractorDict
    
def processTenders(tenderFilePath): 
    """Read tenders from file, creates a Tender object. Returns tenderDict. key = tender_no"""
    with open(tenderFilePath) as tenderFile:
        tenderDict = {}
        reader = csv.DictReader(tenderFile, dialect = "excel")
        
        for row in reader:
            key = row["tender_no."]
            if key in tenderDict:
                tender = tenderDict[key]
                tender.supplierAwarded[row["supplier_name"]] = row["awarded_amt"]
            else:
                supplierAwarded = {row["supplier_name"]:row["awarded_amt"]}
                tender = PAClasses.Tender(row["tender_no."], row["agency"], row["tender_description"], row["award_date"], row["tender_detail_status"], supplierAwarded)
                tenderDict[key] = tender
    print("Tender Listing Loaded")
    print (len(tenderDict))
    return tenderDict

def getAgencyProcurement(tenderDict): 
    """gets the procurement info of each agency. Returns agencyDict. key = agency name"""
    agencyDict = {}
    for tenderNo in tenderDict:
        agency = tenderDict[tenderNo].agency
        if agency in agencyDict:
            agencyDict[agency].append(tenderNo)
        else:
            agencyDict[agency] = [tenderNo]
    print("Agencies loaded")
    return agencyDict

def procurementToFile(agencyDict): 
    """Writes each agencies tender info into individual files"""
    agencyDir = currentFileDir + "\\Agencies"
    
    if not os.path.exists(agencyDir):
        os.makedirs(agencyDir)
        
    for agency in agencyDict:
        agencyFilePath = os.path.join(agencyDir, agency)
        with open(agencyFilePath + ".txt", "w") as agencyFile:
            for item in agencyDict[agency]:
                agencyFile.write(item + "\n")
                
def overtendered(tenderDict, contractorDict): 
    """Gets the tenders and contractors where the contractors are over their respective tendering limit"""
    overtendered = {}
    for tender in tenderDict:
        suppliers = tenderDict[tender].supplierAwarded
        for supplier in suppliers:
            if supplier in contractorDict:
                contractor = contractorDict[supplier]
                #writer.writerow([tender , tenderDict[tender].tender_description , tenderDict[tender].supplierAwarded[supplier] , contractor.company_name])
                max = 0
                for workhead in contractor.workheadGrade:
                    if gradeDict[contractor.workheadGrade[workhead]] > max:
                        max = gradeDict[contractor.workheadGrade[workhead]]
                        
                if float(tenderDict[tender].supplierAwarded[supplier]) > max:
                    overtendered[tender] = [contractor.company_name, tenderDict[tender].supplierAwarded[supplier], str(max)]
                    
    return overtendered

def total_Proc(agencyDict): #UNUSED
    totalproc = {}
    for agency in agencyDict: #gets the agency
        total = 0
        list = agencyDict[agency] #gets the list of tenders
        for tender in list: #gets the tenderno in list
            SA = tenderDict[tender].supplierAwarded #gets the supplierawarded dict
            for val in SA.values():
                total += float(val)
        totalproc[agency] = str(total)
    return totalproc
     
def getLatest(uen): 
    """Scrapes HTML from BCA to get the latest listing information about a company. if it exists, returns a contractor object"""
    workheadGrade = {}
    url = "https://www.bca.gov.sg/BCADirectory/Company/Details/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = url + uen
    try:
        contents = requests.get(url, headers = headers, timeout = 10)
        print(contents.status_code)
        if contents.status_code == 500: #check if contractor exists
            return "Contractor does not Exist/has closed down" #Contractor may have closed down
        
        #get the contractor information from BCA
        soup = BeautifulSoup(contents.content, "html.parser")
        company_name = soup.find_all("div", class_="body-bluetext bold")[0].string
        uen_no = soup.find_all(string=re.compile("UEN"))[0][10:]
        address = soup.find_all(string=re.compile("Address"))[0][10:]
        tel_no = soup.find_all(string=re.compile("^\d{8}$"))[0]
        
        #get workheads and expiry
        expiry_date= ""
        workheadGrade = {}
        registeredContractors = soup.tbody.get_text()
        workheads = registeredContractors.strip().replace("\n", "|").replace("|||", "^").split("^")
        for workhead in workheads:
            split = workhead.split("|")
            workheadGrade[split[0]] = split[2]
            expiry_date = split[3]
        additional_info = None
            
        contractor = PAClasses.Contractor(company_name, uen_no, workheadGrade, additional_info, expiry_date, address, tel_no)
        return contractor #returns a contractor object
    except Exception as e:
        print(e)
        return "Page could not be reached/connection has timed out"