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
        self.root.geometry('800x525+400+200')
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
        self.fullname = Entry(frame)
        self.fullname.grid(row=1, column=2)

        Label(frame, text="Father's name :").grid(row=2, column=1, sticky=W)
        self.fathersname = Entry(frame)
        self.fathersname.grid(row=2, column=2)

        Label(frame, text="GrandFather's name :").grid(row=3, column=1, sticky=W)
        self.grandfathername = Entry(frame)
        self.grandfathername.grid(row=3, column=2)

        Label(frame, text='ID:').grid(row=4, column=1, sticky=W)
        self.username = Entry(frame)
        self.username.grid(row=4, column=2)

        Label(frame, text='Address:').grid(row=5, column=1, sticky=W)
        self.address = Entry(frame)
        self.address.grid(row=5, column=2)

        Label(frame, text='Age:').grid(row=6, column=1, sticky=W)
        self.age = Entry(frame)
        self.age.grid(row=6, column=2)

        Label(frame, text='Contact:').grid(row=7, column=1, sticky=W)
        self.contact = Entry(frame)
        self.contact.grid(row=7, column=2)  

        Label(frame, text='Amount Paid:').grid(row=8, column=1, sticky=W)
        self.amount = Entry(frame)
        self.amount.grid(row=8, column=2)
    
        '''Add Button'''
        ttk.Button(frame, text='Add Record', command=self.add).grid(row=9, column=2)
        ttk.Button(frame, text='Add Photo', command=self.photo).grid(row=9, column=1)



        '''Message Display'''
        self.message = Label(text='', fg='Red')
        self.message.grid(row=9, column=1)

        '''Database Table display box '''
        self.tree = ttk.Treeview(height=10, column=['', '', '', '', '', '','',''])
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
            self.message['text'] = 'Record {} {} added!'.format(self.fullname.get(), self.username.get())

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

        fname = self.tree.item(self.tree.selection())['values'][0]
        lname = self.tree.item(self.tree.selection())['values'][1]
        uname = self.tree.item(self.tree.selection())['values'][2]
        email = self.tree.item(self.tree.selection())['values'][3]
        subject = self.tree.item(self.tree.selection())['values'][4]
        age = self.tree.item(self.tree.selection())['values'][5]

        self.edit_root = Toplevel()
        self.edit_root.title('Edit Record')
        self.edit_root.geometry('305x355+600+200')

        Label(self.edit_root, text='Old Firstname').grid(row=0, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=fname), state='readonly').grid(row=0,
                                                                                                          column=2)
        Label(self.edit_root, text='New Firstname').grid(row=1, column=1, sticky=W)
        new_fname = Entry(self.edit_root , textvariable=StringVar(self.edit_root, value=fname))
        new_fname.grid(row=1, column=2)

        Label(self.edit_root, text='Old Lastname').grid(row=2, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=lname), state='readonly').grid(row=2,
                                                                                                          column=2)
        Label(self.edit_root, text='New Lastname').grid(row=3, column=1, sticky=W)
        new_lname = Entry(self.edit_root,textvariable=StringVar(self.edit_root, value=lname))
        new_lname.grid(row=3, column=2)

        Label(self.edit_root, text='Old Username').grid(row=4, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=uname), state='readonly').grid(row=4,
                                                                                                          column=2)
        Label(self.edit_root, text='New Username').grid(row=5, column=1, sticky=W)
        new_uname = Entry(self.edit_root,textvariable=StringVar(self.edit_root, value=uname))
        new_uname.grid(row=5, column=2)

        Label(self.edit_root, text='Old Email').grid(row=6, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=email), state='readonly').grid(row=6,
                                                                                                          column=2)
        Label(self.edit_root, text='New Email').grid(row=7, column=1, sticky=W)
        new_email = Entry(self.edit_root,textvariable=StringVar(self.edit_root, value=email))
        new_email.grid(row=7, column=2)

        Label(self.edit_root, text='Old Subject').grid(row=8, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=subject), state='readonly').grid(row=8,
                                                                                                            column=2)
        Label(self.edit_root, text='New Subject').grid(row=9, column=1, sticky=W)
        new_subject = Entry(self.edit_root,textvariable=StringVar(self.edit_root, value=subject))
        new_subject.grid(row=9, column=2)

        Label(self.edit_root, text='Old Age').grid(row=10, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root, value=age), state='readonly').grid(row=10,
                                                                                                        column=2)
        Label(self.edit_root, text='New Age').grid(row=11, column=1, sticky=W)
        new_age = Entry(self.edit_root,textvariable=StringVar(self.edit_root, value=age))
        new_age.grid(row=11, column=2)

        Button(self.edit_root, text='Save Changes', command=lambda: self.edit_record(new_fname.get(), fname, new_lname.get(), lname, new_uname.get(), uname, new_email.get(), email,new_subject.get(), subject, new_age.get(), age)).grid(row=12, column=2, sticky=W)

        self.edit_root.mainloop()

    def edit_record(self, new_fname, fname, new_lname, lname, new_uname, uname, new_email, email, new_subject, subject,
                    new_age, age):
        query = 'UPDATE studentlist SET Firstname=?, Lastname=?, Username=?, Email=?, Subject=?, Age=? WHERE ' \
                'Firstname=? AND Lastname=? AND Username=? AND Email=? AND Subject=? AND Age=?'

        parameters = (new_fname, new_lname, new_uname, new_email, new_subject, new_age, fname, lname, uname, email,subject, age)
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