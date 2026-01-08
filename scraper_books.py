import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
puntuaciones = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

try:
    response = requests.get(BASE_URL)
    print("Te has conectado de forma exitosa!!")

except requests.exceptions.RequestException as e:
    print("Ocurrió un error al conectarte a la web: ", e)
    exit()

html = response.text


def buscar_elementos(html):
    # Array que contendrá el data frame
    result = []

    # Obteniendo bloque de libros
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
        try:
            # Obteniendo Titulo
            contenedor_titulo = element.find("h3")
            titulo_a = contenedor_titulo.find("a")
            titulo = titulo_a.get("title")

            # Obteniendo precio
            contenedor_precio = element.find("div", class_="product_price")
            precio_completo = contenedor_precio.find("p", class_="price_color")

            if precio_completo is None:
                precio = 0
            else:
                precio = float(precio_completo.get_text()[2:])

            # Obteniendo la puntuación
            elemento_puntuacion = element.find("p", class_="star-rating")
            puntuacion = puntuaciones[elemento_puntuacion.get("class")[1]]

            result.append(
                {"titulo": titulo, "precio": precio, "puntuacion": puntuacion}
            )

        except Exception as e:
            print(f"Error al procesar un libro individual: {e}")

    return result


def main():
    df_data = buscar_elementos(html)
    print(df_data)
    print(f"Total de libros procesados: {len(df_data)}")


if __name__ == "__main__":
    main()
