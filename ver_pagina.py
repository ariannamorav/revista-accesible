from pdf2image import convert_from_path
import hashlib


POPPLER_PATH = r"C:\Users\10\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"


def convertir(pdf, imagen):
    paginas = convert_from_path(
        pdf,
        dpi=150,
        poppler_path=POPPLER_PATH
    )

    paginas[0].save(imagen)

    return paginas[0]


def hash_imagen(imagen):
    return hashlib.md5(imagen.tobytes()).hexdigest()


# PDF original
original = convertir(
    "input/pagina6.pdf",
    "output/pagina6_original.png"
)

# PDF accesible
accesible = convertir(
    "output/pagina6_accesible.pdf",
    "output/pagina6_accesible.png"
)


print("=== COMPARACIÓN VISUAL ===")

hash_original = hash_imagen(original)
hash_accesible = hash_imagen(accesible)

print("Hash original :", hash_original)
print("Hash accesible:", hash_accesible)

print()
print("¿Son visualmente idénticos?:", hash_original == hash_accesible)