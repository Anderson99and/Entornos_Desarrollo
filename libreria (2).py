import json

class Libreria:
    def __init__(self):
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"

import unittest
import json
import os
from unittest.mock import patch

class Libreria:
    """
    Una clase para representar una biblioteca de libros.

    Atributos:
        libros (list): Una lista de diccionarios que representan los libros en la biblioteca.
    """

    def __init__(self):
        """Inicializa una nueva instancia de la clase Libreria con una lista vacía de libros."""
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un libro a la biblioteca.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            genero (str): El género del libro.
            anio (int): El año de publicación del libro.

        Returns:
            str: Un mensaje indicando que el libro ha sido añadido.
        """
        self.libros.append({
            'titulo': titulo,
            'autor': autor,
            'genero': genero,
            'anio': anio
        })
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.

        Args:
            titulo (str): El título del libro a buscar.

        Returns:
            list: Una lista de libros que coinciden con el título buscado.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por autor.

        Args:
            autor (str): El autor de los libros a buscar.

        Returns:
            list: Una lista de libros que coinciden con el autor buscado.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro por su título.

        Args:
            titulo (str): El título del libro a eliminar.

        Returns:
            str: Un mensaje indicando si el libro fue eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la lista de libros en un archivo JSON.

        Args:
            archivo (str): El nombre del archivo donde se guardarán los libros.

        Returns:
            str: Un mensaje indicando que los libros han sido guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga la lista de libros desde un archivo JSON.

        Args:
            archivo (str): El nombre del archivo desde donde se cargarán los libros.

        Returns:
            str: Un mensaje indicando que los libros han sido cargados o si el archivo no fue encontrado.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"

class TestLibreria(unittest.TestCase):
    def setUp(self):
        self.libreria = Libreria()

    def test_anadir_libro(self):
        self.libreria.anadir_libro("1984", "George Orwell", "Distopia", 1949)
        self.assertEqual(len(self.libreria.libros), 1)
        self.assertEqual(self.libreria.libros[0]['titulo'], "1984")

    def test_buscar_libro(self):
        self.libreria.anadir_libro("1984", "George Orwell", "Distopia", 1949)
        resultado = self.libreria.buscar_libro("1984")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['titulo'], "1984")

    def test_buscar_por_autor(self):
        self.libreria.anadir_libro("1984", "George Orwell", "Distopia", 1949)
        self.libreria.anadir_libro("Animal Farm", "George Orwell", "Satira", 1945)
        resultado = self.libreria.buscar_por_autor("George Orwell")
        self.assertEqual(len(resultado), 2)

    def test_eliminar_libro(self):
        self.libreria.anadir_libro("1984", "George Orwell", "Distopia", 1949)
        self.libreria.eliminar_libro("1984")
        self.assertEqual(len(self.libreria.libros), 0)

    def test_guardar_libros(self):
        self.libreria.anadir_libro("1984", "George Orwell", "Distopia", 1949)
        self.libreria.guardar_libros('test_libreria.json')
        with open('test_libreria.json', 'r') as f:
            datos = json.load(f)
        self.assertEqual(len(datos), 1)
        self.assertEqual(datos[0]['titulo'], "1984")
        os.remove('test_libreria.json')

    def test_cargar_libros(self):
        libros_data = [{'titulo': "1984", 'autor': "George Orwell", 'genero': "Distopia", 'anio': 1949}]
        with open('test_libreria.json', 'w') as f:
            json.dump(libros_data, f)
        self.libreria.cargar_libros('test_libreria.json')
        self.assertEqual(len(self.libreria.libros), 1)
        self.assertEqual(self.libreria.libros[0]['titulo'], "1984")
        os.remove('test_libreria.json')

    def test_cargar_libros_archivo_no_encontrado(self):
        resultado = self.libreria.cargar_libros('no_existe.json')
        self.assertEqual(resultado, "Archivo no encontrado")

if __name__ == '__main__':
    unittest.main()

mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))