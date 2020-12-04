import tkinter
from tkinter import *
import os
import re
import pandas as pd
import sqlite3
import hashlib
import tkinter.messagebox as tkMessageBox
from tkinter import simpledialog


# Function to store the filled in registeration info to the database table project1_registration -


def store_database(roll_no, password, user_name, whatsapp):

    temp = hashlib.sha224(password.encode())
    password_hash = temp.hexdigest()

    conn.execute("INSERT INTO project1_registration VALUES(?,?,?,?)", (
        roll_no, password_hash, user_name, whatsapp))
    conn.commit()
    next_window_registration(1)

# Function to show the user the login page -


def Login():
    global label_quiz, label_register, label_password, label_login, label_roll_no, entry_password, entry_roll_no, btnRegister, btnEnter

    os.chdir(os.path.join(os.getcwd(), 'quiz_wise_questions'))

    label_quiz = Label(
        root,
        text="Quiz Portal",
        font=("Helevetica", 30, "bold"),
        background="#ffffff",
        fg="blue",
    )
    label_quiz.pack(pady=(0, 50))

    label_login = Label(
        root,
        text="Login",
        font=("Helevetica", 24, "bold"),
        fg='red',
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

    btnEnter = Button(
        root,
        text='Enter',
        font=("Helevetica", 18, "bold"),
        relief=FLAT,
        border=0,
        command=lambda: EnterLogin(),
    )
    btnEnter.pack()

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
        command=lambda: next_window(2)
    )
    btnRegister.pack()

# Function to show the user the registration page -


def Register():

    global label_register_2, label_user_name, label_whatsapp, entry_user_name, entry_whatsapp, btnEnter_2, btnEnter, btnLogin

    label_register_2 = Label(
        root,
        text="Register",
        font=("Helevetica", 24, "bold"),
        fg="blue",
        background="#ffffff",)
    label_register_2.pack(pady=(50, 0))

    label_user_name = Label(
        root,
        text="User Name",
        font=("Helevetica", 18, "bold"),
        background="#ffffff",)
    label_user_name.pack()

    entry_user_name = Entry()
    entry_user_name.pack()

    label_roll_no.pack()
    entry_roll_no.pack()

    label_password.pack()
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

    btnEnter_2 = Button(
        root,
        text='Enter',
        font=("Helevetica", 18, "bold"),
        relief=FLAT,
        border=0,
        command=lambda: EnterRegister(
            entry_roll_no, entry_password, entry_user_name, entry_whatsapp)
    )
    btnEnter_2.pack()

    btnLogin = Button(
        root,
        text='Login',
        font=("Helevetica", 18, "bold"),
        relief=FLAT,
        border=0,
        command=lambda: next_window_registration(1)
    )
    btnLogin.pack(pady=(50, 0))


# Function to check if the login details(Roll no and Password) are registered in database -
def register_check(roll_no, password):

    global label_check, btnReturn, user_name

    temp = hashlib.sha224(password.encode())
    password_hash = temp.hexdigest()

    for row in c.execute('SELECT * FROM project1_registration'):
        if row[0] == roll_no and row[1] == password_hash:
            user_name = row[2]
            quiz_select()
            break
    else:
        label_check = Label(
            root,
            text="Please register before logging in",
            font=("Helevetica", 18, "bold"),
            background="#ffffff",)
        label_check.pack(pady=(50, 0))
        btnReturn = Button(
            root,
            text='Return',
            font=("Helevetica", 18, "bold"),
            relief=FLAT,
            command=lambda: next_window_registration(0)
        )
        btnReturn.pack(pady=(50, 0))


# Function to select the Quiz user wants to give -
def quiz_select():

    global label_text,  btn1, btn2, btn3
    label_text = Label(
        root,
        text="Please Select which quiz you want to give: ",
        font=("Helevetica", 18, "bold"),
        background="#ffffff",)
    label_text.pack()

    btn1 = Button(
        root,
        text='Quiz 1',
        font=("Helevetica", 18, "bold"),
        relief=FLAT,
        border=0,
        command=lambda: quiz_unpack(1),
    )
    btn1.pack(pady=20)

    btn2 = Button(
        root,
        text='Quiz 2',
        font=("Helevetica", 18, "bold"),
        relief=FLAT,
        border=0,
        command=lambda: quiz_unpack(2),
    )
    btn2.pack(pady=20)

    btn3 = Button(
        root,
        text='Quiz 3',
        font=("Helevetica", 18, "bold"),
        relief=FLAT,
        border=0,
        command=lambda: quiz_unpack(3),
    )
    btn3.pack(pady=20)


