import pikepdf

pdf = pikepdf.open("output/pagina6_accesible.pdf")

print("=== VERIFICACIÓN DE ACCESIBILIDAD ===")

# 1. MarkInfo
print("\nMarkInfo:")
print(pdf.Root.MarkInfo)

# 2. Idioma
print("\nIdioma:")
print(pdf.Root.Lang)

# 3. Árbol estructural
print("\nStructTreeRoot:")
print(pdf.Root.StructTreeRoot)

# 4. Buscar elementos Figure y mostrar Alt
print("\nTexto alternativo:")

struct_root = pdf.Root.StructTreeRoot
document = struct_root.K[0]

elementos = document.K

for i, elemento in enumerate(elementos):
    print(f"\nFigura {i + 1}:")
    print("Tipo:", elemento.S)
    print("Alt:", elemento.Alt)