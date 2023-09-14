import pickle

pickle_file_to_read = "estera_raw"
pickle_file_to_write = "estera"

def correct_pickle(pickle_file_to_read, pickle_file_to_write):
    with open(pickle_file_to_read, "rb") as f:
        book = pickle.load(f)

    poglavlje1 = book[0]

    verse1a = poglavlje1[0]

    stih1b = poglavlje1[1]

    verse1b = stih1b[2:]

    verse1 = verse1a
    verse1 += "\n"
    verse1 += verse1b

    estera1 = []
    estera1.append(verse1)

    estera_drugi_dio = poglavlje1[2:]
    estera1.extend(estera_drugi_dio)

    estera = []
    estera.append(estera1)

    estera_treci_dio = book[1:]
    estera.extend(estera_treci_dio)

    with open(pickle_file_to_write, "wb") as fp:
        pickle.dump(estera, fp)

correct_pickle(pickle_file_to_read, pickle_file_to_write)