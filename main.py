from nltk.tokenize import word_tokenize
from nltk import FreqDist
from pdf_service_manager import ServiceManagerPdf
from models import PdfOutput

import csv
import string


def main():
    file_string = ""
    txt_file = open("trabalho1.txt", "r+")
    csv_file = open("trabalho1.csv", "w+")
    csv_manage = csv.writer(csv_file, delimiter=";", quoting=csv.QUOTE_MINIMAL)
    base_text = txt_file.read()
    sentences = word_tokenize(base_text)
    frequency = FreqDist(sentences)

    print("texto : {0}".format(base_text))

    print("Total de palavras : {0}".format(frequency.N()))
    print("Total de Termos : {0}".format(len(frequency.keys())))
    print("")

    print("Tabela de Frequência de Termos")
    print("")

    for key in frequency.keys():
        csv_manage.writerow([key, str(frequency.get(key))])
        print("Termo: {0}  Total: {1}".format(key, str(frequency.get(key))))

    pdfOutput = PdfOutput(frequency, frequency.N(), len(frequency.keys()), base_text)
    servicePdfManager = ServiceManagerPdf()
    servicePdfManager.writePdf(pdfOutput)

    txt_file.close()
    csv_file.close()


if __name__ == "__main__":
    main()
