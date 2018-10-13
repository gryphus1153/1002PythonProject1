import pandas as pd
import numpy as np
import os

currentFileDir = os.path.dirname(__file__)
tenderFileRel = "ProjectDatasets/government-procurement/government-procurement-via-gebiz.csv"
tenderFile = os.path.join(currentFileDir,tenderFileRel)
categoryFileRel = "ProjectDatasets/MinistryCategories.csv"
categoryFile = os.path.join(currentFileDir,categoryFileRel)
#tenderFile = "/Users/RayquazaOutrage/Documents/SIT/ICT1002/Project/Project1-master/ProjectDatasets/government-procurement/government-procurement-via-gebiz.csv"


# process department & ministry data for spendingByMinistry()
def processForMinistry():
    #categoryFile = "C://Users//Amirulamin//Dropbox//SIT//Year1//Tri1//1002ProgrammingFundamentals//Project1//ProjectDatasets//MinistryCategories.csv"  # file containing category information
    columnsToGet = ['department', 'parentMinistry']  # specific columns to read
    ministryDF = pd.DataFrame(pd.read_csv(categoryFile, usecols=columnsToGet))  # read CSV and store column into DF
    ministryDF['department'] = ministryDF['department'].str.lower()   # all strings in department to lowercase
    ministryDF['department'] = ministryDF['department'].str.rstrip()  # remove trailing spaces

    return ministryDF


# process department & category for spendingByCategory()
def processForCategory():
    #categoryFile = "C://Users//Amirulamin//Dropbox//SIT//Year1//Tri1//1002ProgrammingFundamentals//Project1//ProjectDatasets//MinistryCategories.csv"  # file containing category information
    columnsToGet = ['department', 'category']  # specific columns to read
    categoryDF = pd.DataFrame(pd.read_csv(categoryFile, usecols=columnsToGet))  # use pandas to read CSV containing categories
    categoryDF['department'] = categoryDF['department'].str.lower()  # all strings in department to lowercase

    return categoryDF

# process tenderCSV for agency and awarded_amt
def processTenderSpending(tenderCSV):

    columnsToGet = ['agency', 'awarded_amt']  # specific columns to read
    tenderDF = pd.DataFrame(pd.read_csv(tenderCSV, usecols=columnsToGet))  # read CSV and store selected column into DF
    tenderDF['agency'] = tenderDF['agency'].str.lower()   # all strings in department to lowercase
    tenderDF['agency'] = tenderDF['agency'].str.split('-|, |\(').str[0]   # ignores characters after - and '
    tenderDF['agency'] = tenderDF['agency'].str.replace('[\d]', '')   # removes any digits in string
    tenderDF['agency'] = tenderDF['agency'].str.rstrip()    # remove trailing spaces
    tenderDF = tenderDF.groupby(['agency'], as_index=False).sum()  # adds all awarded_amt from same agency

    return tenderDF


# processes all spending from tenderCSV and categorize by Ministry
def spendingByMinistry(tenderCSV):

    tenderDF = processTenderSpending(tenderCSV)
    ministryDF = processForMinistry()
    tenderDF['ministry'] = ""  # add new column to assign ministry

    # to assign a ministry to each agency
    for index, row in tenderDF.iterrows():
        agency = row['agency']
        matchRow = (ministryDF[ministryDF['department'].str.match(agency)])  # get row with matching agency to dept
        parentMinistry = matchRow.loc[:, 'parentMinistry']  # get data from ParentMinistry column
        parentMinistryValue = parentMinistry.values  # get ParentMinistry value (is currently pandas series type)
        tenderDF.at[index, 'ministry'] = parentMinistryValue  # assign ministry to tender['ministry']

    # formatting and adding items by ministry
    tenderDF['ministry'] = tenderDF['ministry'].astype('str')  # convert from obj to str
    tenderDF['ministry'] = tenderDF['ministry'].str.replace('[^\w\s]', '')  # removes char that are non alphanumeric
    spendingDF = tenderDF.groupby(['ministry'], as_index=False).sum()   # adds all awarded_amt from same ministry
    spendingDF['awarded_amt'] = np.round(spendingDF['awarded_amt'], decimals=2)   # round off amount to 2 dec places

    return spendingDF


# processes all spending from tenderCSV and categorize by Category
def spendingByCategory(tenderCSV):

    tenderDF = processTenderSpending(tenderCSV)
    categoryDF = processForCategory()
    tenderDF['category'] = ""  # add new column to assign category

    # assign category to each agency
    for index, row in tenderDF.iterrows():
        agency = row['agency']
        matchRow = (categoryDF[categoryDF['department'].str.match(agency)])  # get row with matching category to dept
        category = matchRow.loc[:, 'category']  # get data from category column
        categoryValue = category.values  # get Category value
        tenderDF.at[index, 'category'] = categoryValue  # assign category to tenderDF['category']

    # formatting and adding items by category
    tenderDF['category'] = tenderDF['category'].astype('str')  # convert from obj to str
    tenderDF['category'] = tenderDF['category'].str.replace('[^\w\s]', '')  # removes char that are non alphanumeric
    spendingDF = tenderDF.groupby(['category'], as_index=False).sum()   # add all awarded_amt by category
    spendingDF['awarded_amt'] = np.round(spendingDF['awarded_amt'], decimals=2)  # round off to 2 dec places

    return spendingDF

# main method for testing purposes.


#ministrySpending = spendingByMinistry(tenderFile)
#categorySpending = spendingByCategory(tenderFile)

#print(ministrySpending.values.tolist())

