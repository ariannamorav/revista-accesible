from pypdf import PdfReader, PdfWriter

entrada = "input/Revista_Prueba.pdf"
salida = "input/pagina6.pdf"

reader = PdfReader(entrada)
writer = PdfWriter()

# Extraer la página 6
writer.add_page(reader.pages[5])

with open(salida, "wb") as f:
    writer.write(f)

print("Página 6 extraída correctamente.")