# Function to show the next question to the user -
def next_question(quiz_number, index):
    global quiz_df, radiovar, btnSubmit

    if index < quiz_df.shape[0] - 1 and (quiz_df.loc[index, 'compulsory'] == 'n' or radiovar.get() in [1, 2, 3, 4]):
        index += 1
        labelQuestion.pack_forget()
        r1.pack_forget()
        r2.pack_forget()
        r3.pack_forget()
        r4.pack_forget()
        btnNext.pack_forget()
        btnSubmit.pack_forget()
        labeldisc.pack_forget()
        btnSkip.pack_forget()
        Quiz(quiz_number, index)

    else:
        pass


# Function to find total marks, marked choice, attempted questions, etc
def calc(index):

    global marks, quiz_df, radiovar, attempted, correct, marked_choice, total, btnNext, ques_done

    if index < quiz_df.shape[0] and (quiz_df.loc[index, 'compulsory'] == 'n' or radiovar.get() in [1, 2, 3, 4]):

        individual_df.loc[index, 'marked_choice'] = radiovar.get()

        if radiovar.get() == quiz_df.loc[index, 'correct_option']:
            marks.append(quiz_df.loc[index, 'marks_correct_ans'])
            attempted.append(1)
            correct.append(1)
            marked_choice.append(radiovar.get())
            total.append(2)
            ques_done.append(index)
            individual_df.loc[index, 'Total'] = 2

        elif radiovar.get() in [1, 2, 3, 4]:
            marks.append(quiz_df.loc[index, 'marks_wrong_ans'])
            attempted.append(1)
            marked_choice.append(radiovar.get())
            total.append(1)
            ques_done.append(index)
            individual_df.loc[index, 'Total'] = 1

    if index == quiz_df.shape[0] - 1:
        btnNext.configure(state=DISABLED)

    radiovar.set(-1)


# Function for a countdown timer which takes seconds as input
def countdown(t):
    global label_timer, submitted
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    label_timer['text'] = 'Time: ' + timer

    if t > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, t-1)
    else:
        if submitted != 1:
            submit()


# Function to submit the quiz results
def submit():
    global quiz_df, marks, quiz_no, submitted, correct, attempted
    submitted = 1

    labelQuestion.pack_forget()
    r1.pack_forget()
    r2.pack_forget()
    r3.pack_forget()
    r4.pack_forget()
    btnNext.pack_forget()
    labeldisc.pack_forget()
    btnSkip.pack_forget()
    btnSubmit.pack_forget()
    label_timer.pack_forget()

    total_marks = int(sum(marks))
    total_attempted = int(sum(attempted))
    total_correct = int(sum(correct))
    total_wrong = total_attempted - total_correct

    labelSubmit = Label(
        root,
        anchor='w',
        text=f'''
                Total Quiz Questions: {quiz_df.shape[0]}\n
                Total Quiz Questions Attempted:{total_attempted}\n
                Total Correct Question:{total_correct}\n
                Total Wrong Questions:{total_wrong }\n
                Total Marks: {total_marks}/{quiz_df['marks_correct_ans'].sum()}\n 
                    ''',
        font=("Consolas", 16),
        width=100,
        justify=LEFT,
        background="#BBffff",
    )
    labelSubmit.pack(pady=100)

    for row in c.execute('SELECT * FROM project1_marks'):
        if row[0] == roll_no and row[1] == quiz_no:
            conn.execute(
                "DELETE FROM project1_marks WHERE roll = ? AND quiz_num = ?", (roll_no, quiz_no))
            conn.execute("INSERT INTO project1_marks VALUES(?,?,?);",
                         (roll_no, quiz_no, total_marks))
            break
    else:
        conn.execute("INSERT INTO project1_marks VALUES(?,?,?);",
                     (roll_no, quiz_no, total_marks))

    conn.commit()
    export_to_csv()


