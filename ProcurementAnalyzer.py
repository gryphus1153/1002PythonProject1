import os
import sys
import time
import csv
currentFileDir = os.path.dirname(__file__)
import PAClasses

# ------------------------------ Classes ------------------------------#
#class Address: #takes in address information from listing of registered contractors
#    def __init__(self, building_no, street_name, unit_no, building_name, postal_code):
#        self.building_no = building_no
#        self.street_name = street_name
#        self.unit_no = unit_no
#        self.building_name = building_name
#        self.postal_code = postal_code
#    
#    def toAddress(self):
#        output = self.building_no + " " + self.street_name + " " + self.unit_no + " " + self.building_name + " S(" + self.postal_code + ")"
#        print(output.replace(" na", ""))
#        
#    def toCSV(self):
#        output = self.building_no + ", " + self.street_name + ", " + self.unit_no + ", " + self.building_name + ", " + self.postal_code
#        return output
#        
#class Contractor:
#    def __init__(self, companyName, uen_no, workheadGrade, additional_info, expiry_date, address, tel_no):
#        self.companyName = companyName
#        self.uen_no = uen_no
#        self.workheadGrade = workheadGrade
#        self.additional_info = additional_info
#        self.expiry_date = expiry_date
#        self.address = address
#        self.tel_no = tel_no
#        
#    def toCSV(self):
#        output = ""
#        for workhead in self.workheadGrade:
#            output += str(self.companyName + ", " + self.uen_no + ", " + workhead + ", " + self.workheadGrade[workhead] + ", " + self.additional_info + ", " + self.expiry_date + ", " + self.address.toCSV() + ", " + self.tel_no + "\n")
#        return output
#        
#class Tender:
#    def __init__(self, tender_no, agency, tender_description, award_date, tender_detail_status, supplierAwarded):
#        self.tender_no = tender_no
#        self.agency = agency
#        self.tender_description = tender_description
#        self.award_date = award_date
#        self.tender_detail_status = tender_detail_status
#        self.supplierAwarded = supplierAwarded
#
#    def toCSV(self):
#        output = ""
#        for supplier in self.supplierAwarded:
#            output += str(self.tender_no + ", " + self.agency + ", " + self.tender_description + ", " + self.award_date + ", " + self.tender_detail_status + ", " + supplier + ", " + self.supplierAwarded[supplier] + "\n")
#        return output
#        
# ------------------------------ Functions ------------------------------#
def getFilePath(message):
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
                tender = Tender(row["tender_no."], row["agency"], row["tender_description"], row["award_date"], row["tender_detail_status"], supplierAwarded)
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
                
#contractor file info
contractorFileRel = "ProjectDatasets\\listing-of-registered-contractors\\listing-of-registered-contractors.csv"
contractorFilePath = os.path.join(currentFileDir,contractorFileRel)

#tender file info
tenderFileRel = "ProjectDatasets\\government-procurement\\government-procurement-via-gebiz.csv"
tenderFilePath = os.path.join(currentFileDir,tenderFileRel)

# ------------------------------ MAIN ------------------------------#
#contractorFilePath = getFilePath("Enter the path of contractor file: ")
#tenderFilePath = getFilePath("Enter the path of tender file: ")

start = time.time() # Start timer
contractorDict = processContractors(contractorFilePath)
tenderDict = processTenders(tenderFilePath)
end = time.time() #end timer
print("time taken(s):" + str(end-start))

start = time.time()
agencyDict = getAgencyProcurement(tenderDict)
procurementToFile(agencyDict)
end = time.time() #end timer
print("time taken(s):" + str(end-start))

print(tenderDict["AVA000ETT15000007"].toCSV())