import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk
from tkinter import font, colorchooser
import os.path
import datetime
import time


class Notepad:

    root = Tk()

    # default window width and height
    thisWidth = 300
    thisHeight = 300
    thisTextArea = Text(root)  # mane je ta likha hochhe
    thisMenuBar = Menu(root)
    thisFileMenu = Menu(thisMenuBar, tearoff=0)
    thisEditMenu = Menu(thisMenuBar, tearoff=0)
    thisHelpMenu = Menu(thisMenuBar, tearoff=0)
    thisStatsMenu = Menu(thisMenuBar, tearoff=0)
    thisFormatMenu = Menu(thisMenuBar, tearoff=0)
    # To add scrollbar
    thisScrollBar = Scrollbar(thisTextArea)
    file = None

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size (the default is 300x300)

        try:
            self.thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.root.title("Untitled - Notepad")

        # Center the window
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.thisHeight / 2)

        # For top and bottom
        self.root.geometry('%dx%d+%d+%d' % (self.thisWidth,
                                            self.thisHeight,
                                            left, top))

        # To make the textarea auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.thisTextArea.grid(sticky=N + E + S + W)

        # To open new file
        self.thisFileMenu.add_command(label="New",
                                      command=self.newFile)

        # To open a already existing file
        self.thisFileMenu.add_command(label="Open",
                                      command=self.openFile)

        # To save current file
        self.thisFileMenu.add_command(label="Save",
                                      command=self.saveFile)

        ##############################
        self.thisFileMenu.add_command(label="Save as",
                                      command=self.saveASFile)

        # To create a line in the dialog
        self.thisFileMenu.add_separator()
        self.thisFileMenu.add_command(label="Exit",
                                      command=self.quitApplication)
        self.thisMenuBar.add_cascade(label="File",
                                     menu=self.thisFileMenu)

        # To give a feature of cut
        self.thisEditMenu.add_command(label="Cut",
                                      command=self.cut)

        # to give a feature of copy
        self.thisEditMenu.add_command(label="Copy",
                                      command=self.copy)

        # To give a feature of paste
        self.thisEditMenu.add_command(label="Paste",
                                      command=self.paste)
        self.thisEditMenu.add_command(label="Find/Replace",
                                      command=self.find)
        # To give a feature of editing
        self.thisMenuBar.add_cascade(label="Edit",
                                     menu=self.thisEditMenu)

        #######stats###########################
        self.thisStatsMenu.add_command(label="Word Count",
                                       command=self.totalword)
        self.thisStatsMenu.add_command(label="Character Count",
                                       command=self.totalcharacter)
        self.thisStatsMenu.add_command(label="Created time",
                                       command=self.createdTime)
        self.thisStatsMenu.add_command(label="Modified time",
                                       command=self.modifiedTime)
        self.thisMenuBar.add_cascade(label="Stats",
                                     menu=self.thisStatsMenu)
        ################FORMAT##########################
        self.thisFormatMenu.add_command(label="Bold",
                                        command=self.bold)
        self.thisFormatMenu.add_command(label="Font/Size",
                                        command=self.font)
        self.thisMenuBar.add_cascade(label="Format",
                                     menu=self.thisFormatMenu)

        # To create a feature of description of the notepad
        self.thisHelpMenu.add_command(label="About Notepad",
                                      command=self.showAbout)
        self.thisMenuBar.add_cascade(label="Help",
                                     menu=self.thisHelpMenu)

        ##########################################
        self.root.config(menu=self.thisMenuBar)

        self.thisScrollBar.pack(side=RIGHT, fill=Y)
        ######TOOLBAR LABEL###############
        # tool_bar = tkinter.Label(self.root)
        # tool_bar.pack()
        # Scrollbar will adjust automatically according to the content
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)

    def quitApplication(self):
        self.root.destroy()
        # exit()

    def showAbout(self):
        showinfo("FEATURE ADDED BY", "SAIKAT AND KARTIK")

    # defination of each function###################

    def openFile(self):

        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"),
                                               ("Text Documents", "*.txt")])

        if self.file == "":

            # no file to open
            self.file = None
        else:

            # Try to open the file
            # set the window title
            self.root.title(os.path.basename(self.file) + " - Notepad")
            self.thisTextArea.delete(1.0, END)

            file = open(self.file, "r")

            self.thisTextArea.insert(1.0, file.read())

            file.close()

    def newFile(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.thisTextArea.delete(1.0, END)

    def saveFile(self):

        if self.file == None:
            # Save as new file
            self.file = asksaveasfilename(initialfile='Untitled.txt',
                                          defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"),
                                                     ("Text Documents", "*.txt")])

            if self.file == "":
                self.file = None
            else:

                # Try to save the file
                file = open(self.file, "w")
                file.write(self.thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.root.title(os.path.basename(self.file) + " - Notepad")

        else:
            file = open(self.file, "w")
            file.write(self.thisTextArea.get(1.0, END))
            file.close()

    def saveASFile(self):
        if self.file == None:
            self.file = asksaveasfilename(initialfile='Untitled.txt',
                                          defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"),
                                                     ("Text Documents", "*.txt")])
            self.root.title(os.path.basename(self.file) + " - Notepad")

            file = open(self.file, "w")
            file.write(self.thisTextArea.get(1.0, END))
            file.close()
        else:
            self.file = asksaveasfilename(initialfile=os.path.basename(self.file),
                                          defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"),
                                                     ("Text Documents", "*.txt")])
            self.root.title(os.path.basename(self.file) + " - Notepad")
            file = open(self.file, "w")
            file.write(self.thisTextArea.get(1.0, END))
            file.close()

    def cut(self):
        self.thisTextArea.event_generate("<<Cut>>")

    def copy(self):
        self.thisTextArea.event_generate("<<Copy>>")

    def paste(self):
        self.thisTextArea.event_generate("<<Paste>>")

    def run(self):

        # Run main application
        self.root.mainloop()