# Function to convert Total column to Legend column in individual_df
def legend_func(x):
    if x == 1:
        return "Wrong Choice"
    elif x == 2:
        return "Correct Choice"
    elif x == 0:
        return "Unattempted"


# Function to export the result of the quiz just given
def export_to_csv():
    global quiz_df, marked_choice, total, quiz_no, roll_no, marks, individual_df

    os.chdir(os.path.split(os.getcwd())[0])
    os.chdir(os.path.join(os.getcwd(), 'individual_responses'))

    marked_choice += [0]*(quiz_df.shape[0] - len(marked_choice))
    total += [0]*(quiz_df.shape[0] - len(total))

    individual_df = individual_df.fillna(0)

    individual_df['marked_choice'] = individual_df['marked_choice'].astype(int)
    individual_df['Total'] = individual_df['Total'].astype(int)

    individual_df['Legend'] = individual_df['Total'].apply(legend_func)

    total_df = pd.DataFrame(columns=individual_df.columns)
    list_total = [sum(marks), quiz_df['marks_correct_ans'].sum()]
    list_legend = ['Marks Obtained', 'Total Quiz Marks']

    total_df['Total'] = list_total
    total_df['Legend'] = list_legend

    final_df = individual_df.append(total_df)

    with open('q' + str(quiz_no) + '_' + roll_no + '.csv', 'w', newline='') as f:
        final_df.to_csv(f, index=False)


# Function to display the questions one by one
def Quiz(quiz_number, index):

    global labelQuestion, r1, r2, r3, r4, btnNext, labeldisc, label_timer, quiz_df, btnSubmit, btnSkip
    compulsory_dict = {
        'y': 'Yes',
        'n': 'No'
    }
    var = StringVar()

    labelQuestion = Label(
        root,
        anchor='w',
        textvariable=var,
        font=("Consolas", 16),
        width=700,
        justify="left",
        wraplength=700,
        background="#71AAEE",
    )
    var.set('Q' + str(index + 1) + ". " + quiz_df.loc[index, 'question'])
    labelQuestion.pack(pady=(0, 20))

    var1 = StringVar()

    r1 = Radiobutton(
        root,
        textvariable=var1,
        anchor='w',
        font=("Times", 12),
        value=1,
        width=30,
        variable=radiovar,
        justify='left',
        background="#ffffff",
    )
    var1.set(quiz_df.loc[index, 'option1'])
    r1.pack(pady=5)

    var2 = StringVar()
    r2 = Radiobutton(
        root,
        textvariable=var2,
        anchor='w',
        font=("Times", 12),
        value=2,
        variable=radiovar,
        justify='left',
        width=30,
        background="#ffffff",
    )
    var2.set(quiz_df.loc[index, 'option2'])
    r2.pack(pady=5)

    var3 = StringVar()
    r3 = Radiobutton(
        root,
        textvariable=var3,
        anchor='w',
        font=("Times", 12),
        value=3,
        variable=radiovar,
        justify='left',
        width=30,
        background="#ffffff",
    )
    var3.set(quiz_df.loc[index, 'option3'])
    r3.pack(pady=5)

    var4 = StringVar()
    r4 = Radiobutton(
        root,
        textvariable=var4,
        anchor='w',
        font=("Times", 12),
        value=4,
        justify='left',
        width=30,
        variable=radiovar,
        background="#ffffff",
    )
    var4.set(quiz_df.loc[index, 'option4'])
    r4.pack(pady=5)

    if index in ques_done:
        btnNext.configure(state=DISABLED)
    else:
        btnNext = Button(
            root,
            text='Enter Answer',
            font=("Helevetica", 18, "bold"),
            width=15,
            relief=FLAT,
            background="#CBBBB8",
            border=0,
            command=lambda: [next_question(quiz_number, index), calc(index)]
        )
        btnNext.pack(pady=(10, 10))

    btnSkip = Button(
        root,
        text='Skip',
        font=("Helevetica", 18, "bold"),
        width=15,
        relief=FLAT,
        background="#CBBBB8",
        border=0,
        command=lambda: skip(index)
    )
    btnSkip.pack()

    labeldisc = Label(
        root,
        anchor='w',
        text=f'''
            Credits if Correct Option: {quiz_df.loc[index,'marks_correct_ans']}
            Negative Marking: {quiz_df.loc[index,'marks_wrong_ans']}
            Compulsory: {compulsory_dict[quiz_df.loc[index,'compulsory']]}
                ''',
        font=("Consolas", 16),
        width=500,
        justify=LEFT,
        background="#ffffff",
    )
    labeldisc.pack()

    btnSubmit = Button(
        root,
        text='Submit',
        font=("Helevetica", 18, "bold"),
        relief=FLAT,
        width=15,
        background="#CBBBB8",
        border=0,
        command=submit
    )
    btnSubmit.pack(pady=5)


