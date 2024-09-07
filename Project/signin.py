from tkinter import *
from PIL import ImageTk


# Functionality part
    


def signup_page() :
    login_window.destroy()
    import signup



def user_enter(event) :
    if usernameEntry.get()=="Username" :
        usernameEntry.delete(0,END)


def password_enter(event) :
    if passwordEntry.get()=="Password" :
        passwordEntry.delete(0,END)







# GUT part
login_window=Tk()
login_window.geometry("990x660+50+50")
login_window.resizable(False,False)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file="bg2.jpg")
# ----------------------------for background------------------------------
bgLabel=Label(login_window,image=bgImage)

bgLabel.place(x=0,y=0)

heading=Label(login_window,text="USER LOGIN",font=("Microsoft Yahei UI Light",23,'bold'),bg='white',fg="firebrick1")

heading.place(x=622,y=120)

usernameEntry=Entry(login_window,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=600,y=200)

usernameEntry.insert(0,"Username")

usernameEntry.bind("<FocusIn>",user_enter)
# -------------------------------------------------------------------------------------------------------------------------------
frame1=Frame(login_window,width=250,height=2,bg="firebrick1")
frame1.place(x=600,y=222)

passwordEntry=Entry(login_window,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=600,y=260)

passwordEntry.insert(0,"Pssword")

passwordEntry.bind("<FocusIn>",password_enter)

frame2=Frame(login_window,width=250,height=2,bg="firebrick1")
frame2.place(x=600,y=282)




forfetButton=Button(login_window,text="Forgot Password ?",bd=0,bg='white',activebackground="white",cursor='hand2',font=("Microsoft Yahei UI Light",8,'bold'),fg='firebrick1')
forfetButton.place(x=735,y=300)

loginButton=Button(login_window,text='Login',font=('open sans',15,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor="hand2",bd=0,width=20)
loginButton.place(x=600,y=349)

orLabel=Label(login_window,text='---------------OR---------------',font=("Open Sans",16),fg="firebrick1",bg="white")
orLabel.place(x=600,y=405) 


facebook_logo=PhotoImage(file="facebook.png")
fbLabel=Label(login_window,image=facebook_logo,bg="white")
fbLabel.place(x=630,y=450)



google_logo=PhotoImage(file="google.png")
googleLabel=Label(login_window,image=google_logo,bg="white")
googleLabel.place(x=695,y=450)

twitter_logo=PhotoImage(file="twitter.png")
twitterLabel=Label(login_window,image=twitter_logo,bg="white")
twitterLabel.place(x=760,y=450)

signupLabel=Label(login_window,text="Dont have an account ?",font=("Open Sans",9,'bold'),fg="firebrick1",bg='white')
signupLabel.place(x=590,y=530) 

newaccountButton=Button(login_window,text='Create new one',font=('open sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor="hand2",bd=0,command=signup_page)
newaccountButton.place(x=735,y=529)



login_window.mainloop()