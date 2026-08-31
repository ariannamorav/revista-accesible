# Revista PDF Accesible

## Prototipo

El flujo desarrollado es:

```text
Revista PDF
     ↓
Seleccionar página
     ↓
Analizar contenido
     ↓
Identificar imágenes
     ↓
Extraer imágenes
     ↓
Definir textos ALT
     ↓
Organizar información en JSON
     ↓
Generar PDF accesible
     ↓
Verificar estructura
     ↓
Comparar visualmente
```

---

## Estructura del proyecto

```text
revista-accesible/
│
├── data/
│   └── pagina6.json
│
├── input/
│   ├── Revista_Prueba.pdf
│   └── pagina6.pdf
│
├── output/
│   ├── X31.jpg
│   ├── X32.jpg
│   ├── pagina6.png
│   ├── pagina6_accesible.pdf
│   ├── pagina6_accesible.png
│   └── pagina6_original.png
│
├── analizar_pagina.py
├── comprobar_json.py
├── comprobar_pagina.py
├── extraer_imagenes.py
├── extraer_pagina.py
├── tagger.py
├── ver_pagina.py
├── verificar_accesibilidad.py
│
├── .gitignore
└── requirements.txt
```

> El entorno virtual `venv/` no forma parte del repositorio.

---

## Tecnologías y herramientas

### Python

Lenguaje utilizado para desarrollar el proceso de análisis, extracción, generación y validación.

### pypdf

Utilizado para:

* Leer archivos PDF.
* Extraer texto.
* Obtener información de las páginas.
* Crear una copia de una página específica.
* Inspeccionar recursos del documento.

### pikepdf

Utilizado para trabajar con la estructura interna del PDF, incluyendo:

* `StructTreeRoot`
* `StructElem`
* `/Figure`
* `/Alt`
* `/MarkInfo`
* `/Lang`
* `ParentTree`

### pdf2image

Utilizado para convertir páginas PDF en imágenes y realizar comparaciones visuales.

### Pillow

Utilizado para trabajar con las imágenes obtenidas durante el proceso.

### Poppler

Herramienta externa utilizada en Windows para permitir el procesamiento de PDF mediante `pdf2image`.

### JSON

Utilizado para almacenar de forma estructurada la información de cada página.

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/ariannamorav/revista-accesible.git
```

Entrar al proyecto:

```bash
cd revista-accesible
```

Crear el entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual en Windows:

```powershell
venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución del prototipo

### 1. Extraer la página 6

```bash
python extraer_pagina.py
```

Este proceso genera una copia de trabajo de la página seleccionada.

### 2. Comprobar el texto

```bash
python comprobar_pagina.py
```

Permite comprobar que la página contiene texto extraíble.

### 3. Analizar los recursos gráficos

```bash
python analizar_pagina.py
```

Permite identificar los recursos gráficos existentes en la página.

### 4. Extraer las imágenes

```bash
python extraer_imagenes.py
```

Genera las imágenes individuales para su análisis.

### 5. Comprobar el JSON

```bash
python comprobar_json.py
```

Verifica que la información estructurada pueda ser leída correctamente.

### 6. Generar el PDF accesible

```bash
python tagger.py
```

Este es el programa principal del prototipo.

Genera:

```text
output/pagina6_accesible.pdf
```

### 7. Verificar la accesibilidad estructural

```bash
python verificar_accesibilidad.py
```

Permite comprobar:

```text
/Marked = True
Lang = es-CO
/Figure
/Alt
```

y verificar que los textos alternativos fueron almacenados.

### 8. Comparar visualmente

```bash
python ver_pagina.py
```

El prototipo utiliza un hash MD5 sobre las imágenes renderizadas para comprobar que la representación visual de la página original y la accesible sea idéntica.

Resultado obtenido en la prueba:

```text
Hash original : 7f4a5c7a4dc554c7bb74eab53c0dc251
Hash accesible: 7f4a5c7a4dc554c7bb74eab53c0dc251

¿Son visualmente idénticos?: True
```

---

## Ejemplo de textos ALT

se identificaron dos imágenes principales.

### X31

```text
Dos modelos muestran vestidos negros: una lleva el vestido ajustado del producto C y otra lleva el vestido semiajustado con detalles blancos del producto D.
```

### X32

```text
Vista posterior del vestido semiajustado negro del producto D, con detalles blancos en el escote y el borde inferior.
```
