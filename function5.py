import pandas as pd
import os

currentFileDir = os.path.dirname(__file__)

govtTenderFile = "ProjectDatasets/government-procurement/government-procurement-via-gebiz.csv"
govtTenderFile = os.path.join(currentFileDir, govtTenderFile)
registeredContractorsFile = "ProjectDatasets\listing-of-registered-contractors\listing-of-registered-contractors.csv"
registeredContractorsFile = os.path.join(currentFileDir, registeredContractorsFile)
totalContractorsFile = "ProjectDatasets\\totalNRCnRC.csv"
totalContractorsFile = os.path.join(currentFileDir, totalContractorsFile)
top5File = "ProjectDatasets\\top5Awards.csv"
top5File = os.path.join(currentFileDir, top5File)

govtDataFrame = pd.DataFrame(pd.read_csv(govtTenderFile))
registeredContractorsDataFrame = pd.DataFrame(pd.read_csv(registeredContractorsFile))

procurementDataFrame = govtDataFrame.merge(registeredContractorsDataFrame, how='outer', left_on='supplier_name', right_on='company_name')  # mergers both datasets together into new dataFrame
procurementDataFrame.drop(['company_name', 'postal_code'], axis=1, inplace=True)  # drops company name and postal code column after merging csv files.
procurementDataFrame.drop_duplicates('tender_no.', inplace=True)  # drops duplicated rows after merging csv files.
procurementDataFrame['supplier_name'] = procurementDataFrame['supplier_name'].str.lower()  # Converts the supplier_name Column into lower case
groupedSupplierDataFrame = procurementDataFrame.groupby('supplier_name')  # group by supplier names
groupedSupplierDataFrame.sum().to_csv('ProjectDatasets\\totalNRCnRC.csv')  # sums up the total awarded amounts by supplier names and creates total

# print groupedSupplierDataFrame  # <------- test
totalContractorsDataFrame = pd.DataFrame(pd.read_csv(totalContractorsFile))
totalContractorsDataFrame.nlargest(5, 'awarded_amt').to_csv('ProjectDatasets\\top5Awards.csv', index=False)  # sums up the awarded amounts by supplier names and sorts out the top 5 companies..
top5DataFrame = pd.DataFrame(pd.read_csv(top5File))

