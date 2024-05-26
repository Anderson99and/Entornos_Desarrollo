import json
import unittest


class Libreria:
    """
    Clase para gestionar una colección de libros en una librería virtual.
    """

    def __init__(self):
        """
        Inicializa una instancia de la clase Libreria con una lista vacía de libros.
        """
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un libro a la colección.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            genero (str): El género del libro.
            anio (int): El año de publicación del libro.

        Returns:
            str: Mensaje indicando que el libro ha sido añadido.
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
        Busca libros en la colección por su título.

        Args:
            titulo (str): El título del libro a buscar.

        Returns:
            list: Lista de libros que coinciden con el título proporcionado.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros en la colección por el autor.

        Args:
            autor (str): El autor del libro a buscar.

        Returns:
            list: Lista de libros que coinciden con el autor proporcionado.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def modificar_libro(self, titulo, nuevo_titulo=None, nuevo_autor=None, nuevo_genero=None, nuevo_anio=None):
        """
        Modifica la información de un libro existente en la colección.

        Args:
            titulo (str): El título del libro a modificar.
            nuevo_titulo (str, optional): El nuevo título del libro.
            nuevo_autor (str, optional): El nuevo autor del libro.
            nuevo_genero (str, optional): El nuevo género del libro.
            nuevo_anio (int, optional): El nuevo año de publicación del libro.

        Returns:
            str: Mensaje indicando si el libro ha sido modificado o no encontrado.
        """
        for libro in self.libros:
            if libro['titulo'].lower() == titulo.lower():
                if nuevo_titulo:
                    libro['titulo'] = nuevo_titulo
                if nuevo_autor:
                    libro['autor'] = nuevo_autor
                if nuevo_genero:
                    libro['genero'] = nuevo_genero
                if nuevo_anio:
                    libro['anio'] = nuevo_anio
                return "Libro modificado"
        return "Libro no encontrado"

    def eliminar_libro(self, titulo):
        """
        Elimina un libro de la colección por su título.

        Args:
            titulo (str): El título del libro a eliminar.

        Returns:
            str: Mensaje indicando si el libro ha sido eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la colección de libros en un archivo JSON.

        Args:
            archivo (str): El nombre del archivo donde se guardarán los libros.

        Returns:
            str: Mensaje indicando que los libros han sido guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga la colección de libros desde un archivo JSON.

        Args:
            archivo (str): El nombre del archivo desde donde se cargarán los libros.

        Returns:
            str: Mensaje indicando que los libros han sido cargados o que el archivo no fue encontrado.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


# Ejemplo de uso de la clase Libreria
mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))
