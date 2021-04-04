import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import read_transaction
import showdb





class Frames(object):
	def __init__(self):
		pass

	def main_frame(self,root):
		root.title("CarRegistration")
		root.geometry("300x100")
		self.query = StringVar()
		self.label= Label(root,text="Entrez votre VIN")
		self.entry = Entry(root,textvariable=self.query)
		self.button = Button(root,text="OK", command=self.get_info)
		self.label.pack()
		self.entry.pack()
		self.button.pack()

	def get_info(self):
		uid = showdb.get_uid(self.query.get())
		print(uid)
		if uid == "error":
			messagebox.showinfo("Erreur", "Code introuvable")
		else:
			self.response = read_transaction.get_dicts(uid)
			print(self.response)
			self.info_frame()
			
	def info_frame(self):
		info = Toplevel()
		info.title("Info")
		info.geometry("1600x1080")
		treeCR=ttk.Treeview(info)
		treeKM=ttk.Treeview(info)
		treeCons=ttk.Treeview(info)
		treeCons['columns'] = ("Cons","Date")
		treeCR['columns'] = ("CR","Date")
		treeKM['columns'] = ("KM","Date")
		treeCR.column("#0",width=0,stretch=NO)
		treeCR.column("CR",anchor=W,width=120)
		treeCR.column("Date",anchor=CENTER,width=300)
		treeCons.column("#0",width=0,stretch=NO)
		treeCons.column("Cons",anchor=W,width=120)
		treeCons.column("Date",anchor=CENTER,width=300)
		treeKM.column("#0",width=0,stretch=NO)
		treeKM.column("KM",anchor=W,width=120)
		treeKM.column("Date",anchor=CENTER,width=300)
		treeCR.heading("#0",text="Label",anchor=W)
		treeCR.heading("CR",text="État courroie",anchor=W)
		treeCR.heading("Date",text="Date",anchor=CENTER)
		treeKM.heading("#0",text="Label",anchor=W)
		treeKM.heading("KM",text="KM",anchor=W)
		treeKM.heading("Date",text="Date",anchor=CENTER)
		treeCons.heading("#0",text="Label",anchor=W)
		treeCons.heading("Cons",text="L/100",anchor=W)
		treeCons.heading("Date",text="Date",anchor=CENTER)
		self.setTable(self.response["km"],treeKM)
		self.setTable(self.response["usure"],treeCR)
		self.setTable(self.response["conso"],treeCons)
		treeCR.pack()
		treeCons.pack()
		treeKM.pack()
		Button(info,text="Close",command=info.destroy).pack()

	def setTable(self,dictio,table):
		count=0
		for valeur,cle in dictio.items():
			table.insert(parent='',index='end',iid=count,values=(cle,datetime.utcfromtimestamp(valeur).strftime('%Y-%m-%d %H:%M:%S')))   #Timestamp value is returned in seconds so need to be parsed
			count +=1


root = Tk()
app = Frames ()
app.main_frame(root)
root.mainloop()
