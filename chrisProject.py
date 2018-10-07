"""
ICT1002 2018 Trimester 1 - Python Project Description on Procurement Analyzer
Done by: Lim Chu Han 1600440

Open Functions (45 Marks):
1) Bid grading assignment to contractor.
2) Group contractors by expiry so as to mark out contractors to be axed.

Reference Link:
1) How to open csv file with python:
https://www.youtube.com/watch?v=NUVblHTElTk

2) python functions and class:
https://www.w3schools.com/python/python_functions.asp
https://www.w3schools.com/python/python_classes.asp

3) Contractor Registration System:
https://www.bca.gov.sg/ContractorsRegistry/contractors_tendering_limits.html
"""

# === libraries ========================================================================================================
import os #operating system
import csv #.csv file
import datetime #date and time

# === DEFINE ===========================================================================================================
COMPANY_NAME = 0
WORKHEAD = 2
GRADE = 3
EXPIRY_DATE = 5

# === class ============================================================================================================
class csvClass:
    """This class group all csv related functions together"""

    #def __init__(self, fileName):
    #    self.fileName = fileName

    def get_file_dir(self):  #get user input csv file directory
        """This function get the csv file directory."""
        os.getcwd()  # get current working directory
        filePath = os.path.join(os.getcwd(), self.fileName)  #join path
        return filePath

    def read_csv(self, filePath):  # csv file reader
        """This function import given csv file and store it's data into a list."""
        list = []
        with open(filePath, "rU") as csvfile:  # open filePath and decalre it as csvfile
            reader = csv.reader(csvfile)
            for row in reader:
                list.append(row)
            return list

    def write_csv(self, list, fileName):  # export list to csv
        """This function export given list into a csv file."""
        with open(fileName + ".csv", 'w') as csvFile:  # w to write
            writer = csv.writer(csvFile, lineterminator='\n')  # lineterminator='\n' to remove \n between
            writer.writerow(list)  # writerow = [1, 2, 3] | writerows = [[1,2,3],[a,b,c]]
        csvFile.close()

class sortBy_workheads_grade_expiry:
    """This class group all functions together for team to import it as a module and call its function easily.
    Main functions:
    1) workheads.grade("GRADE") #input string: construction, specialist, A1 to C3, SingleGrade to L1
    2) workheads.expiredCompany() #show expired company to be axed"""

    def __init__(self, list):
        self.list = list
        sortDatabase(list)

    def workheadGrade(self, search):
        """This function search for specific workhead/grade and display the companies details as an output."""
        search = search.lower() #change to lowercase
        c = A1 + A2 + B1 + B2 + C1 + C2 + C3
        s = SingleGrade + L6 + L5 + L4 + L3 + L2 + L1

        if search == "construction":
            return(c)
        elif search == "specialist":
            return(s)

        elif search == "a1":
            return(A1)
        elif search == "a2":
            return(A2)
        elif search == "b1":
            return(B1)
        elif search == "b2":
            return(B2)
        elif search == "c1":
            return(C1)
        elif search == "c2":
            return(C2)
        elif search == "c3":
            return(C3)
        elif search=="singlegrade" or search=="single grade":
            return(SingleGrade)
        elif search == "l6":
            return(L6)
        elif search == "l5":
            return(L5)
        elif search == "l4":
            return(L4)
        elif search == "l3":
            return(L3)
        elif search == "l2":
            return(L2)
        elif search == "l1":
            return(L1)
        else:
            #print "Invalid workhead/grade not found."
            return None

    def expiredCompany(self):
        """This function display list of expired company as an output."""
        return(expiredCompany)

    def nonExpiredCompany(self):
        """This function display list of non-expired company as an output."""
        return(nonExpiredCompany)

    def find(self, name):
        """This function allow user to input a company name and display the company details as an output."""
        found = []
        for row in self.list[1:]: #[1:] to skip column name
            if name == row[COMPANY_NAME]:
                found.append(row)
        if not found:  #no such agency/company name
            print "Agency/Company not found."
        else:
            myPrint(found)

# === functions ========================================================================================================
def myPrint(list):
    """This function print out given list in rows and row number."""
    #line = 1
    for row in list:
        #print "%d) %s" % (line, row)
        #line += 1
        print row

