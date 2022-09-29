from tkinter import *
from datetime import date, datetime



root = Tk() #initializes tkinter to create display window
root.geometry('500x300') # width and height of the window
root.resizable(0, 0) # sets fix size of window
root.title(' Age calculator') # gives the window a title



yourAge = Label(root,fg="red",text = "Date     Month     Year",font='arial 12 bold').place(x = 210)
setYourAlarm = Label(root,text = "Enter birthday: ",bg="grey",font="arial 11 bold").place(x=80, y=40)

date = StringVar()
month = StringVar()
year = StringVar()

dateTime= Entry(root,textvariable = date, relief = RAISED, width = 4,font=(20)).place(x=210,y=40)
monthTime= Entry(root,textvariable = month,width = 4,font=(20)).place(x=270,y=40)
yearTime = Entry(root,textvariable = year,width = 4,font=(20)).place(x=330,y=40)

def age():
    # Get current date
    today = datetime.today().date()

    setAge_year = int(year.get())
    setAge_month = int(month.get())
    setAge_date = int(date.get())

    current_age = today.year-int(setAge_year)
    if today.month < setAge_month or today.month == setAge_month and today.day < setAge_day:
         current_age -= 1


    CurrentLabel = Label(root, text=f'You are: {current_age} years old',fg='black')
    CurrentLabel.place(relx=0.2, rely=0.8, anchor=CENTER)

submit = Button(root,text = "Calculate your age",fg="red",width = 20,command=age,font=("arial 15 bold" )).place(x=90,y=100)
exit = Button(root,text = "Exit",fg="red",width = 10,command=root.destroy,font=("arial 20 bold" )).place(x=150,y=140)

root.mainloop()
