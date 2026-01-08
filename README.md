# books-toscrape - Web Scraper

## Descripción

Proyecto creado para practicar la técnica del web scraping, usando una pagina destinada a ese fin (<https://books.toscrape.com>)

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
  git clone <https://github.com/tachyon-lhc/books-toscrape>
  python -m venv
  pip install requirements.txt
```

## Uso

```bash
  python scraper_books.py
```

## Resultado

El script genera un archivo `data.csv` con las siguientes columnas:

- **titulo**: [descripción]
- **precio**: [descripción]
- **puntuacion**: [descripción]

## Estructura del proyecto

```
scraper-libros/
├── scraper_libros.py
├── data.csv
├── requirements.txt
└── README.md
```
