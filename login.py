from tkinter import *
from tkinter import messagebox
import os
from game import gameregister

def login_success():
    messagebox.showinfo('success', "Login Successful")
    screen2.destroy()
    gameregister()
def password_not_recognised():
    messagebox.showwarning('ALERT', 'INCORRECT PASSWORD.')
def user_not_found():
    messagebox.showwarning('ALERT','USER NOT FOUND!!!')

def register_user():
    """ this function registers an account and save the data in file."""
    a = ''
    if username_entry.get() == a and password_entry.get() == a and password_entry2.get() == a:
        messagebox.showwarning('ALERT', 'PLEASE FILL ALL THE BOXES.')
    elif username_entry.get() == a:
        messagebox.showwarning('ALERT', 'PLEASE FILL THE BOX.')
    elif password_entry.get() == a:
        messagebox.showwarning('ALERT', 'PLEASE WRITE THE PASSWORD.')
    elif password_entry2.get() == a:
        messagebox.showwarning('ALERT', 'PLEASE CONFIRM YOUR PASSWORD TO CONTINUE.')
    elif password_entry.get()  != password_entry2.get() :
        messagebox.showwarning('ALERT', "SORRY !!! PASSWORD DOESNOT MATCH.")

    else :
        username_info = username.get()
        password_info = password.get()
        file = open(username_info, "a+")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        screen1.destroy()
        screen.destroy()

def login_verify():
    """this function verifies the data present in file."""
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()

def register():
    """this function creates the register page."""
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("288x300")
    screen1.iconbitmap('C:/Users/Lenovo/Downloads/bird.ico')
    #image
    global bg5
    bg5=PhotoImage(file="C:/Users/Lenovo/Downloads/regbg.png")
    img_label2=Label(screen1, image=bg5)
    img_label2.place(x=0, y=0)

    id_label= Label(screen1, text="Create Your ID", fg="green", bg='white', font=("calbria", 15, 'bold'))
    id_label.place(x=10, y=5)

    username_label = Label(screen1, bg='white', fg='green', text='Username', font=('calibria', 12, 'bold'))
    username_label.place(x=40, y=50)
    password_label = Label(screen1, bg='white', fg='green', text='Password', font=('calibria', 12, 'bold'))
    password_label.place(x=40, y=120)
    confrimpassword_label = Label(screen1, bg='white', fg='green', text='Confirm Password', font=('calibria', 12, 'bold'))
    confrimpassword_label.place(x=40, y=190)

    global username
    global password
    global username_entry
    global password_entry
    global password_entry2
    username = StringVar()
    password = StringVar()
    confirmpassword = StringVar()

    username_entry= Entry(screen1, textvariable=username, width='30', borderwidth='5')
    username_entry.place(x=40, y=80, height=30)

    password_entry = Entry(screen1, show="*", textvariable=password,width='30', borderwidth='5')
    password_entry.place(x=40, y=150, height=30)

    password_entry2 = Entry(screen1, show="*", textvariable= confirmpassword,width='30', borderwidth='5')
    password_entry2.place(x=40, y=220, height=30)

    register_btn=Button(screen1, text="Register", width=10, height=1, bg='green', fg="white", font=("calbria", 13, 'bold'),command=register_user)
    register_btn.place(x=70, y=260)


def login():
    """this function creates login page."""
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("288x288")
    screen2.iconbitmap('C:/Users/Lenovo/Downloads/bird.ico')
    #image
    global bg3
    bg3 = PhotoImage(file="C:/Users/Lenovo/Downloads/loginbg.png")
    img_label = Label(screen2, image=bg3)
    img_label.place(x=0, y=0)

    user_label = Label(screen2, text="Username", fg='black', bg='white', font=('calibria', 12, 'bold'))
    user_label.place(x=40, y=60)
    pass_label = Label(screen2, text="Password", fg='black', bg='white', font=('calibria', 12, 'bold'))
    pass_label.place(x=40, y=150)

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    username_entry1 = Entry(screen2, textvariable= username_verify, width='30', borderwidth='5')
    username_entry1.place(x=40, y=90, height=30)

    password_entry1 = Entry(screen2, show="*", textvariable=password_verify, width='30', borderwidth='5')
    password_entry1.place(x=40, y=180, height=30)

    login_btn = Button(screen2, text="Login",font=('calibria', 12, 'bold'), bg='white',  width=7, height=2, command=login_verify)
    login_btn.place(x=100, y=220)

def main_screen():
    """this function creates the main-screen."""
    global screen
    screen = Tk()
    screen.geometry('288x512')
    screen.resizable(False, False)
    screen.title('Login')
    screen.iconbitmap('C:/Users/Lenovo/Downloads/bird.ico')
    #image
    global bg
    bg = PhotoImage(file="C:/Users/Lenovo/Downloads/background-night.png")
    label = Label(screen, image=bg)
    label.place(x=0, y=0)

    # textboxes
    login_button = Button(screen,text='LOGIN', height="3", font=('calibria', 12, 'bold'),bg='orange', fg='white', width="10",
                          command=login)
    login_button.place(x=90, y=80)

    register_button = Button(screen, text='REGISTER',font=('calibria', 12, 'bold'), height="3", bg='orange',fg='white', width="10",
                             command=register)
    register_button.place(x=90, y=200)
    screen.mainloop()
main_screen()
