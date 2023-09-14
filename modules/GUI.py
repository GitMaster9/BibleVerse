from tkinter import *
import customtkinter
from customtkinter import CTkLabel, CTkEntry, CTkButton, CTkTextbox, CTkFrame
import pyperclip

import modules.Database as Database
import database.books as books

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

book_list = books.get_all_books_names()

frame_listboxes_height = 300
frame_listboxes_width = 900

select_height = 300
select_width = 210

entry_width = 205
listbox_width = 33

frame_buttons_height = 80
frame_buttons_width = 400

buttons_height = 60
buttons_width = 150

frame_result_height = 200
frame_result_width = 900

label_result_height = 50
label_result_width = 150

frame_textbox_height = 230
frame_textbox_width = 520

frame_dummy_height = 230
frame_dummy_width = 160

textbox_width = 530

class WindowMain:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title("Biblijski stihovi GUI")
        self.root.minsize(900, 600)

        self.set_frame_listboxes()
        self.set_frame_buttons()
        self.set_frame_result()

        self.update_books(book_list)

        self.selected_book = None
        self.selected_book_chapters = None
        self.selected_chapter = 0
        self.selected_verse_from = 0
        self.selected_verse_to = 0
        self.chapter_list = []
        self.verse_from_list = []
        self.verse_to_list = []
        self.result = ""

        self.check_all_parameters()

        self.root.mainloop()

    def set_frame_listboxes(self):
        frame_listboxes = CTkFrame(self.root, height=frame_listboxes_height, width=frame_listboxes_width, fg_color="transparent")
        frame_listboxes.grid(row = 0, column = 0)

        frame_listbox_book = CTkFrame(frame_listboxes, height=select_height, width=select_width, fg_color="transparent")
        frame_listbox_book.grid(row = 0, column = 0, padx = 5, pady = 5)

        frame_listbox_chapter = CTkFrame(frame_listboxes, height=select_height, width=select_width, fg_color="transparent")
        frame_listbox_chapter.grid(row = 0, column = 1, padx = 5, pady = 5)

        frame_listbox_verse_from = CTkFrame(frame_listboxes, height=select_height, width=select_width, fg_color="transparent")
        frame_listbox_verse_from.grid(row = 0, column = 2, padx = 5, pady = 5)

        frame_listbox_verse_to = CTkFrame(frame_listboxes, height=select_height, width=select_width, fg_color="transparent")
        frame_listbox_verse_to.grid(row = 0, column = 3, padx = 5, pady = 5)

        Grid.columnconfigure(self.root, 0, weight = 1)

        label_book = CTkLabel(frame_listbox_book, text="Odaberi knjigu")
        label_book.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.entry_book = CTkEntry(frame_listbox_book, width=entry_width) #width=entry_width
        self.entry_book.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.listbox_books = Listbox(frame_listbox_book, width=listbox_width)
        self.listbox_books.grid(row = 2, column = 0, padx = 5, pady = 5)

        self.listbox_books.bind("<<ListboxSelect>>", self.select_book)
        self.entry_book.bind("<KeyRelease>", self.check_book_listbox)

        label_chapter = CTkLabel(frame_listbox_chapter, text="Odaberi poglavlje")
        label_chapter.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.entry_chapter = CTkEntry(frame_listbox_chapter, width=entry_width)
        self.entry_chapter.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.listbox_chapters = Listbox(frame_listbox_chapter, width=listbox_width)
        self.listbox_chapters.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.listbox_chapters.bind("<<ListboxSelect>>", self.select_chapter)
        self.entry_chapter.bind("<KeyRelease>", self.check_chapter_listbox)

        label_verse_from = CTkLabel(frame_listbox_verse_from, text="Odaberi početni stih")
        label_verse_from.grid(row = 0, column = 2, padx = 5, pady = 5)

        self.entry_verse_from = CTkEntry(frame_listbox_verse_from, width=entry_width)
        self.entry_verse_from.grid(row = 1, column = 2, padx = 5, pady = 5)

        self.listbox_verse_from = Listbox(frame_listbox_verse_from, width=listbox_width)
        self.listbox_verse_from.grid(row = 2, column = 2, padx = 5, pady = 5)

        self.listbox_verse_from.bind("<<ListboxSelect>>", self.select_verse_from)
        self.entry_verse_from.bind("<KeyRelease>", self.check_verse_from_listbox)

        label_verse_to = CTkLabel(frame_listbox_verse_to, text="Odaberi završni stih")
        label_verse_to.grid(row = 0, column = 3, padx = 5, pady = 5)

        self.entry_verse_to = CTkEntry(frame_listbox_verse_to, width=entry_width)
        self.entry_verse_to.grid(row = 1, column = 3, padx = 5, pady = 5)

        self.listbox_verse_to = Listbox(frame_listbox_verse_to, width=listbox_width)
        self.listbox_verse_to.grid(row = 2, column = 3, padx = 5, pady = 5)

        self.listbox_verse_to.bind("<<ListboxSelect>>", self.select_verse_to)
        self.entry_verse_to.bind("<KeyRelease>", self.check_verse_to_listbox)

    def set_frame_buttons(self):
        frame_buttons = CTkFrame(self.root, height=frame_buttons_height, width=frame_buttons_width, fg_color="transparent")
        frame_buttons.grid(row = 1, column = 0, pady = 5)

        self.button_search = CTkButton(frame_buttons, text="Traži", command=self.submit_search)
        self.button_search.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.button_copy = CTkButton(frame_buttons, text="Kopiraj", command=self.copy_to_clipboard)
        self.button_copy.grid(row = 0, column = 1, padx = 5, pady = 5)

    def set_frame_result(self):
        frame_result = CTkFrame(self.root, height=frame_result_height, width=frame_result_width, fg_color="transparent")
        frame_result.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = NSEW)

        frame_dummy1 = CTkFrame(frame_result, height=frame_dummy_height, width=frame_dummy_width, fg_color="transparent")
        frame_dummy1.grid(row = 0, column = 0, padx = 5, pady = 5)

        frame_textbox = CTkFrame(frame_result, height=frame_textbox_height, width=frame_textbox_width, fg_color="transparent")
        frame_textbox.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = NSEW)

        frame_dummy2 = CTkFrame(frame_result, height=frame_dummy_height, width=frame_dummy_width, fg_color="transparent")
        frame_dummy2.grid(row = 0, column = 2, padx = 5, pady = 5)

        self.textbox_result = CTkTextbox(frame_textbox, width=textbox_width)
        self.textbox_result.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = NSEW)

        Grid.rowconfigure(self.root, 2, weight = 1)

        Grid.columnconfigure(frame_result, 0, weight = 2)
        Grid.columnconfigure(frame_result, 1, weight = 1)
        Grid.columnconfigure(frame_result, 2, weight = 2)

        Grid.rowconfigure(frame_result, 0, weight = 1)

        Grid.columnconfigure(frame_textbox, 0, weight = 1)
        Grid.rowconfigure(frame_textbox, 0, weight = 1)

    def update_books(self, data):
        self.listbox_books.delete(0, END)

        for item in data:
            self.listbox_books.insert(END, item)

    def select_book(self, e):
        book_title = self.listbox_books.get(ANCHOR)
        if self.selected_book:
            if book_title == self.selected_book[2]:
                return
        
        self.entry_book.delete(0, END)

        self.selected_book = books.get_book_by_title(book_title)
        self.selected_chapter = 0
        self.selected_verse_from = 0
        self.selected_verse_to = 0

        if self.selected_book:
            self.selected_book_chapters = Database.get_chapters_from_book_name(self.selected_book[1])

        self.entry_book.insert(0, book_title)
        self.chapter_list = []
        for i in range(1, len(self.selected_book_chapters) + 1):
            self.chapter_list.append(str(i))

        self.update_chapters(self.chapter_list)
        self.entry_chapter.delete(0, END)

        self.verse_from_list = []
        self.verse_to_list = []
        self.update_verse_from(self.verse_from_list)
        self.update_verse_to(self.verse_to_list)
        self.entry_verse_from.delete(0, END)
        self.entry_verse_to.delete(0, END)

        self.check_all_parameters()

    def check_book_listbox(self, e):
        typed = self.entry_book.get()

        if typed == "":
            data = book_list
        else:
            data = []
            for item in book_list:
                if typed.lower() in item.lower():
                    data.append(item)

        self.update_books(data)

    def update_chapters(self, data):
        self.listbox_chapters.delete(0, END)

        for item in data:
            self.listbox_chapters.insert(END, item)

    def select_chapter(self, e):
        try:
            chapter = int(self.listbox_chapters.get(ANCHOR))
            if chapter == self.selected_chapter:
                return
            
            self.selected_chapter = chapter

            self.entry_chapter.delete(0, END)
            self.entry_verse_from.delete(0, END)
            self.entry_verse_to.delete(0, END)

            self.entry_chapter.insert(0, str(chapter))

            self.verse_from_list = []
            self.verse_to_list = []

            for i in range(1, self.selected_book_chapters[chapter - 1] + 1):
                self.verse_from_list.append(str(i))
                self.verse_to_list.append(str(i))

            self.update_verse_from(self.verse_from_list)
            self.update_verse_to(self.verse_to_list)

        except Exception:
            pass

        self.check_all_parameters()

    def check_chapter_listbox(self, e):
        typed = self.entry_chapter.get()

        if typed == "":
            data = self.chapter_list
        else:
            data = []
            for item in self.chapter_list:
                if typed in item:
                    data.append(item)

        self.update_chapters(data)

    def update_verse_from(self, data):
        self.listbox_verse_from.delete(0, END)

        for item in data:
            self.listbox_verse_from.insert(END, item)

    def select_verse_from(self, e):
        try:
            verse_from = int(self.listbox_verse_from.get(ANCHOR))
            if verse_from == self.selected_verse_from:
                return
            
            self.selected_verse_from = verse_from

            self.entry_verse_from.delete(0, END)
            self.entry_verse_from.insert(0, str(verse_from))

            self.entry_verse_to.delete(0, END)

            self.verse_to_list = []

            for item in self.verse_from_list:
                if int(item) >= self.selected_verse_from:
                    self.verse_to_list.append(item)

            self.update_verse_to(self.verse_to_list)

        except Exception:
            pass

        self.check_all_parameters()

    def check_verse_from_listbox(self, e):
        typed = self.entry_verse_from.get()

        if typed == "":
            data = self.verse_from_list
        else:
            data = []
            for item in self.verse_from_list:
                if typed in item:
                    data.append(item)

        self.update_verse_from(data)

    def update_verse_to(self, data):
        self.listbox_verse_to.delete(0, END)

        for item in data:
            self.listbox_verse_to.insert(END, item)

    def select_verse_to(self, e):
        try:
            verse_to = int(self.listbox_verse_to.get(ANCHOR))
            if verse_to == self.selected_verse_to:
                return
            
            self.selected_verse_to = verse_to

            self.entry_verse_to.delete(0, END)
            self.entry_verse_to.insert(0, str(verse_to))

        except Exception:
            pass

        self.check_all_parameters()

    def check_verse_to_listbox(self, e):
        typed = self.entry_verse_to.get()

        if typed == "":
            data = self.verse_to_list
        else:
            data = []
            for item in self.verse_to_list:
                if typed in item:
                    data.append(item)

        self.update_verse_to(data)

    def check_all_parameters(self):
        book_title = self.entry_book.get()
        chapter = self.entry_chapter.get()
        verse_from = self.entry_verse_from.get()
        
        if book_title == "" or chapter == "" or verse_from == "":
            self.button_search.configure(state=DISABLED)
        
        else:
            self.button_search.configure(state=NORMAL)

    def submit_search(self):
        book_title = self.entry_book.get()
        chapter_string = self.entry_chapter.get()
        verse_from_string = self.entry_verse_from.get()
        verse_to_string = self.entry_verse_to.get()

        if book_title == "" or chapter_string == "" or verse_from_string == "":
            print("ERROR: Book title, chapter or verse start is None")
            return

        book = books.get_book_by_title(book_title)

        if book is None:
            print("ERROR: Can't find book by title selected")
            return
        
        chapter = int(chapter_string)
        verse_from = int(verse_from_string)

        if verse_to_string == "":
            verse_to = verse_from
        else:
            verse_to = int(verse_to_string)

        results = Database.get_verses(book, chapter, verse_from, verse_to)
        
        if results is None:
            print("ERROR: Can't find verses")
            return
        
        result = ""

        for verse in results:
            result += verse

        self.result = result

        self.textbox_result.configure(state="normal")
        self.textbox_result.delete(0.0, END)
        self.textbox_result.insert("0.0", self.result)
        self.textbox_result.configure(state="disabled")

    def copy_to_clipboard(self):
        pyperclip.copy(self.result)