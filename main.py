import pandas as pd 
import numpy as np 
from openpyxl import load_workbook
from tkinter import *

root = Tk()
root.title("BRITISH ARMY TRAINING CENTER")
root.configure(background="#b3c1f2")
root.option_add( "*font", "Verdana  18" )  #setting default font and fontsize

#making frame
insert_frame= LabelFrame(root, padx=200,pady=50, bg="#8290bf")
view_frame= LabelFrame(root, bg="#455959")

#packing frame items 
insert_frame.grid( row=2, column= 0 ,padx=5, pady=5)
view_frame.grid( row=0, column= 0,padx=5, pady=5)

'''#making fullscreen
width_value= root.winfo_screenwidth()
height_value=root.winfo_screenwidth()
root.geometry("%dx%d" %(width_value,height_value))'''


def add():
    df = pd.DataFrame({'Name': [name_data.get()],
                    "Father's Name":[fathers_name_data.get()],
                    "GrandFather's Name":[grandfathers_name_data.get()],
                    'Age': [age_data.get()],
                    'Address':[address_data.get()],
                    'Contact':[contact_data.get()]

                })
    writer = pd.ExcelWriter('demo.xlsx', engine='openpyxl')
# try to open an existing workbook
    writer.book = load_workbook('demo.xlsx')
# copy existing sheets
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# read existing file
    reader = pd.read_excel(r'demo.xlsx')
# write out the new sheet
    df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

    writer.close()

#writer.close()
def delete(val):
    df = pd.read_excel('demo.xlsx', index_col=[0])
    df = df.drop([val], axis=0)
    
    df.to_excel("demo.xlsx")

    #print("Deleted sucessfully")
def search():
    df = pd.read_excel('demo.xlsx', index_col=[0])
    sear = df.loc[search_data.get()]
    print(search_data.get())
    print(sear)
    open(sear)
def open(value):
    top=Toplevel()
    top.title("View recruits info")
    Label(top,text=value).pack()
    print(val)
    #print(sear)
def edit(name):
    naam=input('Enter name:\n')
    age=input('Enter age\n')
    add(naam,age)
    delete(name)
def view():
    top=Toplevel()
    top.title("View recruits info")
    df=pd.read_excel('demo.xlsx', index_col=0)
    file = "demo.xlsx"
    wb = load_workbook(file, data_only=True)
    ws = wb.active

    r= 1
    for row in ws:
        c = 1
        for cell in row:
            Label(top,text=cell.value).grid(row=r,column=c)
            c+=1
        r+=1


#function for view button
'''def open():
    top=Toplevel()
    top.title("View recruits info")'''

#function for data input
def data():
    print(name_data.get())
    print(fathers_name_data.get())
    print(grandfathers_name_data.get())
    print(age_data.get())
    print(address_data.get())
    print(contact_data.get())
#pop up
def viewrec():
    df=pd.read_excel('demo.xlsx', index_col=0)
    tkMessageBox.showinfo("Details", str(df))

name_data=StringVar()
fathers_name_data=StringVar()
grandfathers_name_data=StringVar()
age_data=StringVar()
address_data=StringVar()
contact_data=StringVar()
search_data=StringVar()
#buttons
insert = Button(insert_frame, text="INSERT NEW RECRUITS",bg="#e4eded", fg="#063332",width=25, command=add)
view = Button(view_frame, text="VIEW RECRUITS INFO", bg="#e4eded", fg="#063332",command=view)
search = Button(view_frame, text="SEARCH", bg="#e4eded", fg="#063332",command=search)
#only for search
search_e = Entry(view_frame, textvariable=search_data)
search_e.grid(row=0, column=4)

insert.grid( row=7, column= 2)
view.grid( row=0, column= 1)
search.grid( row=0, column= 2)


#insert labels 

name = Label(insert_frame, text="Fullname :", padx=20, pady=20, bg="#8290bf",fg="white")
fathers_name = Label(insert_frame, text="Father's name :", padx=20, pady=20, bg="#8290bf",fg="white")
grandfathers_name = Label(insert_frame, text="Grandfather's name :", padx=20, pady=20, bg="#8290bf",fg="white")
age = Label(insert_frame, text="Age :", padx=20, pady=20, bg="#8290bf",fg="white")
address = Label(insert_frame, text="Address :", padx=20, pady=20, bg="#8290bf",fg="white")
contact = Label(insert_frame, text="Contact :", padx=20, pady=20, bg="#8290bf",fg="white")

#entry
name_e = Entry(insert_frame, textvariable=name_data, width=25)
fathers_name_e = Entry(insert_frame, textvariable=fathers_name_data, width=25)
grandfathers_name_e = Entry(insert_frame, textvariable=grandfathers_name_data,width=25)
age_e = Entry(insert_frame, textvariable=age_data,width=25)
address_e = Entry(insert_frame, textvariable=address_data,width=25)
contact_e = Entry(insert_frame, textvariable=contact_data,width=25)


name.grid(row=1, column=0)
name_e.grid(row=1, column=2, sticky="ew")
fathers_name.grid(row=2, column=0)
fathers_name_e.grid(row=2, column=2, sticky="ew")
grandfathers_name.grid(row=3, column=0)
grandfathers_name_e.grid(row=3, column=2, sticky="ew")
age.grid(row=4, column=0)
age_e.grid(row=4, column=2, sticky="ew")
address.grid(row=5, column=0)
address_e.grid(row=5, column=2, sticky="ew")
contact.grid(row=6, column=0)
contact_e.grid(row=6, column=2, sticky="ew")




root.mainloop()