constructionWorkhead, specialistWorkhead = [], [] # workheads category
A1,A2,B1,B2,C1,C2,C3 = [],[],[],[],[],[],[]  #construction grading system
SingleGrade,L6,L5,L4,L3,L2,L1 = [],[],[],[],[],[],[]  #specialist grading system
expiredCompany, nonExpiredCompany = [], []
def sortDatabase(list):
    """This function sort out contractor csv file into WORKHEAD, GRADE and EXPIRY_DATE."""
    now = datetime.datetime.now()  #get today date and time
    day = now.strftime("%d/%m/%Y")  #get today date only
    date, month, year = day.split('/')  #split into today date, month and year
    for row in list[1:]: #[1:] to skip column name

        # === sort by workheads ===
        if "CW" in row[WORKHEAD][:2]: #check first two char in workhead column
            constructionWorkhead.append([row[COMPANY_NAME], row[WORKHEAD], row[GRADE], row[EXPIRY_DATE]])
        else:  # CR, ME, MW, SY
            specialistWorkhead.append([row[COMPANY_NAME], row[WORKHEAD], row[GRADE], row[EXPIRY_DATE]])

        # === sort by grade ===
        if "A1" in row[GRADE]: #check grade column
            A1.append([row[COMPANY_NAME], row[GRADE]]) #store company name that fall under this grade
        elif "A2" in row[GRADE]:
            A2.append([row[COMPANY_NAME], row[GRADE]])
        elif "B1" in row[GRADE]:
            B1.append([row[COMPANY_NAME], row[GRADE]])
        elif "B2" in row[GRADE]:
            B2.append([row[COMPANY_NAME], row[GRADE]])
        elif "C1" in row[GRADE]:
            C1.append([row[COMPANY_NAME], row[GRADE]])
        elif "C2" in row[GRADE]:
            C2.append([row[COMPANY_NAME], row[GRADE]])
        elif "C3" in row[GRADE]:
            C3.append([row[COMPANY_NAME], row[GRADE]])
        elif "Single Grade" in row[GRADE]:
            SingleGrade.append([row[COMPANY_NAME], row[GRADE]])
        elif "L6" in row[GRADE]:
            L6.append([row[COMPANY_NAME], row[GRADE]])
        elif "L5" in row[GRADE]:
            L5.append([row[COMPANY_NAME], row[GRADE]])
        elif "L4" in row[GRADE]:
            L4.append([row[COMPANY_NAME], row[GRADE]])
        elif "L3" in row[GRADE]:
            L3.append([row[COMPANY_NAME], row[GRADE]])
        elif "L2" in row[GRADE]:
            L2.append([row[COMPANY_NAME], row[GRADE]])
        elif "L1" in row[GRADE]:
            L1.append([row[COMPANY_NAME], row[GRADE]])

        # === sort by expiry ===
        listDay = row[EXPIRY_DATE]
        listDate, listMonth, listYear = listDay.split('/')
        if int(listYear) < int(year):
            expiredCompany.append([row[COMPANY_NAME], row[EXPIRY_DATE]])  # store company name that expired
        elif int(listYear) > int(year):  #skip the year that is yet to expire
            nonExpiredCompany.append([row[COMPANY_NAME], row[EXPIRY_DATE]])
            continue
        elif int(listMonth) < int(month):
            expiredCompany.append([row[COMPANY_NAME], row[EXPIRY_DATE]])
        elif int(listMonth) > int(month):
            nonExpiredCompany.append([row[COMPANY_NAME], row[EXPIRY_DATE]])
            continue
        elif int(listDate) <= int(date):  #same date expired
            expiredCompany.append([row[COMPANY_NAME], row[EXPIRY_DATE]])

# === chris's main =====================================================================================================
#myCSV = csvClass("listing-of-registered-contractors.csv") #user input csv file here
#filePath = myCSV.get_file_dir() #get file path
#registerdContractorList = myCSV.read_csv(filePath) #store csv file data into a list
#chrisFn = sortBy_workheads_grade_expiry(registerdContractorList) #sort workheads, grade and expiry

# === chris's open function sort by 1)grade and 2)expiry. Amin please use these ========================================
#chrisFn.workheadGrade("A1") #input string: construction, specialist, A1 to C3, SingleGrade to L1
#chrisFn.expiredCompany() #show expired company to be axed

# === other commands ===================================================================================================

# === expiry commands ===
#chrisFn.expiredCompany() #show expired company to be axed
#chrisFn.nonExpiredCompany() #show non-expired company

# === find command ===
#chrisFn.find("68 SYSTEMS & PROJECT ENGINEERING PTE LTD") #find by company name and output its data

# === export csv command ===
#myCSV.write_csv(expiredCompany, "output") #export list to csv


