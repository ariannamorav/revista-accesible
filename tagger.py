import json
import re
import pikepdf
from pikepdf import Dictionary, Array, Name, String


def construir_descripciones(datos):
    """
    Crea una descripción específica para cada imagen.
    """

    descripcion_x31 = (
        "Dos modelos muestran vestidos negros: "
        "una lleva el vestido ajustado del producto C "
        "y otra lleva el vestido semiajustado con detalles blancos "
        "del producto D."
    )

    descripcion_x32 = (
        "Vista posterior del vestido semiajustado negro del producto D, "
        "con detalles blancos en el escote y el borde inferior."
    )

    return descripcion_x31, descripcion_x32


def etiquetar_pagina(entrada, json_path, salida):

    # 1. Leer JSON

    with open(json_path, encoding="utf-8") as archivo:
        datos = json.load(archivo)

    descripcion_x31, descripcion_x32 = construir_descripciones(datos)

    print("Descripción X31:")
    print(descripcion_x31)

    print("\nDescripción X32:")
    print(descripcion_x32)

    # 2. Abrir PDF

    pdf = pikepdf.open(entrada)

    page = pdf.pages[0]

    # 3. Obtener contenido original

    contenido_original = page.Contents.read_bytes()

    contenido = contenido_original

    # 4. Agregar marcado a X31

    patron_x31 = rb"/X31\s+Do"

    reemplazo_x31 = (
        b"/Figure <</MCID 0>> BDC\n"
        b"/X31 Do\n"
        b"EMC"
    )

    contenido = re.sub(
        patron_x31,
        reemplazo_x31,
        contenido,
        count=1
    )

    # 5. Agregar marcado a X32

    patron_x32 = rb"/X32\s+Do"

    reemplazo_x32 = (
        b"/Figure <</MCID 1>> BDC\n"
        b"/X32 Do\n"
        b"EMC"
    )

    contenido = re.sub(
        patron_x32,
        reemplazo_x32,
        contenido,
        count=1
    )

    # 6. Guardar nuevo Content Stream

    page.Contents = pdf.make_stream(contenido)

    page.StructParents = 0

    # 7. Crear Figure para X31

    figure_x31 = pdf.make_indirect(
        Dictionary(
            Type=Name.StructElem,
            S=Name.Figure,
            Pg=page.obj,
            K=0,
            Alt=String(descripcion_x31)
        )
    )

    # 8. Crear Figure para X32

    figure_x32 = pdf.make_indirect(
        Dictionary(
            Type=Name.StructElem,
            S=Name.Figure,
            Pg=page.obj,
            K=1,
            Alt=String(descripcion_x32)
        )
    )

    # 9. Crear elemento Document

    document = pdf.make_indirect(
        Dictionary(
            Type=Name.StructElem,
            S=Name.Document,
            K=Array([
                figure_x31,
                figure_x32
            ])
        )
    )

    # 10. Relacionar figuras con Document

    figure_x31.P = document
    figure_x32.P = document

    # 11. Crear ParentTree

    parent_tree = Dictionary(
        Nums=Array([
            0,
            Array([
                figure_x31,
                figure_x32
            ])
        ])
    )

    # 12. Crear StructTreeRoot

    struct_root = pdf.make_indirect(
        Dictionary(
            Type=Name.StructTreeRoot,
            K=Array([document]),
            ParentTree=parent_tree,
            ParentTreeNextKey=1
        )
    )

    document.P = struct_root

    # 13. Configuración de accesibilidad

    pdf.Root.StructTreeRoot = struct_root

    pdf.Root.MarkInfo = Dictionary(
        Marked=True
    )

    pdf.Root.Lang = String("es-CO")

    # 14. Guardar

    pdf.save(salida)

    print("\nPDF accesible creado correctamente.")
    print(f"Archivo: {salida}")


if __name__ == "__main__":

    etiquetar_pagina(
        "input/pagina6.pdf",
        "data/pagina6.json",
        "output/pagina6_accesible.pdf"
    )