# Function for changing Quiz select page to the Quiz page
def quiz_unpack(var):
    global total, marks, correct, attempted, radiovar, label_timer, quiz_df, quiz_no, submitted, marked_choice, ques_done, individual_df
    radiovar = IntVar()
    marks = []
    attempted = []
    correct = []
    marked_choice = []
    total = []
    ques_done = []
    index = 0
    submitted = 0
    quiz_no = var

    btn1.pack_forget()
    btn2.pack_forget()
    btn3.pack_forget()
    label_text.pack_forget()

    quiz_df = pd.read_csv('q' + str(var)+'.csv')

    t = int(re.findall(r'\d+', quiz_df.columns[-1])[0])
    t = t*60

    individual_df = quiz_df.copy()
    individual_df.drop(individual_df.columns[len(
        individual_df.columns)-1], inplace=True, axis=1)

    label_timer = Label(root,
                        font=("Consolas", 16),
                        width=50,
                        justify=LEFT,
                        background="#ffffff",)
    label_timer.pack()
    countdown(t)

    label_info = Label(
        root,
        anchor='w',
        text=f'Roll: {roll_no}\nName: {user_name}',
        font=("Times", 18),
        justify='left',
        width=500,
        background="#13F38F",
    )
    label_info.pack()
    Quiz(var, index)


# Function for changing the Registration page to the Login page
def next_window_registration(var):
    if var == 1:
        label_register_2.pack_forget()
        label_user_name.pack_forget()
        label_whatsapp.pack_forget()
        label_roll_no.pack_forget()
        label_password.pack_forget()
        entry_user_name.pack_forget()
        entry_whatsapp.pack_forget()
        entry_roll_no.pack_forget()
        entry_password.pack_forget()
        btnEnter_2.pack_forget()
        btnLogin.pack_forget()
    else:
        label_check.pack_forget()
        btnReturn.pack_forget()

    label_quiz.pack(pady=(0, 50))
    label_login.pack(pady=(25, 10))
    label_roll_no.pack()
    entry_roll_no.pack()
    label_password.pack()
    entry_password.pack()
    btnEnter.pack()
    label_register.pack(pady=(50, 0))
    btnRegister.pack()

# Function for changing the Login page to the Quiz select page


def next_window(var):
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

# Function for taking the login values after 'Enter' button is pressed


def EnterLogin():
    global roll_no, password
    roll_no = entry_roll_no.get()
    password = entry_password.get()

    next_window(1)

# Function for taking the Registration values after 'Enter' button is pressed


def EnterRegister(entry_roll_no, entry_password, entry_user_name, entry_whatsapp):
    global roll_no, password, user_name, whatsapp
    roll_no = entry_roll_no.get()
    password = entry_password.get()
    user_name = entry_user_name.get()
    whatsapp = entry_whatsapp.get()
    store_database(roll_no, password, user_name, whatsapp)


# Function to display unattempted questions in a messagebox
def unattempted_ask(event):
    global attempted, quiz_df, ques_done

    unattempted = quiz_df.shape[0] - int(sum(attempted))

    all_ques_done = [x+1 for x in ques_done]
    all_ques = [x for x in range(1, quiz_df.shape[0]+1)]

    unattempted_ques = set(all_ques) - set(all_ques_done)

    if len(unattempted_ques) != 0:
        tkMessageBox.showinfo(
            "Unattempted", f"Total unattempted Questions: {unattempted}\nUnattempted Question No. : {unattempted_ques}")
    else:
        tkMessageBox.showinfo(
            "Unattempted", f"Total unattempted Questions: {unattempted}\nAll Questions Attempted")

