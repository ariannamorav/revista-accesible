from pypdf import PdfReader

pdf = PdfReader("input/pagina6.pdf")
pagina = pdf.pages[0]

recursos = pagina["/Resources"]
xobjects = recursos["/XObject"].get_object()

for nombre in ["/X31", "/X32"]:

    imagen = xobjects[nombre].get_object()

    datos = imagen.get_data()

    extension = ".jpg"

    if "/DCTDecode" not in imagen.get("/Filter", []):
        extension = ".bin"

    archivo = f"output/{nombre[1:]}{extension}"

    with open(archivo, "wb") as f:
        f.write(datos)

    print(f"Imagen extraída: {archivo}")