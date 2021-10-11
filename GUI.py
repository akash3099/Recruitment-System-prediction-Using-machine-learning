from tkinter import *
import tkinter.messagebox as ms
from PIL import ImageTk, Image
from project2 import *


def get_data():
    name1=name.get()
    per1=int(per.get())
    backlog1=int(backlog.get())
    intern1=int(intern.get())
    round1=int(round.get())
    comm1=int(comm.get())
    tree=DecisionTreeClassifier12(per1,backlog1,intern1,round1,comm1)
    forest=randomforest12(per1,backlog1,intern1,round1,comm1)
    
    return (tree,forest)

def out12():
    tree,forest=get_data()
    if tree==1:
     out.set('Hired')
    elif tree==0:
     out.set('Not..Hired..')
     
def out13():
    tree,forest=get_data()
    if forest==1:
     out2.set('Hired')
    elif forest==0:
     out2.set('Not..Hired..')
    

top=Tk()
top.title("RECRUITMENT RESULT")
top.configure(background="#0a2845#")
top.geometry("1000x800")
top.resizable(False, False)

a1=Label(top,text="  Nucleus Computers Ltd.",fg="White",bg="#0a2845#",font="Times 24 bold",bd=15)
a1.grid(row=0,column=0,pady=30,columnspan=10)

path = "Final_Logo.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(top, image = img,fg="White",height=140,width=150)
panel.grid(row=0,column=10,sticky=W,columnspan=10)

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
l6.grid(row=8,column=1,sticky=W,pady=15)
l10=Label(top,text="DecisionTree",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l10.grid(row=9,column=0,sticky=W,pady=1)
l11=Label(top,text="RandomForest",font="times 12 ",bd=8,bg="#0a2845#",fg="white")
l11.grid(row=10,column=0,sticky=W,pady=1)



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


b1=Button(top,text="DecisionTree", width=16,bg="#134e85",fg="white",bd=4,command=out12)
b1.grid(row=3,column=13,columnspan=3,pady=15)
b2=Button(top,text="RandomForest", width=16,bg="#134e85",fg="white",bd=4,command=out13)
b2.grid(row=4,column=13,columnspan=3,pady=15)
c1=Label(top,height=2,width=27,bg="#0a2845#")
c1.grid(row=6,column=13)

out=StringVar()
c1=Label(top,textvariable=out,height=2,width=27,fg="White",bg="#0a2845#",font="Times 14 bold")
c1.grid(row=9,column=1)
out2=StringVar()
c6=Label(top,textvariable=out2,height=2,width=27,fg="White",bg="#0a2845#",font="Times 14 bold")
c6.grid(row=10,column=1)

top.mainloop()
