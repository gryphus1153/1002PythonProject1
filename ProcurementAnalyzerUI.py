#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Sep 27, 2018 04:23:01 PM CST  platform: Windows NT

import sys
import os
import pandas as pd
#import ProjOpenFunction
#import PythonProject
#import ProjFunction3

try:
    from Tkinter import *
    
except ImportError:
    from tkinter import *


try:
    import ttk
    import tkFileDialog
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    from tkinter import filedialog as tkFileDialog
    py3 = True

import ProcurementAnalyzerUI_support

def vp_start_gui(): #INIT
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Load_CSV(root)
    ProcurementAnalyzerUI_support.init(root, top)
    root.mainloop()

w = None
#============================== Global Vars ==========================#
import functionAmirulamin as Amin

contractorDict = {}
tenderDict = {}
agencyDict = {}

contractorPandas = None
tenderPandas = None

currentFileDir = os.path.dirname(__file__)

#default contractor file info
contractorFileRel = "ProjectDatasets\\listing-of-registered-contractors\\listing-of-registered-contractors.csv"
contractorFilePath = os.path.join(currentFileDir,contractorFileRel)

#default tender file info
tenderFileRel = "ProjectDatasets\\government-procurement\\government-procurement-via-gebiz.csv"
tenderFilePath = os.path.join(currentFileDir,tenderFileRel)

#============================== Functions ============================#
def changeScreen(cla, dset=None, ty=None):
    for widget in root.winfo_children():
        widget.destroy()
    
    if cla == "MainPage":
        MainPage(root)
    else:
        eval("%s(root,dataset=dset,datatype=ty)" %(cla))
        
        
def newWindow(cla, data=None):
    global topNew
    try:
        topNew.destroy()
    except:
        pass
        
    topNew = Toplevel()
    eval("%s(topNew, dataset = data)" %(cla))
    
    
def destroyWindow():
    topNew.destroy()
    
#============================== Classes ==============================#