##################################################

    def totalword(self):
        totalword_popup = Toplevel()
        totalword_popup.geometry("200x100")
        totalword_popup.title("Word Count")
        totalword_popup.resizable(0, 0)
        totalword_frame = tkinter.LabelFrame(
            totalword_popup, text="WORD COUNT")
        totalword_frame.pack(pady=20)

        content = self.thisTextArea.get(1.0, END)
        word = len(content.split())
        totalword_time = tkinter.Label(totalword_frame, text=word)
        totalword_time.pack()
        # tkinter.messagebox.showinfo("word count", word)

    def totalcharacter(self):
        totalchar_popup = Toplevel()
        totalchar_popup.geometry("200x100")
        totalchar_popup.title("Character Count")
        totalchar_popup.resizable(0, 0)
        totalchar_frame = tkinter.LabelFrame(
            totalchar_popup, text="CHARACTER COUNT")
        totalchar_frame.pack(pady=20)
        content = self.thisTextArea.get(1.0, END)
        character = len(content.replace(" ", ""))-1
        totalchar_time = tkinter.Label(totalchar_frame, text=character)
        totalchar_time.pack()
        # showinfo("character count", character)

    def createdTime(self):
        ct_popup = Toplevel()
        ct_popup.geometry("200x100")
        ct_popup.title("Created Time")
        ct_popup.resizable(0, 0)
        ct_frame = tkinter.LabelFrame(ct_popup, text="CREATED TIME")
        ct_frame.pack(pady=20)
        # text_find = tkinter.Label(find_frame, text=)
        if self.file == None:
            t = time.ctime(os.path.getmtime("p1_main.py"))
            # showinfo("Created", datetime.datetime.fromtimestamp(t))
            ct_time = tkinter.Label(ct_frame, text=t)
            ct_time.pack()
        else:
            t = time.ctime(os.path.getctime(os.path.basename(self.file)))
            ct_time = tkinter.Label(ct_frame, text=t)
            ct_time.pack()

    def modifiedTime(self):
        mdf_popup = Toplevel()
        mdf_popup.geometry("200x100")
        mdf_popup.title("Modified Time")
        mdf_popup.resizable(0, 0)
        mdf_frame = tkinter.LabelFrame(mdf_popup, text="MODIFIED TIME")
        mdf_frame.pack(pady=20)
        if self.file == None:
            t = time.ctime(os.path.getmtime("p1_main.py"))
            mdf_time = tkinter.Label(mdf_frame, text=t)
            mdf_time.pack()
        else:
            t = time.ctime(os.path.getmtime(os.path.basename(self.file)))
            mdf_time = tkinter.Label(mdf_frame, text=t)
            mdf_time.pack()

    def find(self):
        def find():
            word = find_input.get()
            self.thisTextArea.tag_remove("match", "1.0", END)
            matches = 0
            if word:
                start_pos = "1.0"
                while True:
                    start_pos = self.thisTextArea.search(
                        word, start_pos, stopindex=END)
                    if not start_pos:
                        break
                    end_pos = f"{start_pos}+{len(word)}c"
                    self.thisTextArea.tag_add("match", start_pos, end_pos)
                    matches += 1
                    start_pos = end_pos
                    self.thisTextArea.tag_config(
                        "match", foreground="red", background="yellow")

        def replace():
            word = find_input.get()
            replace_text = replace_input.get()
            content = self.thisTextArea.get(1.0, END)
            new_content = content.replace(word, replace_text)
            self.thisTextArea.delete(1.0, END)
            self.thisTextArea.insert(1.0, new_content)

        find_popup = Toplevel()
        find_popup.geometry("450x300")
        find_popup.title("Find or Replace")
        find_popup.resizable(0, 0)
        ###
        find_frame = tkinter.LabelFrame(find_popup, text="Find and replace")
        find_frame.pack(pady=20)
        text_find = tkinter.Label(find_frame, text='Find')
        text_replace = tkinter.Label(find_frame, text='Replace')
        find_input = tkinter.Entry(find_frame, width=30)
        replace_input = tkinter.Entry(find_frame, width=30)

        find_btn = tkinter.Button(find_frame, text="Find", command=find)
        replace_btn = tkinter.Button(
            find_frame, text="Replace", command=replace)

        text_find.grid(row=0, column=0, padx=4, pady=4)
        text_replace.grid(row=1, column=0, padx=4, pady=4)
        find_input.grid(row=0, column=1, padx=4, pady=4)
        replace_input.grid(row=1, column=1, padx=4, pady=4)
        find_btn.grid(row=2, column=0, padx=8, pady=4)
        replace_btn.grid(row=2, column=1, padx=8, pady=4)

    def bold(self):
        # bold_btn=tkinter.Button(l,)
        text_get = font.Font(font=self.thisTextArea["font"])
        font_now = text_get.actual()['family']
        font_size_now = text_get.actual()['size']
        if text_get.actual()["weight"] == 'normal':
            self.thisTextArea.configure(font=(font_now, font_size_now, "bold"))
        if text_get.actual()["weight"] == 'bold':
            self.thisTextArea.configure(
                font=(font_now, font_size_now, "normal"))

    def font(self):
        font_popup = Toplevel()
        font_popup.geometry("400x300")
        font_popup.title("Font")
        font_popup.resizable(0, 0)
        ##
        font_tuple = font.families()
        font_fmaily = StringVar()
        font_label = Label(font_popup, text="Font")
        font_label.grid(row=0, column=0, padx=15)
        font_box = ttk.Combobox(
            font_popup, width=30, textvariable=font_fmaily, state="readonly")
        font_box["values"] = font_tuple
        font_box.current(font_tuple.index("Arial"))
        font_box.grid(row=1, column=0, padx=15)

        size_variable = IntVar()
        size_label = Label(font_popup, text="Size")
        size_label.grid(row=0, column=1, padx=15)
        size_box = ttk.Combobox(font_popup, width=10,
                                textvariable=size_variable, state="readonly")
        size_box["values"] = tuple(range(8, 100, 2))
        size_box.current(4)
        size_box.grid(row=1, column=1, padx=15)

        font_now = "Arial"
        font_size_now = 16

        def change_font(font_popup):
            global font_now
            font_now = font_fmaily.get()
            self.thisTextArea.configure(font=(font_now, font_size_now))

        def size_change(font_popup):
            global font_size_now
            font_size_now = size_variable.get()
            self.thisTextArea.configure(font=(font_now, font_size_now))

        font_box.bind("<<ComboboxSelected>>", change_font)
        size_box.bind("<<ComboboxSelected>>", size_change)
        # status_bars = Label(notepad, text='status bars')
        # status_bars.pack(side=Tk.BOTTOM)
        # text_change = False
        # def change_word(self):
        #     global text_change
        #     if self.__thisTextArea.edit_modified():
        #         text_change = True
        #         content = self.__thisTextArea.get(1.0, END)
        #         word = len(content.split())
        #         status_bars.config(text=f"CHAR:{word}")
        #     self.__thisTextArea.edit_modified(False)
        # self.__thisTextArea.bind("<<<Modified>>>", change_word)


        # Run main application
notepad = Notepad(width=600, height=400)
notepad.run()
