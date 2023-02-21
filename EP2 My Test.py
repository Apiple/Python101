from tkinter import *
from tkinter import ttk
from tkinter import messagebox
GUI=Tk()
GUI.title('Program for Planning')
GUI.geometry('700x700')

L1=Label(GUI,text='Planing system',font=('Angsana New',30),fg='blue')
L1.place(x=30,y=20)

#######
def Button1() :
    text='Current Stock today'
    messagebox.showinfo('Show status stock',text)
    
FB1=Frame(GUI)
FB1.place(x=100,y=100)
B1=ttk.Button(FB1,text='Current Stock',command=Button1)
B1.pack(ipadx=40,ipady=20,)
#########

#####
def Button2() :
    text='Remain schedule'
    messagebox.showinfo('Show status',text)

FB2=Frame(GUI)
FB2.place(x=100,y=200)
B2=ttk.Button(FB2,text='Total Plan Delevery',command=Button2)
B2.pack(ipadx=25,ipady=20,)
########

#######
def Button3() :
    text='Totoal this month are'
    messagebox.showinfo('Show total order',text)

FB3=Frame(GUI)
FB3.place(x=100,y=300)
B3=ttk.Button(FB3,text='Order this month',command=Button3)
B3.pack(ipadx=25,ipady=20,)
########

#######
def Button4() :
    text='Total forcast Next N+1 are'
    messagebox.showinfo('Show total Forcast N+1',text)

FB4=Frame(GUI)
FB4.place(x=400,y=100)
B4=ttk.Button(FB4,text='Forecast N+1',command=Button4)
B4.pack(ipadx=25,ipady=20,)
########

#######
def Button5() :
    text='Total forcast Next N+2 are'
    messagebox.showinfo('Show total Forcast N+2',text)

FB5=Frame(GUI)
FB5.place(x=400,y=200)
B5=ttk.Button(FB5,text='Forecast N+2',command=Button5)
B5.pack(ipadx=25,ipady=20,)
########

########
def Button6() :
    text='Total forcast Next N+3 are'
    messagebox.showinfo('Show total Forcast N+3',text)

FB6=Frame(GUI)
FB6.place(x=400,y=300)
B6=ttk.Button(FB6,text='Forecast N+3',command=Button6)
B6.pack(ipadx=25,ipady=20,)
########

########
def Button7() :
    text='This month it different are'
    messagebox.showinfo('Show different',text)

FB7=Frame(GUI)
FB7.place(x=200,y=400)
B7=ttk.Button(FB7,text='Compare Order VS Actual Delivery',command=Button7)
B7.pack(ipadx=25,ipady=20,)
########


GUI.mainloop
