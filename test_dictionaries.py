def test_la_forma_de_crearse_diccionarios_es_parecida_a_javascript() :
    diccionario = {
        -2: "eagle",
        -1: "birdie",
        0 :"par",
        1: "bogey",
        2: "double bogey"
    }

    assert diccionario[1] == "bogey"

def test_para_añadir_itmes_a_un_diccionario_es_igual_que_en_javascript_o_cs() :
    diccionario = {
        -2: "eagle",
        -1: "birdie",
        0 :"par",
        1: "bogey",
        2: "double bogey"
    }

    diccionario[3] = "eres muy malo"

    assert diccionario[3] == "eres muy malo"

def test_para_recorrer_todas_las_claves_valor_de_un_diccionario_se_usa_items() :
    diccionario = {
        -2: "eagle",
        -1: "birdie",
        0 :"par",
        1: "bogey",
        2: "double bogey"
    }

    for clave, valor in diccionario.items() :
        assert valor == diccionario[clave]

def test_las_claves_de_un_diccionarios_se_obtienen_usando_keys():
    diccionario = {
        -2: "eagle",
        -1: "birdie",
        0 :"par",
        1: "bogey",
        2: "double bogey"
    }

    claves = []

    for key in diccionario.keys() :
        claves.append(key)

    assert claves == [-2,-1,0,1,2]

def test_los_valores_de_un_diccionarios_se_obtienen_usando_keys():
    diccionario = {
        -2: "eagle",
        -1: "birdie",
        0 :"par",
        1: "bogey",
        2: "double bogey"
    }

    valores = []

    for valor in diccionario.values() :
        valores.append(valor)

    assert valores == ["eagle","birdie","par","bogey","double bogey"]