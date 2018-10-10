import numpy as np
import pandas as pd
import os

currentFileDir = os.path.dirname(__file__)

govtTenderFile = "ProjectDatasets/government-procurement/government-procurement-via-gebiz.csv"
govtTenderFile = os.path.join(currentFileDir, govtTenderFile)
registeredContractorsFile = "ProjectDatasets\listing-of-registered-contractors\listing-of-registered-contractors.csv"
registeredContractorsFile = os.path.join(currentFileDir, registeredContractorsFile)

govtDataFrame = pd.DataFrame(pd.read_csv(govtTenderFile))
registeredContractorsDataFrame = pd.DataFrame(pd.read_csv(registeredContractorsFile))

subSetColumns = registeredContractorsDataFrame.columns.difference(govtDataFrame.columns)  # compares columns of both csv files and removes duplicates

# Mergers both datasets together using supplier_name and company_name as unique keys into new dataFrame called govtDataFrame3
awardedContractorsDataFrame = govtDataFrame.merge(registeredContractorsDataFrame[subSetColumns], how='inner', left_on='supplier_name', right_on='company_name')

#  replace empty cells with NaN values
awardedContractorsDataFrame['awarded_amt'].replace(['', 0], np.nan, inplace=True)  # replaces empty cells and 0 values in awarded_amt column with NaN value
awardedContractorsDataFrame['company_name'].replace(['', 0], np.nan, inplace=True)  # replaces empty cells and 0 values in company_name column with NaN value

# drop cells with NaN values
awardedContractorsDataFrame.dropna(subset=['awarded_amt', 'company_name'], inplace=True)  # drops cells in awarded_amt & company_name column with NaN value
awardedContractorsDataFrame.drop('company_name', axis=1, inplace=True)  # drops duplicated column after merging csv files.
awardedContractorsDataFrame.drop_duplicates('tender_no.', inplace=True)  # drops duplicated rows after merging csv files.

# creates csv file
awardedContractorsDataFrame.to_csv('ProjectDatasets\\awardedRegisteredContractors.csv', index=False)  # creates the merged csv files without indexes.

# clean up CSV file to display on UI
cleanedUpDataFrame = awardedContractorsDataFrame
cleanedUpDataFrame.drop_duplicates('supplier_name', inplace=True)


