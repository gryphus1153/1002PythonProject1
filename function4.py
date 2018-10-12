import numpy as np
import pandas as pd
import os

currentFileDir = os.path.dirname(__file__)

#govtTenderFile = "ProjectDatasets/government-procurement/government-procurement-via-gebiz.csv"
#govtTenderFile = os.path.join(currentFileDir, govtTenderFile)
#registeredContractorsFile = "ProjectDatasets\listing-of-registered-contractors\listing-of-registered-contractors.csv"
#registeredContractorsFile = os.path.join(currentFileDir, registeredContractorsFile)

awardedContractorsFile = "ProjectDatasets\\awardedRegisteredContractors.csv"
awardedContractorsFile = os.path.join(currentFileDir, awardedContractorsFile)

class CK1:
    def __init__(self, govtTenderFile, registeredContractorsFile):
        self.govtDataFrame = pd.DataFrame(pd.read_csv(govtTenderFile))
        self.registeredContractorsDataFrame = pd.DataFrame(pd.read_csv(registeredContractorsFile))

        self.subSetColumns = self.registeredContractorsDataFrame.columns.difference(self.govtDataFrame.columns)  # compares columns of both csv files and removes duplicates

        # Mergers both datasets together using supplier_name and company_name as unique keys into new dataFrame called govtDataFrame3
        self.awardedContractorsDataFrame = self.govtDataFrame.merge(self.registeredContractorsDataFrame[self.subSetColumns], how='inner', left_on='supplier_name', right_on='company_name')

        #  replace empty cells with NaN values
        self.awardedContractorsDataFrame['awarded_amt'].replace(['', 0], np.nan, inplace=True)  # replaces empty cells and 0 values in awarded_amt column with NaN value
        self.awardedContractorsDataFrame['company_name'].replace(['', 0], np.nan, inplace=True)  # replaces empty cells and 0 values in company_name column with NaN value

        # drop cells with NaN values
        self.awardedContractorsDataFrame.dropna(subset=['awarded_amt', 'company_name'], inplace=True)  # drops cells in awarded_amt & company_name column with NaN value
        self.awardedContractorsDataFrame.drop('company_name', axis=1, inplace=True)  # drops duplicated column after merging csv files.
        self.awardedContractorsDataFrame.drop_duplicates('tender_no.', inplace=True)  # drops duplicated rows after merging csv files.

        # creates csv file
        self.awardedContractorsDataFrame.to_csv(awardedContractorsFile, index=False)  # creates the merged csv files without indexes.

        # clean up CSV file to display on UI
        self.cleanedUpDataFrame = self.awardedContractorsDataFrame
        self.cleanedUpDataFrame.drop_duplicates('supplier_name', inplace=True)