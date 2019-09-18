import numpy as np
from nltk.tokenize import word_tokenize
from numpy import ndarray
import math


class ServiceTextMining:

    _docs = []

    def select_terms(self, files):
        array_terms = []
        self._docs = []

        for i in range(len(files)):
            base_text = files[i]
            if i > 0:
                terms = word_tokenize(base_text)
                self._docs.append(terms)
                for newterm in terms:
                    if newterm not in array_terms:
                        array_terms.append(newterm)
            else:
                terms = word_tokenize(base_text)
                self._docs.append(terms)
                for term in set(terms):
                    array_terms.append(term)

        return array_terms

    def create_matriz_binary_terms(self, terms):
        matriz_terms = []
        column = []

        for term in terms:
            for doc in self._docs:
                if term in doc:
                    column.append(1)
                else:
                    column.append(0)

            matriz_terms.append(column)
            column = []
        return np.transpose(matriz_terms)

    def cosine_similarity(self, files, matriz_terms):
        count_el_mtz = 0
        numerador = 0
        denominador = 0
        element = 0
        element2 = 0
        similaridade_cossenos = []

        while count_el_mtz < len(matriz_terms):
            first_doc = matriz_terms[count_el_mtz]

            if count_el_mtz + 1 < len(matriz_terms):
                second_doc = matriz_terms[count_el_mtz + 1]

                for indice_term in range(len(first_doc)):
                    numerador += first_doc[indice_term] * second_doc[indice_term]
                    element += math.pow(first_doc[indice_term], 2)
                    element2 += math.pow(second_doc[indice_term], 2)

                print(element)
                print(element2)
                denominador = math.sqrt(element) * math.sqrt(element2)
                similaridade_cossenos.append(numerador / denominador)

            count_el_mtz += 1

        return similaridade_cossenos

    def create_matriz_tf_terms(self, terms):
        matriz_terms = []
        column = []

        for term in terms:
            count_terms = 0
            for doc in self._docs:
                if term in doc:
                    column.append(sum([term == doc[i] for i in range(len(doc))]))
                else:
                    column.append(0)

            matriz_terms.append(column)
            column = []

        return np.transpose(matriz_terms)
