from pdf_service_manager import ServiceManagerPdf
from vector_space_similarity import ServiceTextMining
from models import PdfOutput, DocumentSimilary


import numpy as np


import csv
import string
import glob2


def main():
    files = []
    # 1 - Conjunto de dados curto
    fileNames = sorted(glob2.glob("curto/*.txt"))
    for filename in fileNames:
        files.append(open(filename, "r+").read())

    serviceTextMining = ServiceTextMining()
    print("Tópico 1 - Matrix TF * IDF")
    terms = serviceTextMining.select_terms(files)
    matriz_tf = serviceTextMining.create_matriz_itf_terms(terms)
    matriz_df = serviceTextMining.create_matriz_idf_terms(terms, files)
    matriz_tf_df = serviceTextMining.create_matriz_tf_df_terms(matriz_tf, matriz_df)

    print("Criando arquivo csv")
    csv_file = open("trabalho3.csv", "w+")
    csv_manages = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    csv_file.write("@terms")
    csv_file.write("\n")
    csv_manages.writerow(terms)
    csv_file.write("@matriz_tf")
    csv_file.write("\n")
    for line in range(len(matriz_tf)):
        csv_manages.writerow(matriz_tf[line])
    csv_file.write("@matriz_df")
    csv_file.write("\n")
    csv_manages.writerow(matriz_df)
    csv_file.write("@matriz_df_idf")
    csv_file.write("\n")
    for line in range(len(matriz_tf_df)):
        csv_manages.writerow(matriz_tf_df[line])

    # Deve

    # Com o	conjunto de	dados longo
    query = "but kate's job  , if you will "

    print("Calculo distancia dos cossenos a partir de uma query = {0}".format(query))
    distance = serviceTextMining.calc_distance_cosseno_in_query(query)

    print("Tópico 2 - 10 Documentos mais relevantes")
    nmax = serviceTextMining.Nmaxelements(distance, 10)

    for document in nmax:
        print(
            "Documento {0} distancia dos cossenos {1}".format(
                document.file, document.coeficient
            )
        )
    pdfOutput = PdfOutput(
        None,
        np.transpose(matriz_tf),
        matriz_df,
        np.transpose(matriz_tf_df),
        terms,
        fileNames,
        nmax,
        query,
    )

    servicePdfManager = ServiceManagerPdf()
    servicePdfManager.writePdf(pdfOutput)


if __name__ == "__main__":
    main()
