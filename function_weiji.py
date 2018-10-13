import pandas as pd

def bidamount(biddata):  # primary key tender no, amount awarded show range of values for bids # GOT to rewrite this set as list then get min max
    minmaxdict = {}
    for tender in biddata:
        if biddata[tender].tender_detail_status != "Awarded to no Supplier":
            list = biddata[tender].supplierAwarded.values()
        newlist = map(float, list)
        minmaxdict[biddata[tender].tender_no] = [min(newlist), max(newlist)]

    #for key, val in minmaxdict.items():
    #    print key, val
    return minmaxdict
    
def contractorworkhead(contractorfile):
    contractordata = ['company_name', 'workhead']
    contractorcontain = pd.DataFrame(pd.read_csv(contractorfile, usecols=contractordata))
    return contractorcontain.drop_duplicates(subset = "company_name")


def contractordesc(contractorfile):
    contractorcontain = contractorworkhead(contractorfile)    # assigns the variable with a dataframe
    contractorcontain['workhead_description'] = ''  # sets a column named workhead_description to the dataframe variable
    for index, row in contractorcontain.iterrows(): #assigns a description to a workhead
        workhead = row['workhead']

        if workhead != '':
            if 'CR' in workhead:
                workhead_description = "construction related" #assigns a description to a workhead
                combined = workhead + ' ' + workhead_description
                contractorcontain.at[index, 'workhead_description'] = combined

            elif 'CW' in workhead:
                workhead_description = "construction" #assigns a description to a workhead
                combined = workhead + ' ' + workhead_description
                contractorcontain.at[index, 'workhead_description'] = combined

            elif 'ME' in workhead:
                workhead_description = "mechanical and electrical" #assigns a description to a workhead
                combined = workhead + ' ' + workhead_description
                contractorcontain.at[index, 'workhead_description'] = combined

            elif 'MW' in workhead:
                workhead_description = "maintenance" #assigns a description to a workhead
                combined = workhead + ' ' + workhead_description
                contractorcontain.at[index, 'workhead_description'] = combined


            elif 'TR' in workhead:
                workhead_description = "tradehead for subcontractor" #assigns a description to a workhead
                combined = workhead + ' ' + workhead_description
                contractorcontain.at[index, 'workhead_description'] = combined

            elif 'RW' in workhead:
                workhead_description = "regulatory workhead" #assigns a description to a workhead
                combined = workhead + ' ' + workhead_description
                contractorcontain.at[index, 'workhead_description'] = combined

            elif 'SY' in workhead:
                workhead_description = "supply" #assigns a description to a workhead
                combined = workhead + ' ' + workhead_description
                contractorcontain.at[index,'workhead_description'] = combined

            else:
                continue
        else:
            return "work head is empty"
    return contractorcontain.values.tolist()
    
def agencyFreq(agencyDict, tenderDict):
    agencyFreq = {}
    for agency in agencyDict:
        tenderList = agencyDict[agency]
        supplierDict = {}
        for tender in tenderList:
            for supplier in tenderDict[tender].supplierAwarded:
                if supplier in supplierDict:
                    supplierDict[supplier] += 1
                else:
                    supplierDict[supplier] = 1
        agencyFreq[agency] = supplierDict            
        
    return agencyFreq