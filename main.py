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
    gsheet = gc.open('store_data')
    wks = gsheet[0]

    #Read specific range
    data = wks.get_values('A1', end='A20')
    last_non_empty_index = -1
    for i, value in enumerate(data):
        if value is not None:
            last_non_empty_index = i
    last_empty_cell = last_non_empty_index + 1   
    # Set DataFrame to sheet without header
    if last_non_empty_index == 0:
        df = pd.DataFrame({'Firstname': [fname], 'Lastname': [lname], 'Email': [email]})
        wks.set_dataframe(df, start=(last_empty_cell,1), value_input_option='RAW') 
    else:
        wks.update_value((last_empty_cell+1, 1), fname)  # Insert first name in column A
        wks.update_value((last_empty_cell+1, 2), lname)  # Insert last name in column B
        wks.update_value((last_empty_cell+1, 3), email)  # Insert email in column C
form()
