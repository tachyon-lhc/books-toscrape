# books-toscrape - Web Scraper

## Descripción

Proyecto creado para practicar la técnica del web scraping, usando una pagina destinada a ese fin ([books.toscrape.com](https://books.toscrape.com))

## Características

- Obtiene el titulo, precio, puntuación; de los libros
- Capacidad de iterar sobre multiples paginas del catalogo
- Manejo solido de errores mediante excepciones
- Almacenaje de data en un archivo csv

## Tecnologías

- Python 3.x
- requests
- beautifulsoup4
- pandas

## Instalación

```bash
  git clone https://github.com/tachyon-lhc/books-toscrape
  cd books-toscrape
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate  # Windows
  pip install -r requirements.txt
```

## Uso

```bash
  python scraper_books.py
```

## Resultado

El script genera un archivo `data.csv` con las siguientes columnas:

- **titulo**: Nombre completo del libro
- **precio**: Precio en libras esterlinas (£)
- **puntuación**: Rating del 1 al 5

### Ejemplo de salida en consola

```
Procesando pagina: 1
Te has conectado de forma exitosa!!
Procesando pagina: 2
Te has conectado de forma exitosa!!
...
Total de libros procesados: 1000
DataFrame guardado correctamente en: data.csv
```

## Estructura del proyecto

```
scraper-libros/
├── scraper_libros.py
├── data.csv
├── requirements.txt
└── README.md
```
