import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
response = requests.get(BASE_URL)

if response.status_code == 200:
    print("Te has conectado de forma exitosa!!")
else:
    print("Error al conectarte a la web: ", response.status_code)

html = response.text


def buscar_elementos(html):
    # Obteniendo Titulo
    soup = BeautifulSoup(html, "html.parser")
    contenedor_libros = soup.find("div", class_="col-sm-8 col-md-9")
    contenedor_menu_libros = contenedor_libros.find("ol", class_="row")
    contenedor_titulo = contenedor_menu_libros.find("h3")
    titulo_a = contenedor_titulo.find("a")
    return titulo_a.get("title")


def main():
    titulo = buscar_elementos(html)
    print(titulo)


if __name__ == "__main__":
    main()