class Load_CSV: #Opening screen to load CSV
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+684+224")
        top.title("Procurement Analyzer")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        #Contractor Button
        self.btn_uploadC = Button(top) 
        self.btn_uploadC.place(relx=0.717, rely=0.078, height=33, width=150)
        self.btn_uploadC.configure(activebackground="#d9d9d9")
        self.btn_uploadC.configure(activeforeground="#000000")
        self.btn_uploadC.configure(background="#d9d9d9")
        self.btn_uploadC.configure(disabledforeground="#a3a3a3")
        self.btn_uploadC.configure(foreground="#000000")
        self.btn_uploadC.configure(highlightbackground="#d9d9d9")
        self.btn_uploadC.configure(highlightcolor="black")
        self.btn_uploadC.configure(pady="0")
        self.btn_uploadC.configure(text='''Select Contractor File''')
        self.btn_uploadC.configure(command=lambda:self.getFilePath("Entry_C"))

        #Tender Button
        self.btn_uploadT = Button(top)
        self.btn_uploadT.place(relx=0.717, rely=0.167, height=33, width=150)
        self.btn_uploadT.configure(activebackground="#d9d9d9")
        self.btn_uploadT.configure(activeforeground="#000000")
        self.btn_uploadT.configure(background="#d9d9d9")
        self.btn_uploadT.configure(disabledforeground="#a3a3a3")
        self.btn_uploadT.configure(foreground="#000000")
        self.btn_uploadT.configure(highlightbackground="#d9d9d9")
        self.btn_uploadT.configure(highlightcolor="black")
        self.btn_uploadT.configure(pady="0")
        self.btn_uploadT.configure(text='''Select Tender File''')
        self.btn_uploadT.configure(command=lambda:self.getFilePath("Entry_T"))

        #Contractor Entry
        self.Entry_C = Entry(top)
        self.Entry_C.place(relx=0.05, rely=0.089,height=24, relwidth=0.64)
        self.Entry_C.configure(background="white")
        self.Entry_C.configure(disabledforeground="#a3a3a3")
        self.Entry_C.configure(font="TkFixedFont")
        self.Entry_C.configure(foreground="#000000")
        self.Entry_C.configure(highlightbackground="#d9d9d9")
        self.Entry_C.configure(highlightcolor="black")
        self.Entry_C.configure(insertbackground="black")
        self.Entry_C.configure(selectbackground="#c4c4c4")
        self.Entry_C.configure(selectforeground="black")
        self.Entry_C.insert(END, contractorFilePath)
        
        #Tender Entry
        self.Entry_T = Entry(top)
        self.Entry_T.place(relx=0.05, rely=0.178,height=24, relwidth=0.64)
        self.Entry_T.configure(background="white")
        self.Entry_T.configure(disabledforeground="#a3a3a3")
        self.Entry_T.configure(font="TkFixedFont")
        self.Entry_T.configure(foreground="#000000")
        self.Entry_T.configure(highlightbackground="#d9d9d9")
        self.Entry_T.configure(highlightcolor="black")
        self.Entry_T.configure(insertbackground="black")
        self.Entry_T.configure(selectbackground="#c4c4c4")
        self.Entry_T.configure(selectforeground="black")
        self.Entry_T.insert(END, tenderFilePath)

        #load button
        self.btn_upload = Button(top)
        self.btn_upload.place(relx=0.717, rely=0.267, height=33, width=150)
        self.btn_upload.configure(activebackground="#d9d9d9")
        self.btn_upload.configure(activeforeground="#000000")
        self.btn_upload.configure(background="#d9d9d9")
        self.btn_upload.configure(disabledforeground="#a3a3a3")
        self.btn_upload.configure(foreground="#000000")
        self.btn_upload.configure(highlightbackground="#d9d9d9")
        self.btn_upload.configure(highlightcolor="black")
        self.btn_upload.configure(pady="0")
        self.btn_upload.configure(text='''Load Files''')
        self.btn_upload.configure(command=lambda:self.loadFiles())

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.033, rely=0.378, relheight=0.571, relwidth=0.925)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)

    def getFilePath(self, type): #type is either Entry_C or Entry_T
        filePath = tkFileDialog.askopenfilename(initialdir = os.path.dirname(os.path.abspath(__file__)), filetypes = [("CSV file","*.csv")])
        eval("self." + type + ".delete(0,END)")
        eval("self." + type + ".insert(0,filePath)")
        
    def loadFiles(self): #load the files
        try:
            assert os.path.exists(self.Entry_C.get()), "Contractor File not found. Enter a valid file path."
            assert os.path.exists(self.Entry_T.get()), "Tender file not found. Enter a valid file path."
            assert ".csv" in self.Entry_C.get(), "Contractor file is not a .csv file"
            assert ".csv" in self.Entry_T.get(), "Tender file is not a .csv file"
            
            global contractorDict
            global tenderDict
            global contractorPanda
            global tenderPandas
            contractorDict = Amin.processContractors(self.Entry_C.get()) 
            tenderDict = Amin.processTenders(self.Entry_T.get())#dataFrame = ProjOpenFunction.garyopenfunction
            contractorPandas = pd.read_csv(self.Entry_C.get() , low_memory=False)#for li in dataFrame.values.tolist():
            tenderPandas = pd.read_csv(self.Entry_T.get() , low_memory=False)#    self.Scrolledlistbox1.insert(END, str(li))
            
            #for li in ProjFunction3.garyfunction3("asc").values.tolist():
            #    self.Scrolledlistbox1.insert(END, str(li))
            
            #chris
            #for item in PythonProject.workheads.construction.construction():
            #    self.Scrolledlistbox1.insert(END, str(item))
           
            #for key in contractorDict:
            #    self.Scrolledlistbox1.insert(END, contractorDict[key].toCSV())
            changeScreen("MainPage")
        except Exception as e:
            print(e)
            self.Scrolledlistbox1.insert(END, e)
            
            
