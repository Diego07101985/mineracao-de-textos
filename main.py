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

    serviceTextMining = ServiceTextMining()

    terms = serviceTextMining.select_terms(files)
    matriz_tf = serviceTextMining.create_matriz_tf_terms(terms)
    matriz_df = serviceTextMining.create_matriz_df_terms(terms, files)

    result = []

    # iterate through rows of X
    for i in range(len(matriz_tf)):
        result.append([])

        # # iterate through columns of Y
        for j in range(len(matriz_df)):
            # iterate through rows of Y
            #
            print(
                "linha {0} coluna {1} TF {2}  DF {3}= {4}".format(
                    i,
                    j,
                    matriz_tf[i][j],
                    matriz_df[j][1],
                    round(matriz_df[j][1] * matriz_tf[i][j], 3),
                )
            )
            result[i].append(round(matriz_df[j][1] * matriz_tf[i][j], 3))

    print(result)

    #     for k in range(len(matriz_df)):
    #         result[i][j] += matriz_tf[i][k] * matriz_df[k][j]

    # greater_similarity = np.array(coeficient_array).max()
    # for doc in coefient_doc:
    #     if greater_similarity == doc.coeficient:
    #         print(
    #             "Documentos {0} distancia dos cossenos {1}".format(
    #                 doc.files, doc.coeficient
    #             )
    #         )


if __name__ == "__main__":
    main()
