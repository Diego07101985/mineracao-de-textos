from nltk.tokenize import word_tokenize
from nltk import FreqDist
from pdf_service_manager import ServiceManagerPdf
from vector_space_similarity import ServiceTextMining
from models import PdfOutput

import csv
import string
import glob2


def main():
    files = []
    fileNames = sorted(glob2.glob("docs/*.txt"))
    for filename in fileNames:
        files.append(open(filename, "r+").read())

    count = 0

    while count < len(files):
        serviceTextMining = ServiceTextMining()
        terms = serviceTextMining.select_terms([files[count], files[count - 1]])
        relevation_matriz_docs = serviceTextMining.create_matriz_tf_terms(terms)

        print(relevation_matriz_docs)
        print(
            serviceTextMining.cosine_similarity(
                [files[count], files[count - 1]], relevation_matriz_docs
            )
        )

        count += 1


if __name__ == "__main__":
    main()
