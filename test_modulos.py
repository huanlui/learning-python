import mimodulo as modulo #el as es opcional, si no, se llamaría mimodulo tal cual
from mimodulo import unaFuncion

def test_se_pueden_usar_funciones_importadas_de_un_modulo():
    assert modulo.unaFuncion() == 5
    
def test_se_pueden_usar_las_variables_de_un_modulo():
    assert modulo.unObjeto["edad"] == 54

def test_usaando_from_mimodulo_import_unaFuncion_ya_tengo_esa_funcion_disponible_como_si_estuviera_definida_en_mi_propio_fichero():
    assert unaFuncion() == 5

def test_se_puede_imprimir_lo_que_un_modulo_tiene_usando_dir():
    contenido = dir(modulo)

    print(contenido)
    
    assert contenido == ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'unObjeto', 'unaFuncion']

