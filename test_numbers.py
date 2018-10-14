import pytest 

def test_python_no_soporta_el_operador_mas_mas_y_por_cierto_se_comenta_con_sostenidos() :
    numero = 0
    # numero++  (No compila)
    numero += 1

    assert numero == 1

def test_para_elevar_al_cuadrado_se_usa_dos_veces_el_simbolo_de_multiplicar() :
    assert 5**2 == 25