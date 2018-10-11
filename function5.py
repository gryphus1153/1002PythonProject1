<<<<<<< HEAD
<<<<<<< HEAD
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

procurementDataFrame = govtDataFrame.merge(registeredContractorsDataFrame, how='outer', left_on='supplier_name', right_on='company_name')  # mergers both datasets together into new dataFrame called df3
procurementDataFrame.drop(['company_name', 'postal_code'], axis=1, inplace=True)  # drops company name and postal code column after merging csv files.

groupedSupplierDataFrame = procurementDataFrame.groupby('supplier_name')  # group by supplier names
groupedSupplierDataFrame.sum().to_csv('ProjectDatasets\\totalNRCnRC.csv')  # sums up the total awarded amounts by supplier names and creates total
groupedSupplierDataFrame.sum().nlargest(5, 'awarded_amt').to_csv('ProjectDatasets\\top5Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 5 companies..
# groupedSupplierDataFrame.sum().nlargest(10, 'awarded_amt').to_csv('ProjectDatasets\\top10Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 10 companies..
# groupedSupplierDataFrame.sum().nlargest(50, 'awarded_amt').to_csv('ProjectDatasets\\top50Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 50 companies..
# groupedSupplierDataFrame.sum().nlargest(100, 'awarded_amt').to_csv('ProjectDatasets\\top100Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 100 companies..

# print groupedSupplierDataFrame  # <------- test

totalContractorsDataFrame = pd.DataFrame(pd.read_csv(totalContractorsFile))
top5DataFrame = pd.DataFrame(pd.read_csv(top5File))

=======
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

procurementDataFrame = govtDataFrame.merge(registeredContractorsDataFrame, how='outer', left_on='supplier_name', right_on='company_name')  # mergers both datasets together into new dataFrame called df3
procurementDataFrame.drop(['company_name', 'postal_code'], axis=1, inplace=True)  # drops company name and postal code column after merging csv files.

groupedSupplierDataFrame = procurementDataFrame.groupby('supplier_name')  # group by supplier names
groupedSupplierDataFrame.sum().to_csv('ProjectDatasets\\totalNRCnRC.csv')  # sums up the total awarded amounts by supplier names and creates total
groupedSupplierDataFrame.sum().nlargest(5, 'awarded_amt').to_csv('ProjectDatasets\\top5Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 5 companies..
# groupedSupplierDataFrame.sum().nlargest(10, 'awarded_amt').to_csv('ProjectDatasets\\top10Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 10 companies..
# groupedSupplierDataFrame.sum().nlargest(50, 'awarded_amt').to_csv('ProjectDatasets\\top50Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 50 companies..
# groupedSupplierDataFrame.sum().nlargest(100, 'awarded_amt').to_csv('ProjectDatasets\\top100Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 100 companies..

# print groupedSupplierDataFrame  # <------- test

totalContractorsDataFrame = pd.DataFrame(pd.read_csv(totalContractorsFile))
top5DataFrame = pd.DataFrame(pd.read_csv(top5File))

>>>>>>> 6523728b7ac77b5e06c2555cb76eb2e21debb292
=======
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

procurementDataFrame = govtDataFrame.merge(registeredContractorsDataFrame, how='outer', left_on='supplier_name', right_on='company_name')  # mergers both datasets together into new dataFrame called df3
procurementDataFrame.drop(['company_name', 'postal_code'], axis=1, inplace=True)  # drops company name and postal code column after merging csv files.

groupedSupplierDataFrame = procurementDataFrame.groupby('supplier_name')  # group by supplier names
groupedSupplierDataFrame.sum().to_csv('ProjectDatasets\\totalNRCnRC.csv')  # sums up the total awarded amounts by supplier names and creates total
groupedSupplierDataFrame.sum().nlargest(5, 'awarded_amt').to_csv('ProjectDatasets\\top5Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 5 companies..
# groupedSupplierDataFrame.sum().nlargest(10, 'awarded_amt').to_csv('ProjectDatasets\\top10Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 10 companies..
# groupedSupplierDataFrame.sum().nlargest(50, 'awarded_amt').to_csv('ProjectDatasets\\top50Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 50 companies..
# groupedSupplierDataFrame.sum().nlargest(100, 'awarded_amt').to_csv('ProjectDatasets\\top100Awards.csv')  # sums up the awarded amounts by supplier names and sorts out the top 100 companies..

# print groupedSupplierDataFrame  # <------- test

totalContractorsDataFrame = pd.DataFrame(pd.read_csv(totalContractorsFile))
top5DataFrame = pd.DataFrame(pd.read_csv(top5File))

>>>>>>> 6523728b7ac77b5e06c2555cb76eb2e21debb292
