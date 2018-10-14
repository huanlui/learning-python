def test_si_intentamos_obtener_el_valor_de_una_llamada_a_una_funcion_que_no_tiene_return_entonces_obtenemos_None():
    valor = no_devuelve_nada()

    assert valor == None

def no_devuelve_nada():
    print("No tengo return, ergo no devuelvo nada")

def test_se_pueden_usar_parametros_por_defecto_es_una_funcion():
    assert repite_lo_que_te_he_dicho("hola") == "hola"
    assert repite_lo_que_te_he_dicho() == "No me has dicho nada, pájaro"

def repite_lo_que_te_he_dicho(valor = "No me has dicho nada, pájaro") :
    return valor

def test_se_puede_usar_argumentos_nombrados() :
    assert dame_un_punto(x=1,y=2) == [1,2]

def dame_un_punto(x,y):
    return [x,y]

def test_existe_un_equivalente_a_params_de_cs_en_python() :
    assert dame_array(1,2,3,4) == [1,2,3,4]

def dame_array(*valores) :
    result = []
    for valor in valores:
        result.append(valor)

    return result

def test_se_pueden_combinar_params_con_valores_fijos() :
    assert dame_array_2(1,2,3,valorFinal=4) == [1,2,3,4]


def dame_array_2(*valoresIniciales, valorFinal) :
    result = []
    for valor in valoresIniciales :
        result.append(valor)

    result.append(valorFinal)

    return result

def test_se_pueden_pasar_parametros_con_nombres_arbitrarios_que_posteriormente_se_pueden_tratar_como_un_diccionario_en_la_funcion():
    assert describeme_lo_que_me_has_pasado(nombre="Juan Luis", apellidos="García López") == "Me has pasado nombre = Juan Luis apellidos = García López"

    #además, desde python 3.6, el orden se conserva. Antes podía ser que no: http://treyhunner.com/2018/04/keyword-arguments-in-python/

def describeme_lo_que_me_has_pasado(**parametros):
    result = "Me has pasado"

    for param_name,param_value in parametros.items() :
        result += f" {param_name} = {param_value}"

    return result
