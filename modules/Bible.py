def extract_book_new_testament(lines):
    book = []
    verse = 0
    digits = 0
    text = ""

    for line in lines:
        for i in range(len(line)):
            if line[i].isdigit():
                if digits == 0:
                    book.append(text)
                    verse += 1
                    text = ""
                
                digits += 1
            else:
                digits = 0

            text += line[i]
            
    book.append(text)

    return book

def extract_book_v2(lines):
    book = [[]]
    chapters = []
    chapter = 0
    verse = 0
    digits = 0
    text = ""
    number_as_string = ""

    for line in lines:
        for i in range(len(line)):
            if line[i].isdigit():
                if digits == 0:
                    number_as_string = ""
                
                number_as_string += line[i]
                digits += 1
            else:
                if digits > 0:
                    chapters.append(text)

                    text = ""

                    number_as_int = int(number_as_string)
                    if (number_as_int - chapter) == 1:
                        verse += 1
                    else:
                        book.append(chapters)
                        chapters = []
                        chapter += 1
                        verse = 1

                    text += number_as_string

                    digits = 0

                text += line[i]

    chapters.append(text)
    book.append(chapters)

    return book

def get_chapters_from_all_verses_new_testament(all_verses, chapter_lenghts):
    chapters = []
    verse_index = 0
    
    for i in range(len(chapter_lenghts)):
        cut_from = verse_index
        cut_to = cut_from + chapter_lenghts[i]
        if i == 0: # zbog trenutnog nacina ekstrakcije stringa iz teksta
            cut_to += 1
        tmp = all_verses[cut_from:cut_to]
        chapters.append(tmp)
        verse_index = cut_to

    return chapters