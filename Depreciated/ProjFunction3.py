import pandas as pd
import os

currentFileDir = os.path.dirname(__file__)

#default contractor file info
contractorFileRel = "ProjectDatasets\\listing-of-registered-contractors\\listing-of-registered-contractors.csv"
contractorFilePath = os.path.join(currentFileDir,contractorFileRel)

#default tender file info
tenderFileRel = "ProjectDatasets\\government-procurement\\government-procurement-via-gebiz.csv"
tenderFilePath = os.path.join(currentFileDir,tenderFileRel)

data = pd.read_csv(tenderFilePath, low_memory=False) #read the csv

df = pd.DataFrame.from_records(data, columns=['agency']) #read agency from the csv file and put it in a dataframe



def sortfunc(x, sorts):
    #sorts = raw_input("Please key in asc or desc")
    if sorts == "asc": #if input is asc print the follow result
        result = df['agency'].value_counts().rename_axis('Agency').reset_index(name='Procurement Counter').sort_values(by = "Agency", ascending=True)
        return result
    elif sorts == "desc": #if input is asc print the follow result
        result = df['agency'].value_counts().rename_axis('Agency').reset_index(name='Procurement Counter').sort_values(by = "Agency", ascending=False)
        return result
    else: #else if input is not asc or desc print the following
        return "Please key in a valid input"

def garyfunction3(sorts): #using the function to the data
    return sortfunc(df,sorts)









