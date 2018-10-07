import pandas as pd


#data = pd.read_csv("government-procurement-via-gebiz.csv", index_col=0) #read the csv

class Gary:
    def __init__(self, data):
        self.df = pd.DataFrame.from_records(data, columns=['agency']) #read agency from the csv file and put it in a dataframe
    
    
    def sortfunc(self, sorts):
        #sorts = raw_input("Please key in asc or desc")
        if sorts.lower() == "asc": #if input is asc print the follow result
            result = self.df['agency'].value_counts().rename_axis('Agency').sort_index(ascending=True)
    
            return result
        elif sorts.lower() == "desc": #if input is asc print the follow result
            result = self.df['agency'].value_counts().rename_axis('Agency').sort_index(ascending=False)
            return result
        else: #else if input is not asc or desc print the following
            return "Please key in a valid input"
    
    #garyfunction3 =  sortfunc(df) #using the function to the data
    #print garyfunction3









