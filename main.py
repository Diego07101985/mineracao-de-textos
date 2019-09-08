from pdf_writer import ServiceExtractPdf

# from nltk.tokenize import sent_tokenize


def main():
    fp = open("Termo-de-Aceitacao.pdf", "rb")
    serviceExtract = ServiceExtractPdf(fp)
    str = serviceExtract.readPDF()

    print(str)
    # sentences = sent_tokenize(str)

    # for s in sentences:
    #     print(s)

    fp.close()


if __name__ == "__main__":
    main()
