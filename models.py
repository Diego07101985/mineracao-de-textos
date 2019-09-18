from fpdf import FPDF, HTMLMixin


class PdfOutput:
    def __init__(self, data, total_words, total_terms, texto):
        self.data = data
        self.total_words = total_words
        self.total_terms = total_terms
        self.texto = texto


class HtmlPdf(FPDF, HTMLMixin):
    pass

