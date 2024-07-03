import requests
from bs4 import BeautifulSoup

url = 'https://www.espn.com.co/'

# Encabezados HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Realizar la solicitud HTTP con los encabezados
response = requests.get(url, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer el texto de la página
    page_text = soup.get_text()

    # Guardar el texto en un archivo
    with open('page_content.txt', 'w', encoding='utf-8') as file:
        file.write(page_text)

    print("Contenido guardado en 'page_content.txt'")
else:
    print(f"Error {response.status_code}: No se pudo acceder a la página.")
