import pytest 
from itertools import *

def test_existe_un_equivalente_al_all_de_linq():
    personas = ["Paco", "Wario", "Ana","Elsa", "Gema","Maradona"]

    assert all("a" in persona for persona in personas)


def test_existe_un_equivalente_al_any_de_linq():
    personas = ["Paco", "Wario", "Ana","Elsa", "Gema","Maradona"]

    assert any("W" in persona for persona in personas)

def test_existe_un_equivalente_al_max_de_linq():
    numeros = [1,5,6,99,12]

    assert max(numeros) == 99

def test_existe_un_equivalente_al_min_de_linq():
    numeros = [1,5,6,99,12]

    assert min(numeros) == 1

def test_las_funciones_de_iter_tools_devuelven_iterables_que_son_equivalentes_a_los_ienumerables():
    numeros = range(0,10)

    for numero in islice(numeros,2):
        print(numero)

def test_la_funcion_slice_si_la_pasas_un_indice_como_parametro_te_devuelve_desde_el_inicio_hasta_ese_indice_pasado() :
    numeros = range(0,10)

    assert list(islice(numeros,2)) == [0,1]  

def test_la_funcion_slice_si_la_pasas_dos_indices_como_parametros_el_primero_es_el_start_y_el_segundo_el_stop() :
    numeros = range(0,10)

    assert list(islice(numeros,2,4)) == [2,3] 

def test_la_funcion_slice_si_la_pasas_tres_indices_como_parametros_el_primero_es_el_start_el_segundo_el_stop_y_el_tercero_el_paso() :
    numeros = range(0,10)

    assert list(islice(numeros,2,8,2)) == [2,4,6]

def test_para_hacer_el_equivalente_a_first_se_usa_un_next():
    personas = ["Paco", "Wario", "Ana","Elsa", "Gema","Maradona"]

    primera_que_empieza_por_w = next(persona for persona in personas if persona.startswith("W"))

    assert primera_que_empieza_por_w == "Wario"

def test_para_el_count_se_puede_usar_un_sum() :
    personas = ["Paco", "Wario", "Ana","Elsa", "Gema","Maradona"]

    personas_que_acaban_por_a = sum(1 for persona in personas if persona.endswith("a"))

    assert personas_que_acaban_por_a == 4

def test_para_hacer_una_proyeccion_equivalante_a_select_se_usa_map() :
    personas = ["Paco", "Wario", "Ana","Elsa", "Gema","Maradona"]

    numeros_de_letras =  map(lambda persona : len(persona),personas)

    assert list(numeros_de_letras) == [4,5,3,4,4,8]

def test_para_hacer_un_filtrado_equivalente_a_where_se_usa_filter() :
    personas = ["Paco", "Wario", "Ana","Elsa", "Gema","Maradona"]

    personas_con_menos_de_5_letras = filter(lambda persona : len(persona) < 5, personas)

    assert list(personas_con_menos_de_5_letras) == ["Paco", "Ana", "Elsa", "Gema"]

def test_para_hacer_un_groupby_antes_es_necesario_haber_ordenado_por_la_clave_del_grupo():
    personas = ["Paco", "Wario", "Ana","Elsa", "Gema","Maradona"]
    funcionAgrupacion = lambda persona : len(persona)

    personas_ordenadas_por_numero_de_letras = sorted(personas, key = funcionAgrupacion)

    personas_agrupadas_por_numero_de_letras = groupby(personas_ordenadas_por_numero_de_letras, key=funcionAgrupacion)

    personas_agrupadas_por_numero_de_letras_en_array = [ [clave, list(valores)] for clave, valores in personas_agrupadas_por_numero_de_letras]
    print(personas_agrupadas_por_numero_de_letras_en_array)

    assert personas_agrupadas_por_numero_de_letras_en_array[0][0] == 3
    assert list(personas_agrupadas_por_numero_de_letras_en_array[0][1]) == ["Ana"]
    assert personas_agrupadas_por_numero_de_letras_en_array[1][0] == 4
    assert list(personas_agrupadas_por_numero_de_letras_en_array[1][1]) == ["Paco", "Elsa", "Gema"]
    assert personas_agrupadas_por_numero_de_letras_en_array[2][0] == 5
    assert list(personas_agrupadas_por_numero_de_letras_en_array[2][1]) == ["Wario"]
    assert personas_agrupadas_por_numero_de_letras_en_array[3][0] == 8
    assert list(personas_agrupadas_por_numero_de_letras_en_array[3][1]) == ["Maradona"]


class MiIterable:
        def __iter__(self):
                self.valorActual = 0
                return self
        
        def __next__(self) :
                if(self.valorActual == 5) : raise StopIteration #Esto indica que acaba la iteracion

                self.valorActual += 1
                return self.valorActual


def test_he_definido_un_iterable_y_lo_uso() :
        miIterable = MiIterable()

        miArray = []

        for numero in miIterable:
                miArray.append(numero)

        assert miArray == [1,2,3,4,5]




