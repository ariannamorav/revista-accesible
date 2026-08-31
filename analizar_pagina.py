from pypdf import PdfReader

pdf = PdfReader("input/pagina6.pdf")
pagina = pdf.pages[0]

recursos = pagina.get("/Resources")

print("=== OBJETOS GRÁFICOS ===")

xobjects = recursos.get("/XObject")

if xobjects:
    for nombre, referencia in xobjects.items():
        objeto = referencia.get_object()

        print("\nNombre:", nombre)
        print("Tipo:", objeto.get("/Subtype"))
        print("Ancho:", objeto.get("/Width"))
        print("Alto:", objeto.get("/Height"))
        print("Filtro:", objeto.get("/Filter"))
else:
    print("No hay XObject.")