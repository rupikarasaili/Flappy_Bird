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
