from asyncio.windows_events import NULL
from escuela_api import api

def test_lista_estudiante():
    assert api.update_asistencia('1234567890') == '<h1>REGISTRO MODIFICADO POR Erick Gallegos</h1>'