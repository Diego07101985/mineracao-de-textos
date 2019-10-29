
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import sys
import math
import warnings
import random
from itertools import islice
from scipy import spatial
from scipy.spatial import distance
from scipy.sparse import csc_matrix, SparseEfficiencyWarning
from metrics import Metrics
from collections import OrderedDict
from toolz import reduceby
from numpy.linalg import norm


style.use('ggplot')


class K_Means:
    def __init__(self, k):
        self.k_clusters = k

    # Calcule os centróides para os clusters, calculando a média de todos os pontos de dados que pertencem a cada cluster.
    def compute_centroids(self, lista_centroids):
        new_centroids = []

        print("Begin method compute ")
        for k, centroid in lista_centroids:

            total_distance_cossine = 0
            count_doc = 0
            distance_cossines = []

            for k, doc in lista_centroids:
                distance_cossines.append(doc[1].distance_cosine)
                total_distance_cossine += doc[1].distance_cosine

            mean = (total_distance_cossine / len(centroid))

            print("Centroid {0}".format(len(centroid)))
            print("total_distance_cossine {0}".format(total_distance_cossine))
            print("Mean {0}".format(mean))
            print("Distances {0}".format(distance_cossines))

            distance_mean = distance_cossines.index(
                min(distance_cossines, key=lambda x: abs(x - mean)))

            new_centroids.append(
                (distance_mean, centroid[distance_mean]))
        return new_centroids

    # Retona o index documento com o valor mas proximo do centroid
    def closest_document(self, documents, centroids):

        metric = Metrics()
        list_centroid = []
        list_closest = []
        best_document = ""
        best_index = 0

        documents_k = documents[:]

        print(len(centroids))
        # posso clusterizar
        for centroid in range(len(centroids)):
            list_closest = []
            lista_best_document = []
            for k, document in documents_k:
                distance_cosine = metric.get_cosine_distance(
                    centroids[centroid][1], document)

                list_closest.append(DocumentKmean(distance_cosine, document))

            list_centroid.append((centroids[centroid][0], list_closest))

        for index_lista in range(len(list_centroid)):
            if len(lista_best_document) == 0:
                lista_best_document = [
                    doc.distance_cosine for doc in list_centroid[index_lista][1]]
            else:
                lista_best_document = [max(value) for value in np.array(list(zip([doc.distance_cosine for doc in list_centroid[index_lista][1]], [
                    distance_cosine for distance_cosine in lista_best_document])))]

        list_distance = [
            doc.distance_cosine for doc in list_centroid[2][1]]
        for k in range(len(list_centroid)):
            array_remove = []
            for index in range(len(lista_best_document)):
                if lista_best_document[index] > list_centroid[k][1][index].distance_cosine:
                    array_remove.append(index)
            for index in sorted(array_remove, reverse=True):

                del list_centroid[k][1][index]

        print("Lista centroid 2 = {0}".format(len(list_centroid)))
        # posso clusterizar

        return list_centroid

    def execute(self, matriz_t_idf):
        # reading input parameters

        self.clusters = {}

        document_vectors_list = []

        document_id = 0
        for line in range(len(matriz_t_idf)):

            document_vector = []
            for column in matriz_t_idf[line]:
                document_vector.append(column)

            document_vectors_list.append((document_id, document_vector))
            document_id += 1

        initial_centroids = random.sample(document_vectors_list, k=3)

        print(len(initial_centroids))

        temp_dist = 1.0
        metrics = Metrics()

        while temp_dist > 0.1:
            list_centroids = self.closest_document(
                document_vectors_list, initial_centroids)
            # Calcule os centróides para os clusters, calculando a média de todos os pontos de dados que pertencem a cada cluster.
            print("Lis centroid in execute {0}".format(len(list_centroids)))
            new_clusters = self.compute_centroids(list_centroids)
            # some as distancias euclidianas dos novos clusters com os iniciais esse resultado tende a zero quando não ouver mas mudanças
            temp_dist = sum(metrics.get_eculedian_distance(
                initial_centroids[iK][1], d.document[1]) for (iK, d) in new_clusters)

            print("Temp dist {0}".format(temp_dist))

            for (iK, d) in new_clusters:
                initial_centroids[iK] = (iK, d.document)

        return list_centroids


class DocumentKmean:
    def __init__(self, distance_cosine, document):
        self.distance_cosine = distance_cosine
        self.document = document
