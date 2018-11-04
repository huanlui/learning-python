#https://www.w3schools.com/python/python_classes.asp

class Perro:
    nombre = "" #no se puede dejar vacío al parecer. 
    raza = ""

class PerroConConstructor:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

#Clase callable. Se trata como una función. Al ser casi como una función, también se podría nombrar mi_recta. 
class MiRecta:
    def __init__(self,ordenadaOrigen,pendiente):
        self.ordenadaOrigen = ordenadaOrigen
        self.pendiente = pendiente

    def __call__(self, x):
        y = self.ordenadaOrigen + self.pendiente * x

        return y


def test_para_crear_una_instancia_de_una_clase_se_pone_sin_new():
    perro = Perro()

    perro.nombre= "Perro muchacho"

    assert perro.nombre == "Perro muchacho"

def test_el_constructor_es_init() :
    perro = PerroConConstructor("Ron","Pastor alemán")

    assert perro.nombre == "Ron"

def test_las_clases_callables_son_como_funciones():
    recta = MiRecta(5,10)

    y_para_x_0 = recta(0)
    y_para_x_10 =  recta(10)

    assert y_para_x_0 == 5
    assert y_para_x_10 == 105