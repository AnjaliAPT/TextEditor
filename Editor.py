from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os
import time
import pyautogui as pg


class Menubar:

    def __init__(self, parent):

        self.toolbar = Frame(parent.win, bd=1, relief=RAISED, bg="#1A1A1A")
        self.toolbar.pack(side=TOP, fill=X)
        self.new_img = Image.open("Images/new.png")
        self.new_img = self.new_img.resize((30, 30), Image.ANTIALIAS)
        self.new_eimg = ImageTk.PhotoImage(self.new_img)
        self.new_button = Button(self.toolbar, image=self.new_eimg, relief=FLAT,
                                 command=parent.new_file, border=0, bg="#1A1A1A", cursor="hand2")
        self.new_button.pack(side=LEFT, padx=6, pady=8)

        self.open_img = Image.open("Images/open.png")
        self.open_img = self.open_img.resize((30, 30), Image.ANTIALIAS)
        self.open_eimg = ImageTk.PhotoImage(self.open_img)
        self.open_button = Button(self.toolbar, image=self.open_eimg, relief=FLAT,
                                  command=parent.open_file, border=0, bg="#1A1A1A", cursor="hand2")
        self.open_button.pack(side=LEFT, padx=6, pady=8)

        self.save_img = Image.open("Images/save.png")
        self.save_img = self.save_img.resize((40, 40), Image.ANTIALIAS)
        self.save_eimg = ImageTk.PhotoImage(self.save_img)
        self.save_button = Button(self.toolbar, image=self.save_eimg, relief=FLAT,
                                  command=parent.save, border=0, bg="#1A1A1A", cursor="hand2")
        self.save_button.pack(side=LEFT, padx=6, pady=8)

        self.empty_img = Image.open("Images/empty.png")
        self.empty_img = self.empty_img.resize((40, 50), Image.ANTIALIAS)
        self.empty_eimg = ImageTk.PhotoImage(self.empty_img)
        self.empty_button = Button(self.toolbar, image=self.empty_eimg, relief=FLAT,
                                   border=0, bg="#1A1A1A")
        self.empty_button.pack(side=LEFT, padx=6, pady=8)

        self.cut_img = Image.open("Images/scissors.png")
        self.cut_img = self.cut_img.resize((30, 30), Image.ANTIALIAS)
        self.cut_eimg = ImageTk.PhotoImage(self.cut_img)
        self.cut_button = Button(self.toolbar, image=self.cut_eimg, relief=FLAT,
                                 command=parent.cut, border=0, bg="#1A1A1A", cursor="hand2")
        self.cut_button.pack(side=LEFT, padx=6, pady=8)

        self.copy_img = Image.open("Images/copy.png")
        self.copy_img = self.copy_img.resize((30, 30), Image.ANTIALIAS)
        self.copy_eimg = ImageTk.PhotoImage(self.copy_img)
        self.copy_button = Button(self.toolbar, image=self.copy_eimg, relief=FLAT,
                                  command=parent.copy, border=0, bg="#1A1A1A", cursor="hand2")
        self.copy_button.pack(side=LEFT, padx=6, pady=8)

        self.paste_img = Image.open("Images/paste.png")
        self.paste_img = self.paste_img.resize((30, 30), Image.ANTIALIAS)
        self.paste_eimg = ImageTk.PhotoImage(self.paste_img)
        self.paste_button = Button(self.toolbar, image=self.paste_eimg, relief=FLAT,
                                   command=parent.paste, border=0, bg="#1A1A1A", cursor="hand2")
        self.paste_button.pack(side=LEFT, padx=6, pady=8)

        self.undo_img = Image.open("Images/undo.png")
        self.undo_img = self.undo_img.resize((30, 30), Image.ANTIALIAS)
        self.undo_eimg = ImageTk.PhotoImage(self.undo_img)
        self.undo_button = Button(self.toolbar, image=self.undo_eimg, relief=FLAT,
                                  command=parent.undo, border=0, bg="#1A1A1A", cursor="hand2")
        self.undo_button.pack(side=LEFT, padx=6, pady=8)

        self.redo_img = Image.open("Images/redo.png")
        self.redo_img = self.redo_img.resize((30, 30), Image.ANTIALIAS)
        self.redo_eimg = ImageTk.PhotoImage(self.redo_img)
        self.redo_button = Button(self.toolbar, image=self.redo_eimg, relief=FLAT,
                                  command=parent.redo, border=0, bg="#1A1A1A", cursor="hand2")
        self.redo_button.pack(side=LEFT, padx=6, pady=8)

        self.empty_img = Image.open("Images/empty.png")
        self.empty_img = self.empty_img.resize((40, 50), Image.ANTIALIAS)
        self.empty_eimg = ImageTk.PhotoImage(self.empty_img)
        self.empty_button = Button(self.toolbar, image=self.empty_eimg, relief=FLAT,
                                   border=0, bg="#1A1A1A")
        self.empty_button.pack(side=LEFT, padx=6, pady=8)

        self.empty_img = Image.open("Images/empty.png")
        self.empty_img = self.empty_img.resize((40, 50), Image.ANTIALIAS)
        self.empty_eimg = ImageTk.PhotoImage(self.empty_img)
        self.empty_button = Button(self.toolbar, image=self.empty_eimg, relief=FLAT,
                                   border=0, bg="#1A1A1A")
        self.empty_button.pack(side=LEFT, padx=6, pady=8)

        self.bold_img = Image.open("Images/bold.png")
        self.bold_img = self.bold_img.resize((25, 30), Image.ANTIALIAS)
        self.bold_eimg = ImageTk.PhotoImage(self.bold_img)
        self.bold_button = Button(self.toolbar, image=self.bold_eimg, relief=FLAT,
                                  border=0, bg="#1A1A1A", cursor="hand2")
        self.bold_button.pack(side=LEFT, padx=6, pady=8)

        self.italics_img = Image.open("Images/italics.png")
        self.italics_img = self.italics_img.resize((20, 25), Image.ANTIALIAS)
        self.italics_eimg = ImageTk.PhotoImage(self.italics_img)
        self.italics_button = Button(self.toolbar, image=self.italics_eimg, relief=FLAT,
                                     border=0, bg="#1A1A1A", cursor="hand2")
        self.italics_button.pack(side=LEFT, padx=6, pady=8)

        self.underline_img = Image.open("Images/underline.png")
        self.underline_img = self.underline_img.resize(
            (25, 35), Image.ANTIALIAS)
        self.underline_eimg = ImageTk.PhotoImage(self.underline_img)
        self.underline_button = Button(self.toolbar, image=self.underline_eimg, relief=FLAT,
                                       border=0, bg="#1A1A1A", cursor="hand2")
        self.underline_button.pack(side=LEFT, padx=6, pady=8)


