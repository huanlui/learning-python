import pytest 

def test_python_no_soporta_el_operador_mas_mas_y_por_cierto_se_comenta_con_sostenidos() :
    numero = 0
    # numero++  (No compila)
    numero += 1

    assert numero == 1

def test_para_elevar_al_cuadrado_se_usa_dos_veces_el_simbolo_de_multiplicar() :
    assert 5**2 == 25

def test_para_convertir_a_punto_flotante_se_usa_float_y_el_numero_entre_parentesis():
    assert float(2) == 2.0
    assert float("2.8") == 2.8

def test_para_convertir_a_entero_se_usa_int_y_el_numero_entre_parentesis_truncandose_al_numero_mas_bajo_si_el_numero_no_era_entero():
    assert int(2.8) == 2
    assert int("2") == 2

    with pytest.raises(ValueError): # no te trunca y te convierte del tiron desde string. 
        assert int("2.8") == 2

def test_para_convertir_un_numero_a_string_se_usa_str():
    assert str(2) == "2"
    assert str(2.8) == "2.8"