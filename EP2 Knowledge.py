from tkinter import *
from tkinter import ttk # them of tk
from tkinter import messagebox
GUI=Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') # ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดโปรแกรม

L1=Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
###########
def Button2() :
    text='ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1=Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=80)
B2=ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
#B2.pack(ipadx=20,ipady=20) #ขนาดปุ่ม
B2.pack(ipadx=20,ipady=20,)
###########

###########
def Button3() :
    text='Python 101. Math'
    messagebox.showinfo('วิชาเรียน 10-20 ก.พ. ',text)

FB2=Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=180)
B3=ttk.Button(FB2,text='สัปดาห์นีเรียนวิชาอะไร',command=Button3)
#B2.pack(ipadx=20,ipady=20) #ขนาดปุ่ม
B3.pack(ipadx=20,ipady=20,)
###########
GUI.mainloop()