# Function to display a query regarding submission to the user and submitting if they press 'Yes'


def submit_ask(event):
    MsgBox = tkMessageBox.askquestion(
        'Submit', 'Do you want to final submit?', icon='warning')
    if MsgBox == 'yes':
        submit()
    else:
        pass

# Function to export the database in table project1_marks to csv files quiz wise


def export_ask(event):

    MsgBox = tkMessageBox.askquestion(
        'Export', 'Do you want to export to csv?', icon='info')
    if MsgBox == 'yes':

        marksrecord_df = pd.read_sql_query(
            "SELECT * FROM project1_marks", conn)

        for i in range(1, 4):

            quizrecord_df = marksrecord_df[marksrecord_df['quiz_num'] == i].copy(
            )
            quizrecord_df.columns = ['Roll_No', 'quiz_num', 'Total_marks']

            del quizrecord_df['quiz_num']

            quizrecord_df = quizrecord_df.reindex(
                columns=['Name', 'Whatsapp'] + quizrecord_df.columns.tolist())
            quizrecord_df.reset_index(inplace=True)
            del quizrecord_df['index']

            for roll, k in zip(quizrecord_df['Roll_No'], range(0, quizrecord_df.shape[0])):
                for row in c.execute('SELECT * FROM project1_registration'):
                    if row[0] == roll:
                        quizrecord_df.loc[k, 'Name'] = row[2]
                        quizrecord_df.loc[k, 'Whatsapp'] = row[3]
            quizrecord_df = quizrecord_df.fillna(0)
            quizrecord_df['Whatsapp'] = quizrecord_df['Whatsapp'].astype(int)

            os.chdir(os.path.split(os.getcwd())[0])
            os.chdir(os.path.join(os.getcwd(), 'quiz_wise_responses'))

            with open('quiz' + str(i) + '.csv', 'w', newline='') as f:
                quizrecord_df.to_csv(f, index=False)

    else:
        pass


# Function to skip the current question
def skip(index):

    if index < quiz_df.shape[0]-1 and quiz_df.loc[index, 'compulsory'] == 'n':
        index += 1
        labelQuestion.pack_forget()
        r1.pack_forget()
        r2.pack_forget()
        r3.pack_forget()
        r4.pack_forget()
        btnNext.pack_forget()
        btnSubmit.pack_forget()
        labeldisc.pack_forget()
        btnSkip.pack_forget()
        Quiz(quiz_no, index)

    else:
        pass


# Function to go to user inputted question
def goto_ask(event):
    global quiz_no
    ques_no = int(simpledialog.askstring(
        title="Goto", prompt="Go to question no.: "))

    if ques_no <= quiz_df.shape[0]:
        labelQuestion.pack_forget()
        r1.pack_forget()
        r2.pack_forget()
        r3.pack_forget()
        r4.pack_forget()
        btnNext.pack_forget()
        btnSubmit.pack_forget()
        labeldisc.pack_forget()
        btnSkip.pack_forget()
        Quiz(quiz_no, ques_no-1)

    else:
        pass


os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Creating the database -
conn = sqlite3.connect("project1_quiz_cs384.db")

c = conn.cursor()

# Creating the table project1_registration -
c.execute("""CREATE TABLE IF NOT EXISTS project1_registration(
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    whatsapp TEXT NOT NULL
);""")
conn.commit()

# Creating the table project1_marks -
c.execute("""CREATE TABLE IF NOT EXISTS project1_marks(
    roll TEXT NOT NULL,
    quiz_num INT NOT NULL,
    total_marks INT NOT NULL
);""")

conn.commit()

root = tkinter.Tk()
root.title("Quiz")
root.geometry("800x700")
root.config(background="#FFFFFF")
root.resizable(0, 0)

root.bind("<Control-Alt-u>", unattempted_ask)
root.bind("<Control-Alt-f>", submit_ask)
root.bind("<Control-Alt-e>", export_ask)
root.bind("<Control-Alt-g>", goto_ask)

Login()

root.mainloop()
