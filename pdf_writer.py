from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from urllib.request import urlopen
from pdfminer.pdfpage import PDFPage


class ServiceExtractPdf:
    def __init__(self, arquivo_pdf):
        self.arquivo_pdf = arquivo_pdf

    def readPDF(self):
        resource = PDFResourceManager()
        buffer = StringIO()
        codec = "utf-8"
        layoutParams = LAParams()
        device = TextConverter(resource, buffer, codec=codec, laparams=layoutParams)

        maxpages = 0
        caching = True
        pagenos = set()
        interpreter = PDFPageInterpreter(resource, device)

        for page in PDFPage.get_pages(
            self.arquivo_pdf,
            pagenos,
            maxpages=maxpages,
            caching=caching,
            check_extractable=True,
        ):
            interpreter.process_page(page)

        self.arquivo_pdf.close()
        device.close()
        content = buffer.getvalue()

        buffer.close()
        return content
