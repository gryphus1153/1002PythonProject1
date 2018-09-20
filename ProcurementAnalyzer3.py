import os
import sys
import time
import csv
currentFileDir = os.path.dirname(__file__)

class Address: #takes in address information from listing of registered contractors and
    def __init__(self, building_no, street_name, unit_no, building_name, postal_code):
        self.building_no = building_no
        self.street_name = street_name
        self.unit_no = unit_no
        self.building_name = building_name
        self.postal_code = postal_code
    
    def toAddress(self):
        output = self.building_no + " " + self.street_name + " " + self.unit_no + " " + self.building_name + " S(" + self.postal_code + ")"
        print(output.replace(" na", ""))
        

class Contractor:
    def __init__(self, companyName, uen_no, workheadGrade, additional_info, expiry_date, address, tel_no):
        self.companyName = companyName
        self.uen_no = uen_no
        self.workheadGrade = workheadGrade
        self.additional_info = additional_info
        self.expiry_date = expiry_date
        self.address = address
        self.tel_no = tel_no
    
    
class Tender:
    def __init__(self, tender_no, agency, tender_description, award_date, tender_detail_status, supplierAwarded):
        self.tender_no = tender_no
        self.agency = agency
        tender_description = tender_description
        self.award_date = award_date
        self.tender_detail_status = tender_detail_status
        self.supplierAwarded = supplierAwarded

#contractor file info
contractorFileRel = "ProjectDatasets\\listing-of-registered-contractors\\listing-of-registered-contractors.csv"
contractorFilePath = os.path.join(currentFileDir,contractorFileRel)
contractorDict = {}

#tender file info
tenderFileRel = "ProjectDatasets\\government-procurement\\government-procurement-via-gebiz.csv"
tenderFilePath = os.path.join(currentFileDir,tenderFileRel)
tenderDict = {}


# ------------------------------- MAIN ------------------------
cDone = True
#check if files exist
while(cDone):
    try:
        contractorInput = raw_input("Enter the path of contractor file: ")
        assert os.path.exists(contractorInput)
        contractorFilePath = contractorInput
        cDone = False
    except Exception as e:
        print("I did not find the file")
        
tDone = True
while(tDone):
    try:
        tenderInput = raw_input("Enter the path of tender file: ")
        assert os.path.exists(tenderInput)
        tenderFilePath = tenderInput
        tDone = False
    except Exception as e:
        print("I did not find the file")

start = time.time() # Start timer

#Process contractors
with open(contractorFilePath) as contractorFile:
    reader = csv.DictReader(contractorFile,dialect="excel")
    
    for row in reader:
        key = row["company_name"]
        
        if key in contractorDict:
            #gets Contractor obj, appendss Workhead/Grade
            contractor = contractorDict[key]
            contractor.workheadGrade[row["workhead"]] = row["grade"]
            
        else:
            address = Address(row["building_no"], row["street_name"], row["unit_no"], row["building_name"], row["postal_code"]) #Create Address object
            workheadGrade = {row["workhead"]:row["grade"]} #workhead as key, grade as value
            contractor = Contractor(row["company_name"], row["uen_no"], workheadGrade, row["additional_info"], row["expiry_date"], address, row["tel_no"]) #Create Contractor Object
            contractorDict[key] = contractor
            
print("Contractor Listing loaded")

#Process tenders
with open(tenderFilePath) as tenderFile:
    reader = csv.DictReader(tenderFile, dialect = "excel")
    
    for row in reader:
        key = row["tender_no."]
        
        if key in tenderDict:
            tenderDict[key].supplierAwarded["supplier_name"] = awarded_amt
            
        else:
            supplierAwarded = {row["supplier_name"]:row["awarded_amt"]}
            tender = Tender(row["tender_no."], row["agency"], row["tender_description"], row["award_date"], row["tender_detail_status"], supplierAwarded)
            
print("Tender Listing Loaded")

end = time.time()  
print(end-start)
