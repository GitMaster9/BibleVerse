import database.chapters.chapter_lengths as chapter_lengths

matej_lengths = chapter_lengths.get_chapters_from_book_name("matej")
marko_lengths = chapter_lengths.get_chapters_from_book_name("marko")
luka_lengths = chapter_lengths.get_chapters_from_book_name("luka")
ivan_lengths = chapter_lengths.get_chapters_from_book_name("ivan")
djela_apostolska_lengths = chapter_lengths.get_chapters_from_book_name("djela_apostolska")
rimljanima_lengths = chapter_lengths.get_chapters_from_book_name("rimljanima")
korincanima1_lengths = chapter_lengths.get_chapters_from_book_name("korincanima1")
korincanima2_lengths = chapter_lengths.get_chapters_from_book_name("korincanima2")
galacanima_lengths = chapter_lengths.get_chapters_from_book_name("galacanima")
efezanima_lengths = chapter_lengths.get_chapters_from_book_name("efezanima")
filipljanima_lengths = chapter_lengths.get_chapters_from_book_name("filipljanima")
kolosanima_lengths = chapter_lengths.get_chapters_from_book_name("kolosanima")
solunjanima1_lengths = chapter_lengths.get_chapters_from_book_name("solunjanima1")
solunjanima2_lengths = chapter_lengths.get_chapters_from_book_name("solunjanima2")
timoteju1_lengths = chapter_lengths.get_chapters_from_book_name("timoteju1")
timoteju2_lengths = chapter_lengths.get_chapters_from_book_name("timoteju2")
titu_lengths = chapter_lengths.get_chapters_from_book_name("titu")
filemonu_lengths = chapter_lengths.get_chapters_from_book_name("filemonu")
hebrejima_lengths = chapter_lengths.get_chapters_from_book_name("hebrejima")
jakovljeva_lengths = chapter_lengths.get_chapters_from_book_name("jakovljeva")
petrova1_lengths = chapter_lengths.get_chapters_from_book_name("petrova1")
petrova2_lengths = chapter_lengths.get_chapters_from_book_name("petrova2")
ivanova1_lengths = chapter_lengths.get_chapters_from_book_name("ivanova1")
ivanova2_lengths = chapter_lengths.get_chapters_from_book_name("ivanova2")
ivanova3_lengths = chapter_lengths.get_chapters_from_book_name("ivanova3")
judina_lengths = chapter_lengths.get_chapters_from_book_name("judina")
otkrivenje_lengths = chapter_lengths.get_chapters_from_book_name("otkrivenje")

# ID number, book name (internal), full name (title), new_testament, book length
matej = (47, "matej", "Evanđelje po Mateju", "new_testament", matej_lengths)
marko = (48, "marko", "Evanđelje po Marku", "new_testament", marko_lengths)
luka = (49, "luka", "Evanđelje po Luki", "new_testament", luka_lengths)
ivan = (50, "ivan", "Evanđelje po Ivanu", "new_testament", ivan_lengths)
djela_apostolska = (51, "djela_apostolska", "Djela apostolska", "new_testament", djela_apostolska_lengths)
rimljanima = (52, "rimljanima", "Poslanica Rimljanima", "new_testament", rimljanima_lengths)
korincanima1 = (53, "korincanima1", "Prva poslanica Korinćanima", "new_testament", korincanima1_lengths)
korincanima2 = (54, "korincanima2", "Druga poslanica Korinćanima", "new_testament", korincanima2_lengths)
galacanima = (55, "galacanima", "Poslanica Galaćanima", "new_testament", galacanima_lengths)
efezanima = (56, "efezanima", "Poslanica Efežanima", "new_testament", efezanima_lengths)
filipljanima = (57, "filipljanima", "Poslanica Filipljanima", "new_testament", filipljanima_lengths)
kolosanima = (58, "kolosanima", "Poslanica Kološanima", "new_testament", kolosanima_lengths)
solunjanima1 = (59, "solunjanima1", "Prva poslanica Solunjanima", "new_testament", solunjanima1_lengths)
solunjanima2 = (60, "solunjanima2", "Druga poslanica Solunjanima", "new_testament", solunjanima2_lengths)
timoteju1 = (61, "timoteju1", "Prva poslanica Timoteju", "new_testament", timoteju1_lengths)
timoteju2 = (62, "timoteju2", "Druga poslanica Timoteju", "new_testament", timoteju2_lengths)
titu = (63, "titu", "Poslanica Titu", "new_testament", titu_lengths)
filemonu = (64, "filemonu", "Poslanica Filemonu", "new_testament", filemonu_lengths)
hebrejima = (65, "hebrejima", "Poslanica Hebrejima", "new_testament", hebrejima_lengths)
jakovljeva = (66, "jakovljeva", "Jakovljeva poslanica", "new_testament", jakovljeva_lengths)
petrova1 = (67, "petrova1", "Prva Petrova poslanica", "new_testament", petrova1_lengths)
petrova2 = (68, "petrova2", "Druga Petrova poslanica", "new_testament", petrova2_lengths)
ivanova1 = (69, "ivanova1", "Prva Ivanova poslanica", "new_testament", ivanova1_lengths)
ivanova2 = (70, "ivanova2", "Druga Ivanova poslanica", "new_testament", ivanova2_lengths)
ivanova3 = (71, "ivanova3", "Treća Ivanova poslanica", "new_testament", ivanova3_lengths)
judina = (72, "judina", "Judina poslanica", "new_testament", judina_lengths)
otkrivenje = (73, "otkrivenje", "Otkrivenje", "new_testament", otkrivenje_lengths)

new_testament_books = []
new_testament_books.append(matej)
new_testament_books.append(marko)
new_testament_books.append(luka)
new_testament_books.append(ivan)
new_testament_books.append(djela_apostolska)
new_testament_books.append(rimljanima)
new_testament_books.append(korincanima1)
new_testament_books.append(korincanima2)
new_testament_books.append(galacanima)
new_testament_books.append(efezanima)
new_testament_books.append(filipljanima)
new_testament_books.append(kolosanima)
new_testament_books.append(solunjanima1)
new_testament_books.append(solunjanima2)
new_testament_books.append(timoteju1)
new_testament_books.append(timoteju2)
new_testament_books.append(titu)
new_testament_books.append(filemonu)
new_testament_books.append(hebrejima)
new_testament_books.append(jakovljeva)
new_testament_books.append(petrova1)
new_testament_books.append(petrova2)
new_testament_books.append(ivanova1)
new_testament_books.append(ivanova2)
new_testament_books.append(ivanova3)
new_testament_books.append(judina)
new_testament_books.append(otkrivenje)

def get_books():
    return new_testament_books

def get_books_names():
    new_testament_books_names = []
    for book in new_testament_books:
        name = book[2]
        new_testament_books_names.append(name)
        
    return new_testament_books_names

def get_book_by_title(book_title):
    for book in new_testament_books:
        title = book[2]
        if title == book_title:
            return book
        
    return None