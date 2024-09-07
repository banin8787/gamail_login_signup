from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("login")
root.resizable(False,False)
lblName = Label(root,text="enter your name : ")
lblName.place(x=50 , y= 100)
strName = StringVar()
entryName = Entry(root,textvariable=strName)
entryName.place(x= 150 , y= 102)





root.mainloop()