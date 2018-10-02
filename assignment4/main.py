from assignment4 import conllx_reader as cr


def get_swedish_corpus():
    path = "./data"
    suffix = ".conll"
    return cr.get_files(path, suffix)[0]


def get_subject_verbs():
    corpus = get_swedish_corpus()
    print(corpus)
    sentences = cr.read_sentences(corpus)
    print(sentences[0])
    new_sentences = cr.split_rows(sentences, "abcdefghijklmnopqrst")
    split_row = cr.split_rows(new_sentences, )
    for x in range(0, 10):
        print(new_sentences[x])


def get_subject_verb_objects():
    corpus = get_swedish_corpus()

    print("tmap")


def main():
    get_subject_verbs()


if __name__ == "__main__":
    main()