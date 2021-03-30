from tkinter import *
window = Tk()


window.title("Ma voiture")
window.geometry("1080x720")


#label.pack(expand=YES)
frame=Frame(window, bd=1,relief=SUNKEN)
label = Label(frame,text="Entrez votre code voiture")
label.pack()
idv_entry = Entry(frame,fg='white')
idv_entry.pack()
ok_button = Button(frame, text="Ok")
ok_button.pack()

frame.pack(expand=YES)


window.mainloop()