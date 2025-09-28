import requests

url_usuarios = 'https://jsonplaceholder.typicode.com/users'
url_posts = 'https://jsonplaceholder.typicode.com/posts'

def get_usuarios():
    """
    Obtener los usuarios de la API (timeout 10s), en caso de error lanza la excepción HTTPError
    """
    respuesta = requests.get(url_usuarios, timeout=10)
    respuesta.raise_for_status()
    return respuesta.json()

def  get_posts():
    """
    Obtener los posts de la API (timeout 10s), en caso de error lanza la excepción HTTPError
    """
    respuesta = requests.get(url_posts, timeout=10)
    respuesta.raise_for_status()
    return respuesta.json()
