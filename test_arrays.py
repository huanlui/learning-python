import pytest 

def test_un_array_se_imprime_correctamente_sin_necesidad_de_hacer_nada_mas_que_print() :
    arr = [4,5,6]
    print(arr)

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

def test_para_saber_si_un_elemento_esta_en_un_array_se_usa_in() :
    array = [1,2,3]

    assert 3 in array

def test_para_saber_si_un_elemento_NO_esta_en_un_array_se_usa_not_in() :
    array = [1,2,3]

    assert 4 not in array