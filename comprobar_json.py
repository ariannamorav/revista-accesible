import json

with open("data/pagina6.json", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print("JSON leído correctamente.")
print("Página:", datos["pagina"])
print("Categoría:", datos["categoria"])
print("Precio:", datos["precio"])

print("\nProductos:")

for producto in datos["productos"]:
    print(
        f"- Producto {producto['codigo']}: "
        f"{producto['descripcion']} "
        f"Color: {producto['color']}"
    )