class MainPage: #MANY DOORS THAT GO EVERYWHERE
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x450+457+222")
        top.title("Procurement Analyzer")
        top.configure(background="#d9d9d9")



        self.btn_vContractors = Button(top)
        self.btn_vContractors.place(relx=0.05, rely=0.044, height=33, width=146)
        self.btn_vContractors.configure(activebackground="#d9d9d9")
        self.btn_vContractors.configure(activeforeground="#000000")
        self.btn_vContractors.configure(background="#d9d9d9")
        self.btn_vContractors.configure(disabledforeground="#a3a3a3")
        self.btn_vContractors.configure(foreground="#000000")
        self.btn_vContractors.configure(highlightbackground="#d9d9d9")
        self.btn_vContractors.configure(highlightcolor="black")
        self.btn_vContractors.configure(pady="0")
        self.btn_vContractors.configure(text='''View Contractors''')
        self.btn_vContractors.configure(width=146)
        self.btn_vContractors.configure(command=lambda:changeScreen("View_Info",dset=contractorDict))

        self.btn_vTenders = Button(top)
        self.btn_vTenders.place(relx=0.05, rely=0.133, height=33, width=146)
        self.btn_vTenders.configure(activebackground="#d9d9d9")
        self.btn_vTenders.configure(activeforeground="#000000")
        self.btn_vTenders.configure(background="#d9d9d9")
        self.btn_vTenders.configure(disabledforeground="#a3a3a3")
        self.btn_vTenders.configure(foreground="#000000")
        self.btn_vTenders.configure(highlightbackground="#d9d9d9")
        self.btn_vTenders.configure(highlightcolor="black")
        self.btn_vTenders.configure(pady="0")
        self.btn_vTenders.configure(text='''View Tenders''')

        self.btn_vTenders_2 = Button(top)
        self.btn_vTenders_2.place(relx=0.05, rely=0.222, height=33, width=146)
        self.btn_vTenders_2.configure(activebackground="#d9d9d9")
        self.btn_vTenders_2.configure(activeforeground="#000000")
        self.btn_vTenders_2.configure(background="#d9d9d9")
        self.btn_vTenders_2.configure(disabledforeground="#a3a3a3")
        self.btn_vTenders_2.configure(foreground="#000000")
        self.btn_vTenders_2.configure(highlightbackground="#d9d9d9")
        self.btn_vTenders_2.configure(highlightcolor="black")
        self.btn_vTenders_2.configure(pady="0")
        self.btn_vTenders_2.configure(text='''View Agencies''')

        self.btnvTenders_3 = Button(top)
        self.btnvTenders_3.place(relx=0.05, rely=0.311, height=33, width=146)
        self.btnvTenders_3.configure(activebackground="#d9d9d9")
        self.btnvTenders_3.configure(activeforeground="#000000")
        self.btnvTenders_3.configure(background="#d9d9d9")
        self.btnvTenders_3.configure(disabledforeground="#a3a3a3")
        self.btnvTenders_3.configure(foreground="#000000")
        self.btnvTenders_3.configure(highlightbackground="#d9d9d9")
        self.btnvTenders_3.configure(highlightcolor="black")
        self.btnvTenders_3.configure(pady="0")
        self.btnvTenders_3.configure(text='''Function 2''')

        self.btnvTenders_3 = Button(top)
        self.btnvTenders_3.place(relx=0.05, rely=0.4, height=33, width=146)
        self.btnvTenders_3.configure(activebackground="#d9d9d9")
        self.btnvTenders_3.configure(activeforeground="#000000")
        self.btnvTenders_3.configure(background="#d9d9d9")
        self.btnvTenders_3.configure(disabledforeground="#a3a3a3")
        self.btnvTenders_3.configure(foreground="#000000")
        self.btnvTenders_3.configure(highlightbackground="#d9d9d9")
        self.btnvTenders_3.configure(highlightcolor="black")
        self.btnvTenders_3.configure(pady="0")
        self.btnvTenders_3.configure(text='''Function 3''')

        self.btnvTenders_3 = Button(top)
        self.btnvTenders_3.place(relx=0.05, rely=0.489, height=33, width=146)
        self.btnvTenders_3.configure(activebackground="#d9d9d9")
        self.btnvTenders_3.configure(activeforeground="#000000")
        self.btnvTenders_3.configure(background="#d9d9d9")
        self.btnvTenders_3.configure(disabledforeground="#a3a3a3")
        self.btnvTenders_3.configure(foreground="#000000")
        self.btnvTenders_3.configure(highlightbackground="#d9d9d9")
        self.btnvTenders_3.configure(highlightcolor="black")
        self.btnvTenders_3.configure(pady="0")
        self.btnvTenders_3.configure(text='''Function 4''')

        self.btn_col2 = Button(top)
        self.btn_col2.place(relx=0.3, rely=0.044, height=33, width=146)
        self.btn_col2.configure(activebackground="#d9d9d9")
        self.btn_col2.configure(activeforeground="#000000")
        self.btn_col2.configure(background="#d9d9d9")
        self.btn_col2.configure(disabledforeground="#a3a3a3")
        self.btn_col2.configure(foreground="#000000")
        self.btn_col2.configure(highlightbackground="#d9d9d9")
        self.btn_col2.configure(highlightcolor="black")
        self.btn_col2.configure(pady="0")
        self.btn_col2.configure(text='''Function 4''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        
class View_Info: #Lists out info
    def __init__(self, top=None, dataset=None, datatype=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+650+150")
        top.title("View Info")
        top.configure(background="#d9d9d9")
        self.dataset = dataset
        self.datatype = datatype

        self.btn_back = Button(top)
        self.btn_back.place(relx=0.033, rely=0.889, height=33, width=83)
        self.btn_back.configure(activebackground="#d9d9d9")
        self.btn_back.configure(activeforeground="#000000")
        self.btn_back.configure(background="#d9d9d9")
        self.btn_back.configure(disabledforeground="#a3a3a3")
        self.btn_back.configure(foreground="#000000")
        self.btn_back.configure(highlightbackground="#d9d9d9")
        self.btn_back.configure(highlightcolor="black")
        self.btn_back.configure(pady="0")
        self.btn_back.configure(text='''Back''')
        self.btn_back.configure(width=83)
        self.btn_back.configure(command = lambda: changeScreen("MainPage"))

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.033, rely=0.044, relheight=0.816
                , relwidth=0.925)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)
        for key in dataset.keys():
            self.Scrolledlistbox1.insert(END, key)

        self.btn_access = Button(top)
        self.btn_access.place(relx=0.817, rely=0.889, height=33, width=83)
        self.btn_access.configure(activebackground="#d9d9d9")
        self.btn_access.configure(activeforeground="#000000")
        self.btn_access.configure(background="#d9d9d9")
        self.btn_access.configure(disabledforeground="#a3a3a3")
        self.btn_access.configure(foreground="#000000")
        self.btn_access.configure(highlightbackground="#d9d9d9")
        self.btn_access.configure(highlightcolor="black")
        self.btn_access.configure(pady="0")
        self.btn_access.configure(text='''Access''')
        self.btn_access.configure(command = lambda: self.sendActive("View_Contractors"))
        
    def sendActive(self,cla):
        dataObj = self.dataset[self.Scrolledlistbox1.get(ACTIVE)]
        data = [dataObj.company_name, dataObj.uen_no, dataObj.address.toAddress(), dataObj.tel_no, dataObj.expiry_date, dataObj.workheadGrade]
        print data
        newWindow(cla,data)
        
        
class View_Contractors:
    def __init__(self, top=None, dataset=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x450+905+177")
        top.title("View Contractors")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        #Company Name
        self.lbl_name = Label(top)
        self.lbl_name.place(relx=0.033, rely=0.044, height=26, width=116)
        self.lbl_name.configure(activebackground="#f9f9f9")
        self.lbl_name.configure(activeforeground="black")
        self.lbl_name.configure(background="#d9d9d9")
        self.lbl_name.configure(disabledforeground="#a3a3a3")
        self.lbl_name.configure(foreground="#000000")
        self.lbl_name.configure(highlightbackground="#d9d9d9")
        self.lbl_name.configure(highlightcolor="black")
        self.lbl_name.configure(text='''Company Name:''')

        self.txt_cName = Text(top)
        self.txt_cName.place(relx=0.233, rely=0.044, relheight=0.053
                , relwidth=0.723)
        self.txt_cName.configure(background="white")
        self.txt_cName.configure(font="TkTextFont")
        self.txt_cName.configure(foreground="black")
        self.txt_cName.configure(highlightbackground="#d9d9d9")
        self.txt_cName.configure(highlightcolor="black")
        self.txt_cName.configure(insertbackground="black")
        self.txt_cName.configure(selectbackground="#c4c4c4")
        self.txt_cName.configure(selectforeground="black")
        self.txt_cName.configure(width=434)
        self.txt_cName.configure(wrap=WORD)
        self.txt_cName.insert(END, dataset[0])
        self.txt_cName.configure(state="disabled")

        
        #UEN no.
        self.lbl_uen = Label(top)
        self.lbl_uen.place(relx=0.117, rely=0.111, height=26, width=66)
        self.lbl_uen.configure(activebackground="#f9f9f9")
        self.lbl_uen.configure(activeforeground="black")
        self.lbl_uen.configure(background="#d9d9d9")
        self.lbl_uen.configure(disabledforeground="#a3a3a3")
        self.lbl_uen.configure(foreground="#000000")
        self.lbl_uen.configure(highlightbackground="#d9d9d9")
        self.lbl_uen.configure(highlightcolor="black")
        self.lbl_uen.configure(text='''UEN no.:''')
        
        self.txt_uen = Text(top)
        self.txt_uen.place(relx=0.233, rely=0.111, relheight=0.053
                , relwidth=0.723)
        self.txt_uen.configure(background="white")
        self.txt_uen.configure(font="TkTextFont")
        self.txt_uen.configure(foreground="black")
        self.txt_uen.configure(highlightbackground="#d9d9d9")
        self.txt_uen.configure(highlightcolor="black")
        self.txt_uen.configure(insertbackground="black")
        self.txt_uen.configure(selectbackground="#c4c4c4")
        self.txt_uen.configure(selectforeground="black")
        self.txt_uen.configure(width=434)
        self.txt_uen.configure(wrap=WORD)
        self.txt_uen.insert(END, dataset[1])
        self.txt_uen.configure(state="disabled")
        
        
        #Address
        self.lbl_address = Label(top)
        self.lbl_address.place(relx=0.117, rely=0.178, height=26, width=66)
        self.lbl_address.configure(activebackground="#f9f9f9")
        self.lbl_address.configure(activeforeground="black")
        self.lbl_address.configure(background="#d9d9d9")
        self.lbl_address.configure(disabledforeground="#a3a3a3")
        self.lbl_address.configure(foreground="#000000")
        self.lbl_address.configure(highlightbackground="#d9d9d9")
        self.lbl_address.configure(highlightcolor="black")
        self.lbl_address.configure(text='''Address:''')
        
        self.txt_address = Text(top)
        self.txt_address.place(relx=0.233, rely=0.178, relheight=0.053
                , relwidth=0.723)
        self.txt_address.configure(background="white")
        self.txt_address.configure(font="TkTextFont")
        self.txt_address.configure(foreground="black")
        self.txt_address.configure(highlightbackground="#d9d9d9")
        self.txt_address.configure(highlightcolor="black")
        self.txt_address.configure(insertbackground="black")
        self.txt_address.configure(selectbackground="#c4c4c4")
        self.txt_address.configure(selectforeground="black")
        self.txt_address.configure(width=434)
        self.txt_address.configure(wrap=WORD)
        self.txt_address.insert(END, dataset[2])
        self.txt_address.configure(state="disabled")
        
        
        #telephone number
        self.lbl_tel = Label(top)
        self.lbl_tel.place(relx=0.133, rely=0.244, height=26, width=53)
        self.lbl_tel.configure(background="#d9d9d9")
        self.lbl_tel.configure(disabledforeground="#a3a3a3")
        self.lbl_tel.configure(foreground="#000000")
        self.lbl_tel.configure(text='''Tel no.:''')
        
        self.txt_tel = Text(top)
        self.txt_tel.place(relx=0.233, rely=0.244, relheight=0.053
                , relwidth=0.723)
        self.txt_tel.configure(background="white")
        self.txt_tel.configure(font="TkTextFont")
        self.txt_tel.configure(foreground="black")
        self.txt_tel.configure(highlightbackground="#d9d9d9")
        self.txt_tel.configure(highlightcolor="black")
        self.txt_tel.configure(insertbackground="black")
        self.txt_tel.configure(selectbackground="#c4c4c4")
        self.txt_tel.configure(selectforeground="black")
        self.txt_tel.configure(width=434)
        self.txt_tel.configure(wrap=WORD)
        self.txt_tel.insert(END, dataset[3])
        self.txt_tel.configure(state="disabled")
        
        
        #expiry
        self.lbl_expiry = Label(top)
        self.lbl_expiry.place(relx=0.133, rely=0.311, height=26, width=49)
        self.lbl_expiry.configure(background="#d9d9d9")
        self.lbl_expiry.configure(disabledforeground="#a3a3a3")
        self.lbl_expiry.configure(foreground="#000000")
        self.lbl_expiry.configure(text='''Expiry:''')

        self.txt_expiry = Text(top)
        self.txt_expiry.place(relx=0.233, rely=0.311, relheight=0.053
                , relwidth=0.723)
        self.txt_expiry.configure(background="white")
        self.txt_expiry.configure(font="TkTextFont")
        self.txt_expiry.configure(foreground="black")
        self.txt_expiry.configure(highlightbackground="#d9d9d9")
        self.txt_expiry.configure(highlightcolor="black")
        self.txt_expiry.configure(insertbackground="black")
        self.txt_expiry.configure(selectbackground="#c4c4c4")
        self.txt_expiry.configure(selectforeground="black")
        self.txt_expiry.configure(width=434)
        self.txt_expiry.configure(wrap=WORD)
        self.txt_expiry.insert(END, dataset[4])
        self.txt_expiry.configure(state="disabled")
    
        
        #workheads
        self.lbl_workheads = Label(top)
        self.lbl_workheads.place(relx=0.083, rely=0.378, height=26, width=83)
        self.lbl_workheads.configure(activebackground="#f9f9f9")
        self.lbl_workheads.configure(activeforeground="black")
        self.lbl_workheads.configure(background="#d9d9d9")
        self.lbl_workheads.configure(disabledforeground="#a3a3a3")
        self.lbl_workheads.configure(foreground="#000000")
        self.lbl_workheads.configure(highlightbackground="#d9d9d9")
        self.lbl_workheads.configure(highlightcolor="black")
        self.lbl_workheads.configure(text='''Workheads:''')

        self.txt_workheads = Text(top)
        self.txt_workheads.place(relx=0.233, rely=0.378, relheight=0.52
                , relwidth=0.723)
        self.txt_workheads.configure(background="white")
        self.txt_workheads.configure(font="TkTextFont")
        self.txt_workheads.configure(foreground="black")
        self.txt_workheads.configure(highlightbackground="#d9d9d9")
        self.txt_workheads.configure(highlightcolor="black")
        self.txt_workheads.configure(insertbackground="black")
        self.txt_workheads.configure(selectbackground="#c4c4c4")
        self.txt_workheads.configure(selectforeground="black")
        self.txt_workheads.configure(width=434)
        self.txt_workheads.configure(wrap=WORD)
        for workhead in dataset[5]:
            self.txt_workheads.insert(END, workhead + " : " + dataset[5][workhead] + "\n")
        self.txt_workheads.configure(state="disabled")
        
        
        #Close Button
        self.btn_close = Button(top)
        self.btn_close.place(relx=0.05, rely=0.8, height=33, width=78)
        self.btn_close.configure(activebackground="#d9d9d9")
        self.btn_close.configure(activeforeground="#000000")
        self.btn_close.configure(background="#d9d9d9")
        self.btn_close.configure(disabledforeground="#a3a3a3")
        self.btn_close.configure(foreground="#000000")
        self.btn_close.configure(highlightbackground="#d9d9d9")
        self.btn_close.configure(highlightcolor="black")
        self.btn_close.configure(pady="0")
        self.btn_close.configure(text='''Close''')
        self.btn_close.configure(command = lambda: destroyWindow())
        
        
# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()

