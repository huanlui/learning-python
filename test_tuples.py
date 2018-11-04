from pytest import raises
def test_las_tuplas_se_crean_con_parentesis_y_su_longitud_se_mide_tambien_con_len():
    tupla = ("Nacho","Juani")

    assert len(tupla) == 2

def test_las_tuplas_tambien_se_pueden_crear_usando_su_constrcutor_aunque_es_un_poco_mariconez_perdon_idiotez():
    tupla = tuple(("Ana", "Jose", "Nacho"))

    assert len(tupla) == 3

def test_las_tuplas_estan_ordenadas_y_para_acceder_a_un_elemento_por_indice_es_igual_que_con_las_listas():
    dictadores_del_mundo = ("Adolfo", "Benito", "Jose", "Francisco", "Hugo")

    assert dictadores_del_mundo[1] == "Benito"

def test_no_puedes_cambiar_el_valor_de_una_tupla_porque_las_tuplas_son_inmutables():
    palos = ("Oros", "Copas", "Espadas", "Bastos")

    with raises(TypeError):
        palos[1] = "Copazos"

def test_las_tuplas_se_recorren_como_cualquier_otra_coleccion():
    genios = ("Einstein", "Julio Iglesias", "José Carlos")
    vueltas = 0
    for _ in genios:
        vueltas += 1

    assert vueltas == 3

def test_para_comprobar_si_un_valor_esta_presente_en_una_tupla_se_usa_in_como_en_el_resto_de_colecciones():
    numeros = (4, 8, 15, 16, 23 ,42)

    assert 69 not in numeros

def test_para_eliminar_definitivamente_una_tupla_se_usa_del_como_con_el_resto_de_objetos():
    vas_a_ser_eliminada = (1,2,3)

    del vas_a_ser_eliminada

    with raises(UnboundLocalError):
        print(vas_a_ser_eliminada)
