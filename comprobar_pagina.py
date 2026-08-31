from pypdf import PdfReader

pdf = PdfReader("input/pagina6.pdf")

print("Número de páginas:", len(pdf.pages))

texto = pdf.pages[0].extract_text()

print("Texto encontrado:")
print(repr(texto))