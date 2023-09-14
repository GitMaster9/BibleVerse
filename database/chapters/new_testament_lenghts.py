matej = "25	23	17	25	48	34	29	34	38	42	30	50	58	36	39	28	27	35	30	34	46	46	39	51	46	75	66	20"
marko = "45	28	35	41	43	56	37	38	50	52	33	44	37	72	47	20"
luka = "80	52	38	44	39	49	50	56	62	42	54	59	35	35	32	31	37	43	48	47	38	71	56	53"
ivan = "51	25	36	54	47	71	53	59	41	42	57	50	38	31	27	33	26	40	42	31	25"
djela_apostolska = "26	47	26	37	42	15	60	40	43	48	30	25	52	28	41	40	34	28	40	38	40	30	35	27	27	32	44	31"
rimljanima = "32	29	31	25	21	23	25	39	33	21	36	21	14	23	33	27"
korincanima1 = "31	16	23	21	13	20	40	13	27	33	34	31	13	40	58	24"
korincanima2 = "24	17	18	18	21	18	16	24	15	18	33	21	13"
galacanima = "24	21	29	31	26	18"
efezanima = "23	22	21	32	33	24"
filipljanima = "30	30	21	23"
kolosanima = "29	23	25	18"
solunjanima1 = "10	20	13	18	28"
solunjanima2 = "12	17	18"
timoteju1 = "20	15	16	16	25	21"
timoteju2 = "18	26	17	22"
titu = "16	15	15"
filemonu = "25"
hebrejima = "14	18	19	16	14	20	28	13	28	39	40	29	25"
jakovljeva = "27	26	18	17	20"
petrova1 = "25	25	22	19	14"
petrova2 = "21	22	18"
ivanova1 = "10	29	24	21	21"
ivanova2 = "13"
ivanova3 = "15"
judina = "25"
otkrivenje = "20	29	22	11	14	17	17	13	21	11	19	17	18	20	8	21	18	24	21	15	27	21"

def get_chapters_string_list_from_book_name(book_name):
    if book_name == "matej":
        return matej

    elif book_name == "marko":
        return marko

    elif book_name == "luka":
        return luka

    elif book_name == "ivan":
        return ivan

    elif book_name == "djela_apostolska":
        return djela_apostolska

    elif book_name == "rimljanima":
        return rimljanima

    elif book_name == "korincanima1":
        return korincanima1

    elif book_name == "korincanima2":
        return korincanima2

    elif book_name == "galacanima":
        return galacanima

    elif book_name == "efezanima":
        return efezanima

    elif book_name == "filipljanima":
        return filipljanima

    elif book_name == "kolosanima":
        return kolosanima

    elif book_name == "solunjanima1":
        return solunjanima1

    elif book_name == "solunjanima2":
        return solunjanima2

    elif book_name == "timoteju1":
        return timoteju1

    elif book_name == "timoteju2":
        return timoteju2

    elif book_name == "titu":
        return titu

    elif book_name == "filemonu":
        return filemonu

    elif book_name == "hebrejima":
        return hebrejima

    elif book_name == "jakovljeva":
        return jakovljeva

    elif book_name == "petrova1":
        return petrova1

    elif book_name == "petrova2":
        return petrova2

    elif book_name == "ivanova1":
        return ivanova1

    elif book_name == "ivanova2":
        return ivanova2

    elif book_name == "ivanova3":
        return ivanova3

    elif book_name == "judina":
        return judina

    elif book_name == "otkrivenje":
        return otkrivenje

    return None