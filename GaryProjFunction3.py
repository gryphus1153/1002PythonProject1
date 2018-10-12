"""
ICT1002 2018 Trimester 1 - Python Project Description on Procurement Analyzer
Done by: Gary Koh Zi Wei 1802005

Function 3:
Function 3 (5 Marks):
List down the total amount of procurement for each government sectors
and allow users to order those sectors either by ascending order or descending order.

Reference Link:
1) python functions and class:
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename_axis.html
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_index.html

"""

# === libraries ========================================================================================================
import pandas as pd

# === functions ========================================================================================================
class Gary:
    """This class groups the functions together"""
    def __init__(self, data):
        self.df = pd.DataFrame.from_records(data, columns=['agency'])
        #read agency from the csv file, puts it in a dataframe
    
    
    def sortfunc(self, sorts):
        """This function sorts the dataframe either by ascending or descending and calculate the frequency of total procurement of each government sector."""
        #sorts = raw_input("Please key in asc or desc")
        if sorts.lower() == "asc": #if input is asc print the follow result
            result = self.df['agency'].value_counts().rename_axis('Agency').sort_index(ascending=True)#The resulting object will be in ascending order
            #value_counts collates the frequency of each agency based on total procurement
            #rename_axis alter the name of the index or columns and in this case renames it to Agency
            return result
        elif sorts.lower() == "desc": #if input is asc print the follow result
            result = self.df['agency'].value_counts().rename_axis('Agency').sort_index(ascending=False) #The resulting object will be in descending order

            return result
        else: #else if input is not asc or desc print the following
            return "Please key in a valid input"