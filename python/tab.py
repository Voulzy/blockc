from tkinter import *


root=Tk()

root.geometry("1080x720")

VID=Label(root,width=10,text="VID")
VID.grid(row=0,column=2,padx=20)

CR=Label(root,width=10,text="CR")
CR.grid(row=0,column=3,padx=20)

KM=Label(root,width=10,text="KM")
KM.grid(row=0,column=4,padx=20)

Cons=Label(root,width=10,text="Cons")
Cons.grid(row=0,column=5,padx=20)

TS=Label(root,width=10,text="Timestamp")
TS.grid(row=0,column=1,padx=20)

root.mainloop()