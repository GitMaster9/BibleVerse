import os
import pickle

import modules.Bible as Bible
from database.chapters.chapter_lengths import get_chapters_from_book_name

def get_book_pickled_by_name(book_name):
    path = "database/pickled/" + str(book_name)

    book = load_book_from_pickle(path)
    if book is None:
        print("LOG: Creating new one...")

        book = get_book_from_txt_new_testament(book_name)

        if book is not None:
            save_book_to_pickle(book, path)
        else:
            print("ERROR: Can't get book from .txt file")

    return book

def get_book_from_txt_new_testament(txt_file_name):
    txt_file_location = "database/new_testament_txt/" + str(txt_file_name) + ".txt"

    book = None
    if os.path.isfile(txt_file_location):
        with open(txt_file_location, encoding="utf8") as f:
            lines = f.readlines()

        all_verses = Bible.extract_book_new_testament(lines)

        chapter_lenghts = get_chapters_from_book_name(txt_file_name)
        if chapter_lenghts:
            book = Bible.get_chapters_from_all_verses_new_testament(all_verses, chapter_lenghts)
        else:
            print("ERROR: chapter_lenghts is None")
    
    else:
        print("ERROR: .txt file doesn't exist")
    
    return book

def load_book_from_pickle(path):
    pickled_file = None
    if os.path.isfile(path):
        with open(path, "rb") as f:
            try:
                pickled_file = pickle.load(f)
            except Exception:
                print(Exception)
    else:
        print("LOG: Pickle file doesn't exist")

    return pickled_file

def save_book_to_pickle(book, path):
    with open(path, "wb") as fp:
        pickle.dump(book, fp)
        print('LOG: Created new pickle file')

def get_verses(book, chapter, verse_from, verse_to = 0):
    if book[3] == "old_testament":
        searched_verses = get_verses_old_testament(book, chapter, verse_from, verse_to)
    elif book[3] == "new_testament":
        searched_verses = get_verses_new_testament(book, chapter, verse_from, verse_to)

    return searched_verses

def get_verses_new_testament(book, chapter, verse_from, verse_to = 0):
    book_name = book[1]
    book = get_book_pickled_by_name(book_name)

    if book is None:
        print("ERROR: Can't get book")
        return None
    
    print("Chapter " + str(chapter) + ": verses " + str(verse_from) + " - " + str(verse_to))

    if chapter == 1:
        verse_to += 1
        if verse_from == 1:
            verse_from = 0

    else:
        verse_from -= 1

    chapter -= 1

    searched_verses = get_verses_from_list_new_testament(book, chapter, verse_from, verse_to)
    if searched_verses is None:
        print("ERROR: Can't get verse(s) from this request")

    expected = verse_to - verse_from
    observed = len(searched_verses)

    if expected != observed:
        print("LOG: Number of verses found is less than the number of verses searched for")

    return searched_verses

def get_verses_old_testament(book, chapter_number, verse_from, verse_to = 0):
    book_name = book[1]
    path = "database/pickled/" + str(book_name)

    with open(path, "rb") as f:
        pickled_book = pickle.load(f)

    chapter_number -= 1
    chapter = pickled_book[chapter_number]

    if verse_to == 0:
        verse_to = verse_from + 1
    verse_from -= 1

    searched_verses = chapter[verse_from:verse_to]

    verses = []
    tmp = ""
    for i in range(len(searched_verses)):
        if i == 0:
            tmp += searched_verses[i]
            verses.append(tmp)

            continue

        tmp = " "
        tmp += searched_verses[i]
        verses.append(tmp)

    return verses

def get_verses_from_list_new_testament(book, chapter, verse_from, verse_to):
    try:
        print(verse_from)
        print(verse_to)
        chapter_to_search = book[chapter]
        searched_verses = chapter_to_search[verse_from:verse_to]
        if searched_verses:
            return searched_verses
        else:
            return None
    except:
        return None