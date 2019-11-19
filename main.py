from pdf_service_manager import ServiceManagerPdf
from vector_space_similarity import ServiceTextMining
from models import PdfOutput, DocumentSimilary
from classification.lazy import Knn
from rating_classifier import Rating
from kmeans_spark import K_Means


import numpy as np


import csv
import string
import glob2


def main():

    query = "HAL is a multi-disciplinary open access"
    # query = "Part-of-speech (PoS ) tagging is one of the earliest steps of NLP. However, in spite of its linguistic nature, linguistic studies comparing the impact of diﬀerent"
    fileNames = sorted(glob2.glob(
        "./teste/temporal_tagging_of_noisey.txt"))
    for filename in fileNames:
        query = open(filename, "r+").read()

    serviceTextMining = ServiceTextMining()
    distance = serviceTextMining.calc_euclidian_distance_in_query(query)
    # files = []
    # fileNames = sorted(glob2.glob("longo/*.txt"))
    # for filename in fileNames:
    #     files.append(open(filename, "r+").read())

    # serviceTextMining = ServiceTextMining()
    # # print("Tópico 1 - Matrix TF * IDF")
    # terms = serviceTextMining.select_terms(files)
    # matriz_tf = serviceTextMining.create_matriz_itf_terms(terms)
    # matriz_df = serviceTextMining.create_matriz_idf_terms(terms, files)
    # matriz_tf_df = serviceTextMining.create_matriz_tf_df_terms(
    #     matriz_tf, matriz_df)

    # kmean = K_Means(3)
    # kmean.execute(matriz_tf_df)

    # for cluster in kmean.execute(matriz_tf_df):
    #     print("Cluster {0} \n".format(cluster[0]))
    #     for doc in cluster[1]:
    #         if(doc.distance_cosine != 0):
    #             print("Doc {0}".format(doc.id))
    #             print("Distance {0}".format(doc.distance_cosine))

    # list_list = []
    # list1 = [2, 30, 20, 6, 42]
    # list2 = [4, 98, 43, 3, 2]
    # list3 = [3, 5, 53, 54, 32]

    # list_list.append(list1)
    # list_list.append(list2)
    # list_list.append(list3)

    # # 4, 54, 53, 54, 42

    # print(np.array(list(zip(list1, list2, list3))))
    # list4 = [max(value) for value in list(zip(list1, list2, list3))]

    # # index = 0

    # print(list4)

    # list1 = [ele for ele in list1 if ele in list4]
    # list2 = [ele for ele in list2 if ele in list4]
    # list3 = [ele for ele in list3 if ele in list4]

    # print(list3)
    # print(list2)
    # print(list1)

    # print("distance {0}".format(len(distance)))

    print("Total \n")

    # for d in distance:
    #     print(d.clasz)
    #     print(d.coeficient)

    knn = Knn()
    nmin = knn.NminElements(distance, 5)

    fileNames = sorted(glob2.glob("./docs/**/*.txt"))

    classes = []
    for fileName in fileNames:
        clasz = fileName.split("/")[2]
        if clasz not in classes:
            classes.append(clasz)

    rt = Rating()
    rt.set_class_predict("Analyze")

    # print("3 mais proximo")

    file_names_ne = []
    for nearest in nmin:
        print(nearest.clasz)
        print(nearest.coeficient)
        print(nearest.file)
        file_names_ne.append(nearest.file)

    print(rt.confusion_matrix(nmin, file_names_ne, classes))
    print("Precision value {0}".format(
        rt.precision_value(nmin, file_names_ne, classes)))
    print("Recall Score {0}".format(
        rt.recall_score(nmin, file_names_ne, classes)))
    print("F score {0}".format(
        rt.precision_recall_fscore_support(nmin, file_names_ne, classes)))

    # print("distance {0}".format(len(distance)))
    # for document in distance:
    #     print("Documento {0} distancia dos cossenos {1}  Classe {2}".format(
    #         document.file, document.coeficient, document.clasz
    #     ))

    # for document in distance:
    #     print(
    #         "Documento {0} distancia dos cossenos {1}  Classe {2}".format(
    #             document.file, document.coeficient, document.clasz
    #         )
    #     )

    # files = []
    # # 1 - Conjunto de dados curto
    # fileNames = sorted(glob2.glob("curto/*.txt"))
    # for filename in fileNames:
    #     files.append(open(filename, "r+").read())

    # serviceTextMining = ServiceTextMining()
    # print("Tópico 1 - Matrix TF * IDF")
    # terms = serviceTextMining.select_terms(files)
    # matriz_tf = serviceTextMining.create_matriz_itf_terms(terms)
    # matriz_df = serviceTextMining.create_matriz_idf_terms(terms, files)
    # matriz_tf_df = serviceTextMining.create_matriz_tf_df_terms(
    #     matriz_tf, matriz_df)

    # print("Criando arquivo csv")
    # csv_file = open("trabalho3.csv", "w+")
    # csv_manages = csv.writer(csv_file, delimiter=",",
    #                          quoting=csv.QUOTE_MINIMAL)
    # csv_file.write("@terms")
    # csv_file.write("\n")
    # csv_manages.writerow(terms)
    # csv_file.write("@matriz_tf")
    # csv_file.write("\n")
    # for line in range(len(matriz_tf)):
    #     csv_manages.writerow(matriz_tf[line])
    # csv_file.write("@matriz_df")
    # csv_file.write("\n")
    # csv_manages.writerow(matriz_df)
    # csv_file.write("@matriz_df_idf")
    # csv_file.write("\n")
    # for line in range(len(matriz_tf_df)):
    #     csv_manages.writerow(matriz_tf_df[line])

    # # Deve

    # # Com o	conjunto de	dados longo
    # query = "but kate's job  , if you will "

    # print(
    #     "Calculo distancia dos cossenos a partir de uma query = {0}".format(query))
    # distance = serviceTextMining.calc_distance_cosseno_in_query(query)

    # print("Tópico 2 - 10 Documentos mais relevantes")
    # nmax = serviceTextMining.Nmaxelements(distance, 10)

    # for document in nmax:
    #     print(
    #         "Documento {0} distancia dos cossenos {1}".format(
    #             document.file, document.coeficient
    #         )
    #     )
    # pdfOutput = PdfOutput(
    #     None,
    #     np.transpose(matriz_tf),
    #     matriz_df,
    #     np.transpose(matriz_tf_df),
    #     terms,
    #     fileNames,
    #     nmax,
    #     query,
    # )

    # servicePdfManager = ServiceManagerPdf()
    # servicePdfManager.writePdf(pdfOutput)


if __name__ == "__main__":
    main()
