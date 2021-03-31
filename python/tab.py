from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt



root=Tk()
root.geometry("1080x720")

tCR={"Parfait état":"2021-03-15"}
tKM={"1200":"2021-03-15"}
tCons={"10":"2021-03-15"}


treeCR=ttk.Treeview(root)
treeKM=ttk.Treeview(root)
treeCons=ttk.Treeview(root)

treeCons['columns'] = ("Cons","Date")
treeCR['columns'] = ("CR","Date")
treeKM['columns'] = ("KM","Date")

def setTable(dictio,table):
	count=0
	for cle,valeur in dictio.items():
		table.insert(parent='',index='end',iid=count,values=(cle,valeur))
		count +=1


treeCR.column("#0",width=0,stretch=NO)
treeCR.column("CR",anchor=W,width=120)
treeCR.column("Date",anchor=CENTER,width=120)

treeCons.column("#0",width=0,stretch=NO)
treeCons.column("Cons",anchor=W,width=120)
treeCons.column("Date",anchor=CENTER,width=120)

treeKM.column("#0",width=0,stretch=NO)
treeKM.column("KM",anchor=W,width=120)
treeKM.column("Date",anchor=CENTER,width=120)

treeCR.heading("#0",text="Label",anchor=W)
treeCR.heading("CR",text="État courroie",anchor=W)
treeCR.heading("Date",text="Date",anchor=CENTER)

treeKM.heading("#0",text="Label",anchor=W)
treeKM.heading("KM",text="KM",anchor=W)
treeKM.heading("Date",text="Date",anchor=CENTER)

treeCons.heading("#0",text="Label",anchor=W)
treeCons.heading("Cons",text="L/100",anchor=W)
treeCons.heading("Date",text="Date",anchor=CENTER)

setTable(tCR,treeCR)
setTable(tKM,treeKM)
setTable(tCons,treeCons)

treeCR.pack()
treeCons.pack()
treeKM.pack()



root.mainloop()