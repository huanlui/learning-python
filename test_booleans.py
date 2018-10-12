import pytest 

def test_los_nombres_de_los_booleanos_son_con_mayusculas() :
    valorVerdadero = True
    valorFalso = False    
    assert valorVerdadero 
    assert valorFalso != valorVerdadero

def test_para_negar_se_usar_not() :
    valorVerdadero = True
    valorFalso = False    
    assert valorVerdadero == (not valorFalso)
    assert valorFalso == (not valorVerdadero)

def test_para_hacer_or_se_pone_con_texto_tal_cual() :
    valorVerdadero = True
    valorFalso = False    
    assert (valorVerdadero or valorFalso) == True

def test_para_hacer_and_se_pone_con_texto_tal_cual() :
    valorVerdadero = True
    valorFalso = False    
    assert (valorVerdadero and valorFalso) == False

def test_en_python_tambien_existe_el_operador_elvis() :
    valorVerdadero = True
    valorFalso = False  
    texto1 = "Paco" if valorVerdadero else "Paco2"
    texto2 = "Bonito" if valorFalso else "Benito2"
    assert texto1 == "Paco" 
    assert texto2 == "Benito2"
