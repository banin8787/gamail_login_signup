# from tkinter import*
# from PIL import ImageTk
# from tkinter import messagebox

# def Login_page():
#     signup_window.destroy()
#     import signin






# signup_window=Tk()
# signup_window.title('Sginup Paga')
# signup_window.resizable(False,False)


# background=ImageTk.PhotoImage(file='bg2.jpg')

# bgLabel=Label(signup_window,image=background)
# bgLabel.grid()

# Frame=Frame(signup_window,bg='white')
# Frame.place(x=574,y=92)

# heading=Label(Frame,text="CREATE AN ACCOUNT",font=("Microsoft Yahei UI Light",18,'bold'),bg='white',fg="firebrick1")
# heading.grid(row=0,column=0,padx=10,pady=10)


# emailLabel=Label(Frame,text="Email",font=("Microsoft Yahei UI Light",10,'bold'),bg='white',fg='firebrick1')
# emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

# emailEntry=Entry(Frame,width=30,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
# emailEntry.grid(row=2,column=0,sticky='w',padx=25)


# usernameLabel=Label(Frame,text="Username",font=("Microsoft Yahei UI Light",10,'bold'),bg='white',fg='firebrick1')
# usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

# usernameEntry=Entry(Frame,width=30,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
# usernameEntry.grid(row=4,column=0,sticky='w',padx=25)


# passwordLabel=Label(Frame,text="Password",font=("Microsoft Yahei UI Light",10,'bold'),bg='white',fg='firebrick1')
# passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

# passwordEntry=Entry(Frame,width=30,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
# passwordEntry.grid(row=6,column=0,sticky='w',padx=25)


# confirmLabel=Label(Frame,text=" Confirm Password",font=("Microsoft Yahei UI Light",10,'bold'),bg='white',fg='firebrick1')
# confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

# confirmEntry=Entry(Frame,width=30,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
# confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

# check=IntVar()
# termsandconditions=Checkbutton(Frame,text='I Agree to the Terms & Conditions',font=("Microsoft Yahei UI Light",9,'bold'),fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor="hand2",variable=check)
# termsandconditions.grid(row=9,column=0,pady=10,padx=13)

# signupButton=Button(Frame,text='Signup',font=("Open Sans",16,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=17)
# signupButton.grid(row=10,column=0,pady=11)

# alreadyaccount=Label(Frame,text='Dont have an account?',font=('Open Sans',9,'bold'),bg='white',fg='firebrick1')
# alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)



# logintButton=Button(signup_window,text='Log in',font=('open sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=Login_page)

# logintButton.place(x=740,y=504)


# signup_window.mainloop()







