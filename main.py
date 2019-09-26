from nltk.tokenize import word_tokenize
from nltk import FreqDist
from pdf_service_manager import ServiceManagerPdf
from vector_space_similarity import ServiceTextMining
from models import PdfOutput, DocumentSimilary
import numpy as np


import csv
import string
import glob2


def main():
    files = []
    fileNames = sorted(glob2.glob("docs/*.txt"))
    for filename in fileNames:
        files.append(open(filename, "r+").read())

    count = 0

    coefient_doc = []
    coeficient_array = []

    while count < len(files):
        serviceTextMining = ServiceTextMining()
        terms = serviceTextMining.select_terms([files[count], files[count - 1]])
        relevation_matriz_docs = serviceTextMining.create_matriz_tf_terms(terms)

        document = DocumentSimilary(
            [fileNames[count], fileNames[count - 1]],
            serviceTextMining.cosine_similarity(
                [files[count], files[count - 1]], relevation_matriz_docs
            ),
        )

        coeficient_array.append(document.coeficient)
        coefient_doc.append(document)
        count += 1

    greater_similarity = np.array(coeficient_array).max()
    for doc in coefient_doc:
        if greater_similarity == doc.coeficient:
            print(
                "Documentos {0} distancia dos cossenos {1}".format(
                    doc.files, doc.coeficient
                )
            )


if __name__ == "__main__":
    main()
