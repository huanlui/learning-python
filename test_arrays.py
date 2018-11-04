import pytest

def test_un_array_tambien_llamado_lista_se_imprime_correctamente_sin_necesidad_de_hacer_nada_mas_que_print() :
    arr = [4,5,6]
    print(arr)

def test_para_recorrer_un_array_en_modo_foreach_es_con_for() :
    arr = [4,4,4]

    for number in arr :
        assert number == 4

def test_para_recorrer_un_array_accediendo_a_indice_se_usa_la_utilidad_range_que_nunca_incluye_el_ultimo_numero() :
    arr = [0,1,2]

    for index in range(len(arr)):
        assert arr[index] == index

def test_para_crear_arrays_numericos_es_comodo_range_que_nunca_incluye_el_ultimo_numero():
    cuadrados = []
    for num in range(0,5) :
        cuadrados.append(num *num)
    
    assert cuadrados == [0,1,4,9,16]

def test_para_crear_una_proyeccion_de_un_array_se_usa_una_sintaxis_especial():
    cuadrados = [num * num for num in range(0,5)]

    assert cuadrados == [0,1,4,9,16]

def test_tambien_se_pueden_crear_proyecciones_de_otros_tipos():
    minusculas = ["paco", "pepe", "pedro", "pipi"]
    mayusculas = [nombre.upper() for nombre in minusculas]

    assert mayusculas == ["PACO", "PEPE", "PEDRO", "PIPI"]

def test_las_tuplas_son_como_arrays_pero_inmutables():
    valores = (1,2,3)

    # valores[2] =5 Fallaría
    proyeccion = [x ** 2 for x in valores]

    assert proyeccion == [1,4,9]

@pytest.mark.parametrize("limit,expected_value", [
    (0,[]),
    (1,[4]),
    (2,[4,5]),
    (3,[4,5,6]),
    (4,[4,5,6,7]),
    (5,[4,5,6,7]),
])
def test_se_puede_coger_desde_el_inicio_de_un_array_hasta_un_indice_dado_NO_INCLUIDO_usando_los_dos_puntos(limit,expected_value) :
    arr = [4,5,6,7]

    assert arr[:limit] == expected_value

@pytest.mark.parametrize("limit,expected_value", [
    (0,[4,5,6,7]),
    (1,[5,6,7]),
    (2,[6,7]),
    (3,[7]),
    (4,[]),
])
def test_se_puede_coger_desde_un_indice_dado_INCLUIDO_hsata_el_final_del_array_usando_los_dos_puntos(limit,expected_value) :
    arr = [4,5,6,7]

    assert arr[limit:] == expected_value

@pytest.mark.parametrize("limit_left,limit_right,expected_value", [
    (0,0,[]),
    (0,1,[4]),
    (0,2,[4,5]),
    (0,3,[4,5,6]),
    (0,4,[4,5,6,7]),
    (1,1,[]),
    (1,2,[5]),
    (1,3,[5,6]),
    (1,4,[5,6,7]),
    (2,2,[]),
    (2,3,[6]),
    (2,4,[6,7]),
    (3,3,[]),
    (3,4,[7]),
])
def test_se_puede_coger_desde_un_indice_dado_hsata_el_final_del_array_usando_los_dos_puntos(limit_left,limit_right,expected_value) :
    arr = [4,5,6,7]

    assert arr[limit_left:limit_right] == expected_value

@pytest.mark.parametrize("first_array,second_array,expected_value", [
    ([],[],[]),
    ([],[1],[1]),
    ([1],[2],[1,2]),
    ([2],[1],[2,1]),
    ([1,2,3],[5,4,2],[1,2,3,5,4,2]),
    (["a"],["b"],["a","b"]),
    ([1],["a"],[1,"a"]),
])
def test_para_concaternar_dos_aray_se_usa_el_mas(first_array,second_array,expected_value) :
    assert first_array + second_array == expected_value

def test_da_igual_si_me_salgo_de_las_posiciones_del_array_python_te_lo_apaña() :
    array = [1,2,3]
    array2 = array[-5:80]

    assert array == array2

def test_para_añadir_elementos_al_final_de_un_array_se_usa_append() :
    array  = []

    array.append("a")
    array.append("b")

    assert array == ["a","b"]

def test_para_borrar_un_elemnto_por_indice_se_usa_del_o_pop() :
    array = ["hola","adios", "hasta luego"]

    del array[0]
    array.pop(0)

    assert array == ["hasta luego"]

def test_para_borrar_un_elemento_por_valor_se_usa_remove() :
    array = ["hola","adios", "hasta luego"]

    array.remove("hola")
    array.remove("adios")

    assert array == ["hasta luego"]

def test_para_saber_si_un_elemento_esta_en_un_array_se_usa_in() :
    array = [1,2,3]

    assert 3 in array

def test_para_saber_si_un_elemento_NO_esta_en_un_array_se_usa_not_in() :
    array = [1,2,3]

    assert 4 not in array

def test_para_coger_el_ulitmo_elemento_de_un_array_se_usa_menos_1():
    array = [1,2,3,4,5]

    assert array[-1] == 5

def test_los_arrays_se_copian_por_referencia() :
    array = [1,2,3,4,5]
    array2 = array

    array.remove(1)

    assert array2 == [2,3,4,5]

def test_para_hacerse_una_copia_de_un_array_lo_mas_facil_es_usar_los_dos_puntos() :
    array = [1,2,3,4,5]
    array2 = array[:]

    array.remove(1)

    assert array2 == [1,2 ,3,4,5]

def test_para_obtener_un_array_de_tuplas_a_partir_de_varios_arrays_se_usa_zip() :
    posiciones = [0,1,2,3,4]
    nombres = ["lunes", "martes", "miércoles", "jueves", "viernes", "este no estará porque es más grande"]

    zipped = zip(posiciones,nombres)

    zipped = sorted(zipped, key = lambda tupla : tupla[0]) #ordeno las tuplas por posición, porque zip te lo ordena como le da la gana

    assert zipped == [(0,"lunes"),(1,"martes"),(2,"miércoles"),(3, "jueves"),(4, "viernes")]

