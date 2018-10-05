import csv
import os
import PAClasses
currentFileDir = os.path.dirname(__file__)

def getFilePath(message): #!!!!!!Currently Unused!!!!!#
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
            
def processContractors(contractorFilePath): #Read contractors from file, creates a Contractor object. Returns contractorDict. key = company_name
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
    return contractorDict
    
def processTenders(tenderFilePath): #Read tenders from file, creates a Tender object. Returns tenderDict. key = tender_no
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
    return tenderDict

def getAgencyProcurement(tenderDict): #gets the procurement info of each agency. Returns agencyDict. key = agency name
    agencyDict = {}
    for tenderNo in tenderDict:
        agency = tenderDict[tenderNo].agency
        if agency in agencyDict:
            agencyDict[agency].append(tenderNo)
        else:
            agencyDict[agency] = [tenderNo]
    print("Agencies loaded")
    return agencyDict

def procurementToFile(agencyDict): #Writes each agencies tender info into individual files
    agencyDir = currentFileDir + "\\Agencies"
    
    if not os.path.exists(agencyDir):
        os.makedirs(agencyDir)
        
    for agency in agencyDict:
        agencyFilePath = os.path.join(agencyDir, agency)
        with open(agencyFilePath + ".txt", "w") as agencyFile:
            for item in agencyDict[agency]:
                agencyFile.write(item + "\n")
 