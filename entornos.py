import unittest
import json
import os
from io import StringIO
from unittest.mock import patch

from test_libreria import Libreria
    
class TestLibreria(unittest.TestCase):
    def setUp(self):
        self.libreria = Libreria()

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

if __name__ == '__main__':
    unittest.main()
