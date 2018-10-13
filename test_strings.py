import pytest 

@pytest.mark.parametrize("texto,longitudEsperada", [
    ("pacorr",6), 
     ("mari",4),
    ("",0),
])
def test_el_tamaño_de_un_texto_se_calcula_con_len(texto,longitudEsperada) :
    longitudObtenida = len(texto)
    assert longitudEsperada == longitudObtenida

def test_no_se_puede_calcular_el_tamaño_de_none() :
    with pytest.raises(Exception) as exception :
        print(exception)
        len(None)

def test_los_textos_tambien_se_pueden_tratar_como_arrays() :
    texto = "abcde"
    textoCortado = texto[1:4]

    assert textoCortado == "bcd"

def test_para_escoger_los_n_primeros_caracteres_hay_una_forma_comoda_que_funciona_incluso_con_textos_mas_cortos():
    textoLargo = "abcde"
    textoCorto = "ab"

    tresPrimerasLetrasTextoLargo = textoLargo[:3]
    tresPrimerasLetrasTextoCorto = textoCorto[:3]

    assert tresPrimerasLetrasTextoLargo == "abc"
    assert tresPrimerasLetrasTextoCorto == "ab"

def test_hay_una_forma_mas_facil_para_quedarse_con_los_n_ultimos_caracteres_de_un_texto():
    str = "abcde"
    con_forma_de_toda_la_vida = str[len(str) - 2:]
    con_forma_mejor = str[-2:]

    assert con_forma_de_toda_la_vida == "de"
    assert con_forma_mejor == "de"

def test_permite_interpolacion_desde_version_3_6() :
    nombre = "Paco"
    edad = 76
    saludo = f'Hola, soy {nombre}, y tengo sólo {edad} años'

    assert saludo == "Hola, soy Paco, y tengo sólo 76 años"

def test_como_en_javascript_se_puede_usar_comilla_doble_o_comilla_simple() :
    nombreConComillasDobles = "Paco"
    nombreConComillasSimples = 'Paco'

    assert nombreConComillasDobles == nombreConComillasSimples

def test_otra_forma_de_interpolar_algo_mas_incomoda_pero_compatible_con_versiones_anteriores() :
    nombre = "Paco"
    edad = 76
    saludo = 'Hola, soy %s, y tengo sólo %s años'%(nombre,edad)

    assert saludo == "Hola, soy Paco, y tengo sólo 76 años"

def test_tambien_se_pueden_nombrar_los_parametros_para_repetir_o_desprecouparse_del_orden_de_los_parametros() :
    nombre = "Paco"
    edad = 76
    saludo = 'Hola, soy {nombre}, sí {nombre}, y tengo sólo {edad} años'.format(edad=edad, nombre=nombre)

    assert saludo == "Hola, soy Paco, sí Paco, y tengo sólo 76 años"

