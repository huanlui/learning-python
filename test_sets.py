import pytest


def test_un_set_se_crea_con_llaves_y_no_se_puede_acceder_por_indice_a_sus_valores():
    miSet = {4,7,1}

    # miValor = miSet[0] da error. 

def test_se_puede_saber_el_numero_de_elementos_de_un_set_usando_len():
    miSet = {4,5,6}

    assert len(miSet) == 3

def test_se_puede_iterar_sobre_un_set_aunque_el_orden_no_esta_asegurado():
    miSet = {4,7,1}
    miArray = []
    for valor in miSet:
        miArray.append(valor)

    assert miArray != [4,7,1] # no sele en el orden esperado, porque los sets no aseguran orden
    assert 4 in miArray
    assert 7 in miArray
    assert 1 in miArray

def test_se_puede_comprobar_que_un_elemento_esta_en_un_set_usando_in():
    miSet = {4,5,6}

    assert 4 in miSet
    assert 8 not in miSet

def test_se_pueden_insertar_elementos_en_el_set_usando_add():
    miSet = {4,5,6}

    miSet.add(7)

    assert miSet == {4,5,6,7}

def test_si_inserto_un_elemento_ya_existente_no_hace_nada():
    miSet = {4,5,6}

    miSet.add(6)

    assert miSet == {4,5,6}    


def test_se_pueden_insertar_varios_elementos_del_tiron_en_un_set_usando_upadte():
    miSet = {4,5,6}

    miSet.update([7,8,9])

    assert miSet == {4,5,6,7,8,9}

def test_dos_sets_son_iguales_si_tienen_los_mismos_elementos_aunque_se_hayan_definido_en_distinto_orden():
    miSet = {4,5,6}

    assert miSet == {6,5,4}

def test_se_puede_usar_remove_para_eliminar_un_elemento_del_set():
    miSet = {4,5,6}

    miSet.remove(5)

    assert miSet == {4,6}

def test_se_puede_usar_tambien_discard_para_eliminar_un_elemento_del_set():
    miSet = {4,5,6}

    miSet.discard(5)

    assert miSet == {4,6}

def test_si_un_elemento_esta_repetido_en_el_set_entonces_es_como_si_solo_estuviera_una_vez():
    miSet = {6,6}

    assert miSet == {6}

def test_si_intento_borrar_un_elemento_que_no_existe_usando_remove_entonces_lanza_un_error():
    miSet = {4,5,6}

    with pytest.raises(KeyError):
        miSet.remove(7)

def test_si_intento_borrar_un_elemento_que_no_existe_usando_discard_entonces_NO_lanza_un_error():
    miSet = {4,5,6}

    miSet.discard(7)

def test_para_borrar_y_obtener_el_ultimo_elemento_del_set_se_usa_pop_aunque_no_sabremos_cual_es_porque_no_esta_orden():
    miSet = {4,5,6}

    unValorQueNoSeCualSera = miSet.pop()
    otroQueTampoco = miSet.pop()
    yEsteMenos = miSet.pop()

    assert len(miSet) == 0

def test_para_vaciar_un_set_se_usa_clear():
    miSet = {4,5,6}

    miSet.clear()

    assert len(miSet) == 0

def test_para_ver_si_un_set_esta_vacio_es_mejor_compararlo_con_set_que_contar_su_numero_de_elementos_por_cuestiones_de_rendimiento():
    miSet = {4}

    miSet.clear()

    # assert miSet == {}. Esto falla
    assert len(miSet) == 0 #Esto es lo más claro, pero podría tener peor rendimiento https://stackoverflow.com/a/21191329
    assert miSet == set() #Mejor rendimiento, según dicen en Stackoveflow, pero menos claro. 

def test_para_eliminar_definitivamente_un_set_se_usa_del():
    miSet = {4,5,6}

    del miSet
    
    with pytest.raises(UnboundLocalError): #está borrado => fallará cualquier uso de él
        miSet.add(7)

def test_se_puede_usar_tambien_el_propio_constructor_de_set_ojo_que_es_con_parentesis_no_con_llaves_o_corchetes():
    miSet = set((4,5,6))#doble paréntesis, al constructor le pasas una tupla, diría yo

    assert miSet == {4,5,6}
