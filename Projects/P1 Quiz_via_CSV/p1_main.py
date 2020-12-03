import tkinter
from tkinter import *
import os
import time
import sqlite3
import csv

i = 1


def store_database(roll_no, password, user_name, whatsapp):
    conn.execute("INSERT INTO project1_registration VALUES(?,?,?,?)", (
        roll_no, password, user_name, whatsapp))
    conn.commit()


def register_check(roll_no, password):

    for row in c.execute('SELECT * FROM project1_registration'):
        if row[0] == roll_no and row[1] == password:
            Quiz(1)
            break
    else:
        label = Label(
            root,
            text="Please register before logging in",
            font=("Helevetica", 18, "bold"),
            background="#ffffff",)
        label.pack(pady=(50, 0))


def Register():

    label_register_r = Label(
        root,
        text="Register",
        font=("Helevetica", 18, "bold"),
        background="#ffffff",)
    label_register_r.pack(pady=(50, 0))

    label_user_name = Label(
        root,
        text="User Name",
        font=("Helevetica", 18, "bold"),
        background="#ffffff",)
    label_user_name.pack()

    entry_user_name = Entry()
    entry_user_name.pack()

    label_roll_no = Label(
        root,
        text="Roll No.",
        font=("Helevetica", 18, "bold"),
        background="#ffffff",)
    label_roll_no.pack()

    entry_roll_no = Entry()
    entry_roll_no.pack()

    label_password = Label(
        root,
        text="Password",
        font=("Helevetica", 18, "bold"),
        background="#ffffff",
    )
    label_password.pack()

    entry_password = Entry()
    entry_password.pack()

    label_whatsapp = Label(
        root,
        text="Whatsapp",
        font=("Helevetica", 18, "bold"),
        background="#ffffff",
    )
    label_whatsapp.pack()

    entry_whatsapp = Entry()
    entry_whatsapp.pack()

    btnEnter = Button(
        root,
        text='Enter',
        font=("Helevetica", 18, "bold"),
        relief=FLAT,
        border=0,
        command=lambda: EnterRegister(
            entry_roll_no, entry_password, entry_user_name, entry_whatsapp)
    )
    btnEnter.pack()

    root.mainloop()

# quiz paper####################################


def Quiz(quiz_number):

    with open('q'+str(quiz_number)+'.csv', 'r') as q:
        reader = csv.reader(q)
        global i
        j = 0
        for row in reader:

            if j == i:
                print(i)
                var = StringVar()
                labelQuestion = Label(
                    root,

                    textvariable=var,  # "Sample is back",
                    font=("Consolas", 16),
                    width=500,
                    justify="center",
                    wraplength=400,
                    background="#fBBfff",
                )
                var.set(row[1])
                labelQuestion.pack(pady=(10, 30))

                radiovar = IntVar()
                radiovar.set(-1)
                var1 = StringVar()
                r1 = Radiobutton(
                    root,
                    textvariable=var1,
                    font=("Times", 12),
                    value=0,
                    variable=radiovar,
                    # command = selected,
                    background="#ffffff",
                )
                var1.set(row[2])
                r1.pack(pady=5)

                var2 = StringVar()
                r2 = Radiobutton(
                    root,
                    textvariable=var2,
                    font=("Times", 12),
                    value=1,
                    variable=radiovar,
                    background="#ffffff",
                )
                var2.set(row[3])
                r2.pack(pady=5)

                var3 = StringVar()
                r3 = Radiobutton(
                    root,
                    textvariable=var3,
                    font=("Times", 12),
                    value=2,
                    variable=radiovar,
                    # command = selected,
                    background="#ffffff",
                )
                var3.set(row[4])
                r3.pack(pady=5)

                var4 = StringVar()
                r4 = Radiobutton(
                    root,
                    textvariable=var4,
                    font=("Times", 12),
                    value=3,
                    variable=radiovar,
                    # command = selected,
                    background="#ffffff",
                )
                var4.set(row[5])
                r4.pack(pady=5)

                btnNext = Button(
                    root,
                    text='Next',
                    font=("Helevetica", 18, "bold"),
                    relief=FLAT,
                    background="#CBBBB8",
                    border=0,
                    command=lambda: nextpressed()
                )

                btnNext.pack()
            j += 1
            if j > i:
                break


def nextpressed():
    # labelQuestion.pack_forget()
    # r1.pack()
    # r2.pack()
    # r3.pack()
    # r4.pack()
    global i
    i += 1
    Quiz(1)


##############################################


def ButtonisPressed(var):
    label_quiz.pack_forget()
    label_login.pack_forget()
    label_password.pack_forget()
    label_register.pack_forget()
    label_roll_no.pack_forget()
    entry_roll_no.pack_forget()
    entry_password.pack_forget()
    btnEnter.pack_forget()
    btnRegister.pack_forget()

    if var == 1:
        register_check(roll_no, password)
    elif var == 2:
        Register()


def EnterLogin():
    global roll_no, password
    roll_no = entry_roll_no.get()
    password = entry_password.get()

    ButtonisPressed(1)


def EnterRegister(entry_roll_no, entry_password, entry_user_name, entry_whatsapp):
    global roll_no, password, user_name, whatsapp
    roll_no = entry_roll_no.get()
    password = entry_password.get()
    user_name = entry_user_name.get()
    whatsapp = entry_whatsapp.get()
    store_database(roll_no, password, user_name, whatsapp)


os.chdir(os.path.dirname(os.path.realpath(__file__)))
conn = sqlite3.connect("project1_quiz_cs384.db")


c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS project1_registration(
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    whatsapp INT NOT NULL
);""")
conn.commit()

root = tkinter.Tk()
root.title("Quiz")
root.geometry("700x600")
root.config(background="#fffff5")
root.resizable(0, 0)

label_quiz = Label(
    root,
    text="Quiz Portal",
    font=("Helevetica", 24, "bold"),
    background="#ffffff",
)
label_quiz.pack(pady=(0, 50))

# front page
label_login = Label(
    root,
    text="Login",
    font=("Helevetica", 18, "bold"),
    background="#ffffff",
)
label_login.pack(pady=(25, 10))

label_roll_no = Label(
    root,
    text="Roll No.",
    font=("Helevetica", 18, "bold"),
    background="#ffffff",
)
label_roll_no.pack()

entry_roll_no = Entry(root)
entry_roll_no.pack()
label_password = Label(
    root,
    text="Password",
    font=("Helevetica", 18, "bold"),
    background="#ffffff",
)
label_password.pack()

entry_password = Entry(root)
entry_password.pack()

# front page enter button
btnEnter = Button(
    root,
    text='Enter',
    font=("Helevetica", 18, "bold"),
    relief=FLAT,
    border=0,
    command=lambda: EnterLogin(),
)
btnEnter.pack()


# front page register button
label_register = Label(
    root,
    text="Not Registered?",
    font=("Helevetica", 18, "bold"),
    background="#ffffff",)
label_register.pack(pady=(50, 0))

btnRegister = Button(
    root,
    text='Register',
    font=("Helevetica", 18, "bold"),
    relief=FLAT,
    background="#CBBBB8",
    border=0,
    command=lambda: ButtonisPressed(2)
)
btnRegister.pack()
root.mainloop()
