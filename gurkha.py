''' IMPORTING NECCESARY PACKAGES'''

from tkinter import *
from tkinter import ttk
import datetime
import time
import tkinter.messagebox
import sqlite3
import os 

''' IMPORTING SUCCESSFUL'''

''' CREATING CLASS'''


class School_Portal:
    db_name=os.getcwd()
    db_name=db_name+"\\datas.db"
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x725+400+150')
        self.root.title('GURKHA COMPANY TRAINING CENTER')
        self.root.iconbitmap("icon.ico")

        '''Logo and Title'''

        self.photo = PhotoImage(file='photoo.png')
        self.label = Label(image=self.photo)
        self.label.grid(row=0, column=0)

        self.label1 = Label(font=('arial', 15, 'bold'), text='Portal System', fg='dark blue')
        self.label1.grid(row=8, column=0)

        ''' New Records '''
        frame = LabelFrame(self.root, text='Add New Record:')
        frame.grid(row=0, column=1)

        Label(frame, text='Fullname:').grid(row=1, column=1, sticky=W)
        self.fullname = Entry(frame, width = 30)
        self.fullname.grid(row=1, column=2)

        Label(frame, text="Father's name :").grid(row=2, column=1, sticky=W)
        self.fathersname = Entry(frame, width = 30)
        self.fathersname.grid(row=2, column=2)

        Label(frame, text="GrandFather's name :").grid(row=3, column=1, sticky=W)
        self.grandfathername = Entry(frame, width = 30)
        self.grandfathername.grid(row=3, column=2)

        Label(frame, text='ID:').grid(row=4, column=1, sticky=W)
        self.username = Entry(frame, width = 30)
        self.username.grid(row=4, column=2)

        Label(frame, text='Address:').grid(row=5, column=1, sticky=W)
        self.address = Entry(frame, width = 30)
        self.address.grid(row=5, column=2)

        Label(frame, text='Age:').grid(row=6, column=1, sticky=W)
        self.age = Entry(frame, width = 30)
        self.age.grid(row=6, column=2)

        Label(frame, text='Contact:').grid(row=7, column=1, sticky=W)
        self.contact = Entry(frame, width = 30)
        self.contact.grid(row=7, column=2)  

        Label(frame, text='Amount Paid:').grid(row=8, column=1, sticky=W)
        self.amount = Entry(frame, width = 15)
        self.amount.grid(row=8, column=2, sticky = W)
        
        test1 = StringVar(frame, value= self.amount)
        list1= ['Baisakh','Jestha','Ashad','Shrawan','Bhadra','Ashwin','Kartik','Mangsir','Poush','Magh','Falgun','Chaitra']
        droplist = OptionMenu(frame,test1,*list1)
        droplist.config(width = 7)
        test1.set('Baisakh')
        droplist.grid(row = 8,column =2, sticky= "e")
        
    
        #Add Button'''
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background = '#ADD8E6', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='black')
        style.map('TButton', background=[('active','#ADD8E6')])

        ttk.Button(frame, text='Add Record', command=self.add).grid(row=9, column=2,sticky = E)
        ttk.Button(frame, text='Add Photo', command=self.add_photo).grid(row=9, column=1)



        '''Message Display'''
        self.message = Label(text='', fg='Red')
        self.message.grid(row=9, column=1)
        

        '''Database Table display box '''
        self.tree = ttk.Treeview( column=['', '', '', '', '', '',''])
        self.tree.grid(row=11, column=0, columnspan=4)
        self.tree.heading('#0', text='ID')
        self.tree.column('#0', width=50)
        self.tree.heading('#1', text='Full Name')
        self.tree.column('#1', width=100)
        self.tree.heading('#2', text="Father's Name")
        self.tree.column('#2', width=100)
        self.tree.heading('#3', text="Grandfather's Name")      
        self.tree.column('#3', width=150, stretch=3)
        self.tree.heading('#4', text='Address')
        self.tree.column('#4', width=100)
        self.tree.heading('#5', text='Age')
        self.tree.column('#5', width=40, stretch=False)
        self.tree.heading('#6', text='Contact')
        self.tree.column('#6', width=120)
        self.tree.heading('#7', text='Amount Paid')
        self.tree.column('#7', width=120)

        #scrollbar adding to treeview
        self.treeScrollbar=ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.treeScrollbar.set)
        self.treeScrollbar.grid(row=11,column=5,sticky="ns")
        
        '''Time and Date'''
        
        def tick():
            d = datetime.datetime.now()
            today = '{:%B %d,%Y}'.format(d)

            mytime = time.strftime('%I:%M:%S%p')
            self.lblInfo.config(text=(mytime + '\t' + today))
            self.lblInfo.after(200, tick)

        self.lblInfo = Label(font=('arial', 20, 'bold'), fg='Dark green')
        self.lblInfo.grid(row=10, column=0, columnspan=2)
        tick()

        ''' Menu Bar '''
        Chooser = Menu()
        itemone = Menu()

        itemone.add_command(label='Add Record', command=self.add)
        itemone.add_command(label='Edit Record', command=self.edit)
        itemone.add_command(label='Delete Record', command=self.delet)
        itemone.add_separator()
        itemone.add_command(label='Help', command=self.help)
        itemone.add_command(label='Exit', command=self.ex)

        Chooser.add_cascade(label='File', menu=itemone)
        Chooser.add_command(label='Add', command=self.add)
        Chooser.add_command(label='Edit', command=self.edit)
        Chooser.add_command(label='Delete', command=self.delet)
        Chooser.add_command(label='Help', command=self.help)
        Chooser.add_command(label='Exit', command=self.ex)

        root.config(menu=Chooser)
        self.veiwing_records()

        '''add photo'''
    def addp(self,name):
        b=0
        '''for row in ws.rows:
                if (not row[0].value):
                    break
                elif (row[0].value == rollnumber_data.get()):
                    b = 1
                    break
            if (b ==1):
                pop("Unable to add photo","Student data with that roll number exists.")
            '''

        import os
        import shutil
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
        desktop = desktop + "\\student\\"
        if not os.path.isdir(desktop):
            os.mkdir(desktop)
        desktop=desktop+str(self.username.get())+".png"
    #os.rename(name, desktop)
        shutil.copyfile(name, desktop)
        self.message['text'] = 'Photo moved to'+desktop +' sucessfully.'
    #os.replace(name, desktop)
    '''except:
        pop("Failed","Failed to move photo")'''
    def add_photo(self):
        from tkinter import filedialog
        import os
        #print("here")
        try:
            if not self.username.get():
                self.message['text'] = 'Enter ID before entering data...'
            else:
                rep = filedialog.askopenfilenames(
                    parent=root,
                    initialdir='/',
                    initialfile='tmp',
                    filetypes=[
                        ("All files", "*"),
                        ("PNG", "*.png"),
                        ("JPEG", "*.jpg"),
                        ("JPG","*.jpg")])
                rep1 = ''.join(rep)
        except IndexError:
            self.message['text'] = 'Fields to move photo...' 
        self.addp(str(rep1))

        

    ''' View Database Table'''


    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS studentlist
             ([Roll_number] INTEGER PRIMARY KEY,[Student_Name] text,[Student_Father_Name] text,[Student_Grandfather_Name] text,[Address] text,[Age] integer ,[Amount] integer, [Contact] text)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS month
              ([Roll_nmber] INTEGER PRIMARY KEY,[Baisakh] integer,[Jestha] integer,[Ashad] integer, [Shrawan] integer,[Bhadra] integer,[Ashwin] integer,[Kartik] integer,[Mangsir] integer,[Poush] integer,[Magh] integer,[Falgun] integer,[Chaitra] integer,[total] integer)''')
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result

    def veiwing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * FROM studentlist'
        db_table = self.run_query(query)
        for data in db_table:
            self.tree.insert('', 1000, text=data[0], values=data[1:])

    ''' Add New Record '''

    def validation(self):
        return len(self.fullname.get()) != 0 and len(self.fathersname.get()) != 0 and len(self.username.get()) != 0 and \
               len(self.address.get()) != 0 and len(self.age.get()) != 0 and len(self.amount.get()) != 0  and len(self.contact.get()) !=0

    def add_record(self):
        if self.validation():
            query = 'INSERT INTO studentlist VALUES (?,?,?,?,?,?,?,?)'
            parameters = (self.username.get(),self.fullname.get(), self.fathersname.get(),
                          self.grandfathername.get(),self.address.get(),self.age.get(),self.contact.get(), self.amount.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Record {} added!'.format(self.fullname.get())


            '''Empty the fields'''
            self.fullname.delete(0, END)
            self.fathersname.delete(0, END)
            self.grandfathername.delete(0, END)
            self.username.delete(0, END)
            self.address.delete(0, END)
            self.age.delete(0, END)
            self.amount.delete(0, END)
            self.contact.delete(0, END)

        else:
            self.message['text'] = 'Fields not completed! Complete all fields...'

        self.veiwing_records()

    '''Function for using buttons'''

    def add(self):
        ad = tkinter.messagebox.askquestion('Add Record', 'Do you want to add a New Record?')
        if ad == 'yes':
            self.add_record()


    ''' Deleting a Record '''

    def delete_record(self):
        # To clear output
        self.message['text'] = ''

        try:
            # why 1? --Can be anything
            self.tree.item(self.tree.selection())['values'][1]

        except IndexError as e:
            self.message['text'] = 'Please select a record to delete!'
            return

        # Again clear output
        self.message['text'] = ''
        # ???why text
        number = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM studentlist WHERE ID = ?'
        # Why comma
        self.run_query(query, (number,))
        self.message['text'] = 'Record {} deleted!'.format(number)

        # Printing new database

        self.veiwing_records()

    # Function to add functionality in buttons

    def delet(self):
        de = tkinter.messagebox.askquestion('Delete Record', 'Are you sure you want to delete this Record?')
        if de == 'yes':
            self.delete_record()

    '''EDIT RECORD'''

    '''CREATING A POP UP WINDOW FOR EDIT'''

    def edit_box(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]

        except IndexError as e:
            self.message['text'] = 'Please select a Record to Edit!'
            return

        fname = self.tree.item(self.tree.selection())['values'][0]  #fullname
        father_name = self.tree.item(self.tree.selection())['values'][1]  #fathersname
        grandfather_name = self.tree.item(self.tree.selection())['values'][2]  #gndfathers name
        address = self.tree.item(self.tree.selection())['values'][3]  #address
        age = self.tree.item(self.tree.selection())['values'][4]    #age 
        contact = self.tree.item(self.tree.selection())['values'][5]    #contact
        amt = self.tree.item(self.tree.selection())['values'][6]    #amount

        print(fname,father_name,grandfather_name,address,age,contact,amt)

        self.edit_root = Toplevel()
        self.edit_root.title('Edit Record')
        self.edit_root.geometry('350x435+600+200')

        Label(self.edit_root, text='Fullname (Old)').grid(row=0, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=fname), state='readonly').grid(row=0,
                                                                                                          column=2)
        Label(self.edit_root, text='Fullname (New)').grid(row=1, column=1, sticky=W)
        new_fname = Entry(self.edit_root , textvariable=StringVar(self.edit_root, value=fname))
        new_fname.grid(row=1, column=2)

        Label(self.edit_root, text="Father's name (Old)").grid(row=2, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=father_name), state='readonly').grid(row=2,
                                                                                                          column=2)
        Label(self.edit_root, text="Father's name (New)").grid(row=3, column=1, sticky=W)
        new_father_name = Entry(self.edit_root,textvariable=StringVar(self.edit_root, value=father_name))
        new_father_name.grid(row=3, column=2)

        Label(self.edit_root, text="Grandfather's name (Old)").grid(row=4, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=grandfather_name), state='readonly').grid(row=4,
                                                                                                          column=2)
        Label(self.edit_root, text="Grandfather's name (New)").grid(row=5, column=1, sticky=W)
        new_grandfather_name = Entry(self.edit_root,textvariable=StringVar(self.edit_root, value=grandfather_name))
        new_grandfather_name.grid(row=5, column=2)

        Label(self.edit_root, text='Address (Old)').grid(row=6, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=address), state='readonly').grid(row=6,
                                                                                                          column=2)
        Label(self.edit_root, text='Address (New)').grid(row=7, column=1, sticky=W)
        new_address = Entry(self.edit_root,textvariable=StringVar(self.edit_root, value=address))
        new_address.grid(row=7, column=2)

        Label(self.edit_root, text='Age (Old)').grid(row=8, column=1, sticky=W)
        Entry(self.edit_root, textvariable=IntVar(self.edit_root, value=age), state='readonly').grid(row=8,
                                                                                                            column=2)
        Label(self.edit_root, text='Age (New)').grid(row=9, column=1, sticky=W)
        new_age = Entry(self.edit_root,textvariable=IntVar(self.edit_root, value=age))
        new_age.grid(row=9, column=2)

        Label(self.edit_root, text='Contact (Old)').grid(row=10, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=contact), state='readonly').grid(row=10,
                                                                                                        column=2)
        Label(self.edit_root, text='Contact (New)').grid(row=11, column=1, sticky=W)
        new_contact = Entry(self.edit_root,textvariable=StringVar(self.edit_root, value=contact))
        new_contact.grid(row=11, column=2)

        Label(self.edit_root, text='Amount Paid (Old)').grid(row=12, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=amt), state='readonly').grid(row=12,
                                                                                                        column=2)
        Label(self.edit_root, text='Amount Paid (New)').grid(row=13, column=1, sticky=W)
        new_amt = Entry(self.edit_root,textvariable=StringVar(self.edit_root, value=amt), width = 8)
        new_amt.grid(row=13, column=2, sticky = W)

        test = StringVar(self.edit_root, value=amt)
        list1= ['Baisakh','Jestha','Ashad','Shrawan','Bhadra','Ashwin','Kartik','Mangsir','Poush','Magh','Falgun','Chaitra']
        droplist = OptionMenu(self.edit_root,test,*list1)
        droplist.config(width = 5)
        test.set('Baisakh')
        droplist.grid(row = 13,column =2, sticky= "e")

       

        Button(self.edit_root, text='Save Changes', command=lambda: self.edit_record(new_fname.get(), fname, new_father_name.get(), father_name, new_grandfather_name.get(), grandfather_name, new_address.get(), address, new_age.get(), age, new_contact.get(), contact, new_amt.get(),amt)).grid(row=14, column=2, sticky=W)

        self.edit_root.mainloop()

    def edit_record(self, new_fname, fname, new_father_name, father_name, new_grandfather_name, grandfather_name, new_address, address, new_age, age, new_contact, contact, new_amt, amt):

        query = 'UPDATE studentlist SET Student_name=?, Student_Father_Name=?, Student_Grandfather_Name=?, Address=?, Age=?, Amount=?, Contact=? WHERE ' \
                'Student_name=? AND Student_Father_Name=? AND Student_Grandfather_Name=? AND Address=? AND Age=? AND Amount=? AND Contact=?'

        parameters = (new_fname, new_father_name, new_grandfather_name, new_address, new_age, new_contact,new_amt, fname, father_name, grandfather_name, address,age, contact, amt)
        self.run_query(query, parameters)
        self.edit_root.destroy()
        self.message['text'] = '{} details are changed to {}'.format(fname, new_fname)
        self.veiwing_records()

    def edit(self):
        ed = tkinter.messagebox.askquestion('Edit Record', 'Want to Edit this Record?')
        if ed == 'yes':
            self.edit_box()

    '''HELP'''
    def help(self):
        tkinter.messagebox.showinfo('Log','Report Sent!')

    '''EXIT'''
    def ex(self):
        exit = tkinter.messagebox.askquestion('Exit Application','Are you sure you want to close this application?')
        if exit == 'yes':
            self.root.destroy()


'''MAIN'''

if __name__ == '__main__':
    root = Tk()
    #root.geometry('700x515+500+200')
    application = School_Portal(root)
    root.mainloop()