from tkinter import *
from tkinter import filedialog


class TextEditor:

    location = "no_file"

    def open_file(self):
        open_return = filedialog.askopenfile(
            initialdir="C:/", title="Select file to open", filetypes=(("other files", "*.*"), ("text files", "*.txt")))
        if(open_return != None):
            self.text_area.delete(1.0, END)
            for line in open_return:
                self.text_area.insert(END, line)
            self.location = open_return.name
            open_return.close()

    def save_as_file(self):
        f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if f is None:
            return
        else:
            self.location = f.name
            text2save = self.text_area.get(1.0, END)
            f.write(text2save)
            f.close()

    def save(self):
        if self.location == "no_file":
            self.save_as_file()
        else:
            print(self.location)
            f = open(self.location, "w+")
            textsave = self.text_area.get(1.0, END)
            f.write(textsave)
            f.close()

    def new(self):
        self.text_area.delete(1.0, END)
        self.location = "no_file"

    def exit(self):
        win.quit()

    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first", "sel.last")

    def paste_text(self):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())

    def undo_text(self):
        self.text_area.edit_undo()

    def redo_text(self):
        self.text_area.edit_redo()

    def __init__(self, win):
        self.win = win
        win.title("Text Editor")
        self.text_area = Text(self.master, undo=True)
        self.text_area.pack(fill=BOTH, expand=1)
        self.main_menu = Menu()
        self.win.config(menu=self.main_menu)

        self.file_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(
            label="Save As..", command=self.save_as_file)
        self.file_menu.add_command(label="Save", command=self.save)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="New", command=self.new)
        self.file_menu.add_command(label="Quit", command=self.exit)

        self.edit_menu = Menu(self.main_menu, tearoff=False)
        self.edit_menu.add_cascade(label="Edit", menu=self.edit_menu)


win = Tk()
t = TextEditor(win)
win.mainloop()
