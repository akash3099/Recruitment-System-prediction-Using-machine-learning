#import library

from tkinter import *
import tkinter.messagebox as ms
from PIL import ImageTk, Image
from project2 import *

#define window

top=Tk()
top.title("RECRUITMENT RESULT")
top.configure(background="#0a2845#")
top.geometry("1000x800")
top.resizable(True,True)

#Front Decoration

a1=Label(top,text="  Techwise India Ltd.",fg="White",bg="#0a2845#",font="Times 24 bold",bd=15)
a1.grid(row=0,column=0,pady=30,columnspan=10)

path = "shake-hands-final.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(top, image = img,fg="White",height=150,width=400)
panel.grid(row=0,column=10,sticky=W,columnspan=1)

#Entry

name=StringVar()
e1=Entry(top,textvariable=name,width=35,bd=3,bg="powder blue")
e1.grid(row=2,column=2,pady=15)

per=StringVar()
e2=Entry(top,textvariable=per,width=35,bd=3,bg="powder blue")
e2.grid(row=3,column=2,pady=15)

backlog=StringVar()
e3=Entry(top,textvariable=backlog,width=35,bd=3,bg="powder blue")
e3.grid(row=4,column=2,pady=15)

intern=StringVar()
e4=Entry(top,textvariable=intern,width=35,bd=3,bg="powder blue")
e4.grid(row=5,column=2,pady=15)

round=StringVar()
e5=Entry(top,textvariable=round,width=35,bd=3,bg="powder blue")
e5.grid(row=6,column=2,pady=15)

comm=StringVar()
e6=Entry(top,textvariable=comm,width=35,bd=3,bg="powder blue")
e6.grid(row=7,column=2,pady=15)

#function to get dat from entry and feed it into machine model to get outcome
def get_data():
    name1=name.get()
    per1=int(per.get())
    backlog1=int(backlog.get())
    intern1=int(intern.get())
    round1=int(round.get())
    comm1=int(comm.get())
    tree=DecisionTreeClassifier12(per1,backlog1,intern1,round1,comm1)
    forest=randomforest12(per1,backlog1,intern1,round1,comm1)
    Regression=regression12(per1,backlog1,intern1,round1,comm1)

    return (tree,forest,Regression)


#Funtion to clear Entry


def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)

#function to print Decision on screen
def out12():
    tree,forest,Regression=get_data()
    if tree==1:
     out.set('Hired')
    elif tree==0:
     out.set('Not..Hired..')

def out13():
    tree,forest,Regression=get_data()
    if forest==1:
     out2.set('Hired')
    elif forest==0:
     out2.set('Not..Hired..')

def out14():
    tree,forest,Regression=get_data()
    if Regression==1:
     out3.set('Hired')
    elif Regression==0:
     out3.set('Not..Hired..')

#function to write result in csv file

def Hire():
    name1=name.get()
    per1=int(per.get())
    backlog1=int(backlog.get())
    intern1=int(intern.get())
    round1=int(round.get())
    comm1=int(comm.get())
    myData = [[name1,per1,backlog1,intern1,round1,comm1,1]]
    myFile = open('PerpData.csv', 'a',newline='')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)


def Not_Hire():
    name1=name.get()
    per1=int(per.get())
    backlog1=int(backlog.get())
    intern1=int(intern.get())
    round1=int(round.get())
    comm1=int(comm.get())
    myData = [[name1,per1,backlog1,intern1,round1,comm1,0]]
    myFile = open('PerpData.csv', 'a',newline='')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)


#Define output widget
out=StringVar()
c1=Label(top,textvariable=out,height=2,width=27,fg="White",bg="#0a2845#",font="Times 14 bold")
c1.grid(row=3,column=17)
out2=StringVar()
c6=Label(top,textvariable=out2,height=2,width=27,fg="White",bg="#0a2845#",font="Times 14 bold")
c6.grid(row=4,column=17)
out3=StringVar()
c7=Label(top,textvariable=out3,height=2,width=27,fg="White",bg="#0a2845#",font="Times 14 bold")
c7.grid(row=5,column=17)


#labeling of entry

l1=Label(top,text="NAME",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l1.grid(row=2,column=0,sticky=W,pady=15)
l3=Label(top,text="PERCENTAGE",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l3.grid(row=3,column=0,sticky=W,pady=15)
l4=Label(top,text="BACK LOG",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l4.grid(row=4,column=0,sticky=W,pady=15)
l5=Label(top,text="INTERNSHIPS",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l5.grid(row=5,column=0,sticky=W,pady=15)

l8=Label(top,text="FIRST ROUND",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l8.grid(row=6,column=0,sticky=W,pady=15)
l9=Label(top,text="COMMUNICATION SKILLLS",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l9.grid(row=7,column=0,sticky=W,pady=15)

l6=Label(top,text="RESULT",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l6.grid(row=2,column=15,sticky=W,pady=15)
l10=Label(top,text="DecisionTree",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l10.grid(row=3,column=15,sticky=W,pady=1)
l11=Label(top,text="RandomForest",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l11.grid(row=4,column=15,sticky=W,pady=1)
l12=Label(top,text="Regression",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l12.grid(row=5,column=15,sticky=W,pady=1)

#Buttom

b1=Button(top,text="DecisionTree", width=16,bg="#134e85",fg="white",bd=4,command=out12)
b1.grid(row=25,column=0,pady=15,rowspan=5)
b2=Button(top,text="RandomForest", width=16,bg="#134e85",fg="white",bd=4,command=out13)
b2.grid(row=25,column=1,pady=15,rowspan=5)
b3=Button(top,text="Regression", width=16,bg="#134e85",fg="white",bd=4,command=out14)
b3.grid(row=25,column=2,pady=15,rowspan=5)
b4=Button(top,text="Clear", width=16,bg="#134e85",fg="white",bd=4,command=clear)
b4.grid(row=24,column=4,pady=15)
b5=Button(top,text="Hire", width=16,bg="#134e85",fg="white",bd=4,command=Hire)
b5.grid(row=5,column=16,pady=15,rowspan=5)
b6=Button(top,text=" Don't Hire", width=16,bg="#134e85",fg="white",bd=4,command=Not_Hire)
b6.grid(row=5,column=15,pady=15,rowspan=5)


top.mainloop()
