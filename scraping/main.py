import requests
from bs4 import BeautifulSoup
import os
import pickle

base_URL = "https://biblija.ks.hr/"
book = ("malahija", "malahija", 3)

def save_book_pickle(book):
    pickle_file_name = book[0]
    book_URL = book[1]
    n_chapters = book[2]

    chapters = create_chapters_from_book(book_URL, n_chapters)

    with open(pickle_file_name, "wb") as fp:
        pickle.dump(chapters, fp)

def create_chapters_from_book(book_URL, n_chapters):
    chapters = [[]]

    for i in range(1, n_chapters + 1):
        end_URL = "/" + str(i)
        url = base_URL + book_URL  + end_URL
        chapter = create_chapter_from_url(url)
        chapters.append(chapter)

    del chapters[0]

    return chapters

def create_chapter_from_url(url):
    response = requests.get(url)
    doc = BeautifulSoup(response.text, 'html.parser')

    bible_lines = doc.findAll('span', attrs={"class":"bible-line"})

    lines = []

    for bible_line in bible_lines:
        for data in bible_line(['h2', 'h3', 'h4']):
            data.decompose()

        line = bible_line.get_text(separator="\n")
        line = line.strip()
        line = os.linesep.join([s for s in line.splitlines() if s])
        lines.append(line)

    chapter = []

    for line in lines:
        array = []
        text = ""
        for j in range(len(line)):
            if line[j] == "\r":
                array.append(text)
                text = ""
                continue
                
            if line[j] == "\n":
                continue

            text += line[j]

            if j == len(line) - 1:
                array.append(text)
            
        final_array = []
        for line in array:
            line = line.strip()
            final_array.append(line)

        verse = ""
        for k in range(len(final_array)):
            if k == 0:
                verse += final_array[k]
                verse += " "

                continue

            if k == 1:
                verse += final_array[k]

                continue

            verse += "\n"
            verse += final_array[k]

        chapter.append(verse)

    return chapter

save_book_pickle(book)