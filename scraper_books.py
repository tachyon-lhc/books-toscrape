import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com"
puntuaciones = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def conectar_a_web(url):
    try:
        response = requests.get(url)
        print("Te has conectado de forma exitosa!!")
        return response.text

    except requests.exceptions.RequestException as e:
        print("Ocurrió un error al conectarte a la web: ", e)
        exit()


def extraer_titulo(element):
    # Obteniendo Titulo
    try:
        contenedor_titulo = element.find("h3")
        titulo_a = contenedor_titulo.find("a")
        titulo = titulo_a.get("title")
        return titulo

    except Exception as e:
        print(f"Error al procesar el titulo del libro: {e}")
        return


def extraer_precio(element):
    # Obteniendo Precio
    try:
        contenedor_precio = element.find("div", class_="product_price")
        precio_completo = contenedor_precio.find("p", class_="price_color")

        if precio_completo is None:
            precio = 0
        else:
            precio = float(precio_completo.get_text()[2:])

        return precio

    except Exception as e:
        print(f"Error al procesar el precio del libro: {e}")
        return


def extraer_puntuacion(element):
    # Obteniendo Puntuación
    try:
        elemento_puntuacion = element.find("p", class_="star-rating")
        puntuacion = puntuaciones[elemento_puntuacion.get("class")[1]]

        return puntuacion

    except Exception as e:
        print(f"Error al procesar la puntuacion del libro: {e}")
        return


def extraer_data(html, result):
    # Obteniendo bloque de libros
    libros_pagina = []
    soup = BeautifulSoup(html, "html.parser")
    try:
        contenedor_libros = soup.find("div", class_="col-sm-8 col-md-9")
        contenedor_menu_libros = contenedor_libros.find("ol", class_="row")

        # Obteniendo todos los contenedores de libros
        contenedor_libro_individual = contenedor_menu_libros.find_all(
            "article", class_="product_pod"
        )

    except Exception as e:
        print(f"Error al procesar el bloque de libros: {e}")
        exit()

    for element in contenedor_libro_individual:
        titulo = extraer_titulo(element)
        precio = extraer_precio(element)
        puntuacion = extraer_puntuacion(element)

        # Solo agregar si todos los datos son válidos
        if titulo and precio is not None and puntuacion:
            libros_pagina.append(
                {"titulo": titulo, "precio": precio, "puntuacion": puntuacion}
            )
        else:
            print("Libro incompleto detectado, se omite.")

    return libros_pagina


def guardar_en_csv(df):
    df_raw = pd.DataFrame(df)
    df_raw.to_csv("data.csv", index=False)
    print("DataFrame guardado correctamente en: data.csv")


def main():
    result = []

    for pagina in range(1, 51):  # De 1 a 50
        print(f"Procesando pagina: {pagina}")
        url = f"{BASE_URL}/catalogue/page-{pagina}.html"
        html = conectar_a_web(url)
        libros_pagina = extraer_data(html, result)
        result.extend(libros_pagina)
        time.sleep(1)

    guardar_en_csv(result)
    print(result)
    print(f"Total de libros procesados: {len(result)}")


if __name__ == "__main__":
    main()
