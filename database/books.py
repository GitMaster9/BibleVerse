import database.old_testament as old_testament
import database.new_testament as new_testament

def get_old_testament_books():
    old_testament_books = old_testament.get_books()
    return old_testament_books

def get_new_testament_books():
    new_testament_books = new_testament.get_books()
    return new_testament_books

def get_all_books():
    old_testament_books = old_testament.get_books()
    new_testament_books = new_testament.get_books()

    all_books = []
    all_books.extend(old_testament_books)
    all_books.extend(new_testament_books)

    return all_books

def get_old_testament_books_names():
    old_testament_books_names = old_testament.get_books_names()
    return old_testament_books_names

def get_new_testament_books_names():
    new_testament_books_names = new_testament.get_books_names()
    return new_testament_books_names

def get_all_books_names():
    old_testament_books_names = get_old_testament_books_names()
    new_testament_books_names = get_new_testament_books_names()

    all_books_names = []
    all_books_names.extend(old_testament_books_names)
    all_books_names.extend(new_testament_books_names)

    return all_books_names

def get_book_by_title(book_title):
    book = old_testament.get_book_by_title(book_title)

    if book is None:
        book = new_testament.get_book_by_title(book_title)

    return book