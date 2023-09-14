import database.chapters.old_testament_lenghts as old_testament_lenghts
import database.chapters.new_testament_lenghts as new_testament_lenghts

def get_chapters_from_string(numbers_as_string):
    numbers_as_string_separator = ""

    for number_as_string in numbers_as_string:
        tmp = number_as_string

        if tmp == "\t":
            tmp = ","

        numbers_as_string_separator += tmp

    text = ""
    strings = []

    for character in numbers_as_string_separator:
        if character == ",":
            strings.append(text)
            text = ""

        else:
            text += character

    strings.append(text)

    numbers = []
    for numbers_as_string in strings:
        number = int(numbers_as_string)
        numbers.append(number)

    return numbers

def get_chapters_from_book_name(book_name):
    book_length = []

    book_length_string_list = old_testament_lenghts.get_chapters_string_list_from_book_name(book_name)

    if book_length_string_list:
        for book_length_string in book_length_string_list:
            book_length_current = get_chapters_from_string(book_length_string)
            book_length.extend(book_length_current)

        return book_length
    
    book_length_string = new_testament_lenghts.get_chapters_string_list_from_book_name(book_name)

    if book_length_string:
        book_length = get_chapters_from_string(book_length_string)

    return book_length