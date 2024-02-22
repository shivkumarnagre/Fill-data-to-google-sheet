import pygsheets
import pandas as pd
from tkinter import *

def form():
    root = Tk()
    root.title("Details")
    root.geometry('600x400')
    root.resizable(0,0)  
    Label(root,text = "Information", font='arial 20 bold').pack()
    
    fname_label = Label(root, text="Enter your first name:").pack()#.place(x= 32, y= 90)
    fname_field = Entry(root, width= 30)#.place(x= 32, y= 90)
    fname_field.pack()

    lname_label = Label(root, text="Enter your last name:").pack()
    lname_field = Entry(root, width=30)
    lname_field.pack()

    email_label = Label(root, text="Enter your Email:").pack()
    email_field = Entry(root, width=30)
    email_field.pack()

    btn = Button(root,text='Submit',  font='arial 15 bold', bg='pale violet red', command= lambda: submit(fname_field.get(), lname_field.get(), email_field.get()))
    btn.pack()
    root.mainloop()

def submit(fname, lname, email):
    print(f"Submitted: {fname}, {lname}, {email}")
    gc = pygsheets.authorize(service_file='Credential.json')
    df = pd.DataFrame()
    df['Firstame'] = [fname] 
    df['Lastname'] = [lname]
    df['Email'] = [email]
    gsheet = gc.open('store_data')
    wks = gsheet[0]
   # wks.set_dataframe(df,(1,1))
    wks.set_dataframe(df,(1,1))
form()

