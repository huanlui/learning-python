#https://www.w3schools.com/python/python_classes.asp

class Perro:
    nombre = "" #no se puede dejar vacío al parecer. 
    raza = ""

class PerroConConstructor:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza


def test_para_crear_una_instancia_de_una_clase_se_pone_sin_new():
    perro = Perro()

    perro.nombre= "Perro muchacho"

    assert perro.nombre == "Perro muchacho"

def test_el_constructor_es_init() :
    perro = PerroConConstructor("Ron","Pastor alemán")

    assert perro.nombre == "Ron"