from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from urllib.request import urlopen
from pdfminer.pdfpage import PDFPage
from models import PdfOutput, HtmlPdf


class ServiceManagerPdf:
    def readPDF(self, arquivo_pdf):
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
            arquivo_pdf,
            pagenos,
            maxpages=maxpages,
            caching=caching,
            check_extractable=True,
        ):
            interpreter.process_page(page)

        arquivo_pdf.close()
        device.close()
        content = buffer.getvalue()

        buffer.close()
        return content

    def writePdf(self, pdfOutput):
        pdf = HtmlPdf(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font("Arial", size=18)
        pdf.cell(200, 10, txt="Trabalho 1 ", ln=1, align="C")
        pdf.set_font("Arial", size=14)

        pdf.cell(200, 10, txt="Texto", ln=1, align="C")

        epw = pdf.w - pdf.l_margin - pdf.r_margin
        eph = pdf.h - pdf.t_margin - pdf.b_margin

        pdf.rect(pdf.l_margin, pdf.t_margin, w=epw, h=eph)
        pdf.set_font("Times", "", 12)
        th = pdf.font_size

        pdf.ln(th)

        pdf.ln(2 * th)
        pdf.multi_cell(epw, th, txt="" + pdfOutput.texto)

        pdf.cell(
            200,
            10,
            txt="Total de palavras : " + str(pdfOutput.total_words),
            ln=1,
            align="C",
        )
        pdf.cell(
            200,
            10,
            txt="Total de Termos : " + str(pdfOutput.total_terms),
            ln=1,
            align="C",
        )

        pdf.set_font("Arial", size=16)
        pdf.cell(200, 10, txt="Tabela de Frequência de Termos ", ln=1, align="C")

        pdf.set_font("Arial", size=12)

        col_width = pdf.w / 4.5
        row_height = pdf.font_size

        table = """<table border="0" align="center" width="50%">
                        <thead><tr><th width="30%">Termos </th><th width="70%"> Total</th></tr></thead>
                        <tbody>"""

        for key in pdfOutput.data.keys():
            table += (
                "<tr><td width='30%' width='70%' >"
                + key
                + "</td><td '30%' width='70%'>"
                + str(pdfOutput.data.get(key))
                + "</td></tr>"
            )
        table += "</tbody></table>"
        pdf.write_html(table)
        pdf.output("trabalho1.pdf")
