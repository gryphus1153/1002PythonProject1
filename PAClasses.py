class Address: #takes in address information from listing of registered contractors
    def __init__(self, building_no, street_name, unit_no, building_name, postal_code):
        self.building_no = building_no
        self.street_name = street_name
        self.unit_no = unit_no
        self.building_name = building_name
        self.postal_code = postal_code
    
    def toAddress(self):
        output = self.building_no + " " + self.street_name + "  " + self.unit_no + " " + self.building_name + " Singapore " + self.postal_code
        out = output.replace(" na", "")
        return out
        
    def toCSV(self):
        output = self.building_no + ", " + self.street_name + ", " + self.unit_no + ", " + self.building_name + ", " + self.postal_code
        return output
        
class Contractor:
    def __init__(self, company_name, uen_no, workheadGrade, additional_info, expiry_date, address, tel_no):
        self.company_name = company_name
        self.uen_no = uen_no
        self.workheadGrade = workheadGrade
        self.additional_info = additional_info
        self.expiry_date = expiry_date
        self.address = address
        self.tel_no = tel_no
        
    def toCSV(self):
        output = ""
        for workhead in self.workheadGrade:
            output += str(self.company_name + ", " + self.uen_no + ", " + workhead + ", " + self.workheadGrade[workhead] + ", " + self.additional_info + ", " + self.expiry_date + ", " + self.address.toCSV() + ", " + self.tel_no + "\n")
        return output
        
class Tender:
    def __init__(self, tender_no, agency, tender_description, award_date, tender_detail_status, supplierAwarded):
        self.tender_no = tender_no
        self.agency = agency
        self.tender_description = tender_description
        self.award_date = award_date
        self.tender_detail_status = tender_detail_status
        self.supplierAwarded = supplierAwarded

    def toCSV(self):
        output = ""
        for supplier in self.supplierAwarded:
            output += str(self.tender_no + ", " + self.agency + ", " + self.tender_description + ", " + self.award_date + ", " + self.tender_detail_status + ", " + supplier + ", " + self.supplierAwarded[supplier] + "\n")
        return output
        