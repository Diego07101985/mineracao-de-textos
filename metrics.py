from scipy.spatial import distance
import math
import numpy as np


class Metrics:
    def get_euclidean_length(self, vector):
        euclidean_len = 0
        vector_array = vector.toarray()[0]
        for element in vector_array:
            euclidean_len += element ** 2
        return math.sqrt(euclidean_len)

    def get_cosine_distance(self, document_1, document_2):
        return 1 - distance.cosine(document_1, document_2)

    def get_eculedian_distance(self, document_1, document_2):
        return distance.euclidean(document_1, document_2)