class TextEditor:

    location = "Untitled"

    def __init__(self, win):

        self.win = win

        win.title(self.location + " - My Editor")
        win.iconbitmap(r"Images/editor-icon-11.ico")
        win.geometry("%dx%d+0+0" %
                     (win.winfo_screenwidth(), win.winfo_screenheight()))

        self.mbar = Menubar(self)

        self.line_number_bar = Text(win, width=5, padx=3, takefocus=0,  border=0,
                                    background='DarkOliveGreen1', state='disabled',  wrap='none')
        self.line_number_bar.pack(side='left',  fill=BOTH)

        self.text_area = Text(self.win, undo=1, bg="#212121", fg="white")
        self.text_area.pack(fill=BOTH, expand=1)

        # Main menu

        self.main_menu = Menu()
        self.win.config(menu=self.main_menu)

        # File menu

        self.file_menu = Menu(self.main_menu, tearoff=False, background='#1A1A1A', foreground='white',
                              activebackground='black', activeforeground='white')
        self.main_menu.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(
            label="New File", accelerator="Ctrl+N", command=self.new_file)
        self.file_menu.add_command(
            label="Open File...", accelerator="Ctrl+O", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Save As..", accelerator="Ctrl+Shift+S", command=self.save_as)
        self.file_menu.add_command(
            label="Save", accelerator="Ctrl+S", command=self.save)
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Exit", command=self.quit_window)

        # Edit menu

        self.edit_menu = Menu(self.main_menu, tearoff=False, background='#1A1A1A', foreground='white',
                              activebackground='black', activeforeground='white')
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)

        self.edit_menu.add_command(
            label="Undo", accelerator="Ctrl+Z", command=self.undo)
        self.edit_menu.add_command(
            label="Redo", accelerator="Ctrl+Y", command=self.redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(
            label="Cut", accelerator="Ctrl+X", command=self.cut)
        self.edit_menu.add_command(
            label="Copy", accelerator="Ctrl+C", command=self.copy)
        self.edit_menu.add_command(
            label="Paste", accelerator="Ctrl+V", command=self.paste)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(
            label="Find", accelerator="Ctrl+F", command=self.find)
        self.edit_menu.add_command(
            label="Replace", accelerator="Ctrl+H", command=self.replace)

        # View

        self.view_menu = Menu(self.main_menu, tearoff=False, background='#1A1A1A', foreground='white',
                              activebackground='black', activeforeground='white')
        self.main_menu.add_cascade(label="View", menu=self.view_menu)

        self.view_menu.add_command(
            label="Font", accelerator="Ctrl+Shift+F", command=self.font_box)
        self.view_menu.add_command(
            label="Font Color", command=self.font_color)
        self.view_menu.add_command(
            label="Font Size", command=self.font_size)
        self.view_menu.add_command(
            label="Font Family", command=self.font_family)
        self.view_menu.add_separator()
        self.view_menu.add_command(
            label="Editor Layout", command=self.layout)

        # About

        self.about_menu = Menu(self.main_menu, tearoff=False, background='#1A1A1A', foreground='white',
                               activebackground='black', activeforeground='white')
        self.main_menu.add_cascade(label="About", menu=self.about_menu)

        self.about_menu.add_command(
            label="Keymap", command=self.keymap)
        self.about_menu.add_command(
            label="My Editor", accelerator="Ctrl+~", command=self.my_editor)

        # Keyboard Bindings

        self.keyboard_bindings()

    def new_file(self, *args):
        self.text_area.delete(1.0, END)
        self.location = "Untitled"
        win.title(self.location + " - My Editor")

    def open_file(self, *args):
        open_return = filedialog.askopenfile(
            initialdir="C:/", title="Open File", filetypes=(("other files", "*.*"), ("text files", "*.txt"), ("cpp files", "*.cpp"), ("c files", "*.c"), ("python files", "*.py")))
        if open_return != None:
            self.new_file()
            for line in open_return:
                self.text_area.insert(END, line)
            self.location = open_return.name
            open_return.close()
            win.title(self.location + " - My Editor")

    def save_as(self, *args):
        f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if f is None:
            return
        else:
            self.location = f.name
            text2save = self.text_area.get(1.0, END)
            f.write(text2save)
            f.close()
            win.title(self.location + " - My Editor")

    def save(self, *args):
        if self.location == "Untitled":
            self.save_as()
        else:
            f = open(self.location, "w+")
            textsave = self.text_area.get(1.0, END)
            f.write(textsave)
            f.close()

    def quit_window(self):
        win.quit()

    def copy(self, *args):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut(self, *args):
        self.copy()
        self.text_area.selection_clear()

    def paste(self, *args):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())

    def undo(self, *args):
        self.text_area.edit_undo()

    def redo(self, *args):
        self.text_area.edit_redo()

    def find(self, *args):
        print("New File Find")

    def replace(self, *args):
        print("New File Replace")

    def keymap(self):
        print("Keymap")

    def my_editor(self, *args):
        print("My editor")

    def font_box(self, *args):
        print("Font Box")

    def font_color(self):
        print("Font Color")

    def font_size(self):
        print("Font Size")

    def font_family(self):
        print("Font Family")

    def layout(self):
        print("Editor Layout")

    def keyboard_bindings(self):
        self.text_area.bind('<Control_L><N>', self.new_file)
        self.text_area.bind('<Control_L><n>', self.new_file)
        self.text_area.bind('<Control_L><O>', self.open_file)
        self.text_area.bind('<Control_L><o>', self.open_file)
        self.text_area.bind('<Control_L><S>', self.save)
        self.text_area.bind('<Control_L><s>', self.save)
        self.text_area.bind('<Control_L><Shift_L><S>', self.save_as)
        self.text_area.bind('<Control_L><Shift_L><s>', self.save_as)
        self.text_area.bind('<Control_L><X>', self.cut)
        self.text_area.bind('<Control_L><x>', self.cut)
        self.text_area.bind('<Control_L><C>', self.copy)
        self.text_area.bind('<Control_L><c>', self.copy)
        self.text_area.bind('<Control_L><P>', self.paste)
        self.text_area.bind('<Control_L><p>', self.paste)
        self.text_area.bind('<Control_L><F>', self.find)
        self.text_area.bind('<Control_L><f>', self.find)
        self.text_area.bind('<Control_L><H>', self.replace)
        self.text_area.bind('<Control_L><h>', self.replace)
        self.text_area.bind('<Control_L><Shift_L><F>', self.font_box)
        self.text_area.bind('<Control_L><Shift_L><f>', self.font_box)
        self.text_area.bind('<Control_L><~>', self.my_editor)


# Class constructor


# main
win = Tk()
textedit = TextEditor(win)
win.mainloop()
