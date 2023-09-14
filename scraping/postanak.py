import pickle

pickle_file_to_read = "postanak_raw"
pickle_file_to_write = "postanak"

def correct_pickle(pickle_file_to_read, pickle_file_to_write):
    with open(pickle_file_to_read, "rb") as f:
        book = pickle.load(f)

    poglavlje47 = book[46]

    stih4 = poglavlje47[3]

    index_to_stop = stih4.find("<5a>")

    verse4 = stih4[0:index_to_stop - 1]

    part2 = stih4[index_to_stop:]

    index_to_stop = part2.find("«")

    verse5 = part2[0:index_to_stop + 1]

    verse6 = part2[index_to_stop + 2:]

    postanak47 = poglavlje47[0:3]

    postanak47.append(verse4)
    postanak47.append(verse5)
    postanak47.append(verse6)
    
    postanak_treci_dio = poglavlje47[4:9]

    postanak47.extend(postanak_treci_dio)

    stih12 = poglavlje47[9]

    index_to_stop = stih12.find("<13d>")
    verse12 = stih12[0:index_to_stop - 1]
    
    postanak47.append(verse12)

    verse13 = stih12[index_to_stop:]

    postanak47.append(verse13)

    postanak_cetvrti_dio = poglavlje47[10:]
    postanak47.extend(postanak_cetvrti_dio)

    postanak = book[0:46]
    postanak_nesto = book[47:]

    postanak.append(postanak47)
    postanak.extend(postanak_nesto)

    with open(pickle_file_to_write, "wb") as fp:
        pickle.dump(postanak, fp)

correct_pickle(pickle_file_to_read, pickle_file_to_write)