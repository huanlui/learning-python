import pytest 

#comentario de linea

""" comentario de bloque
  fin de comentario de bloque """

@pytest.mark.parametrize("texto,repetirVeces,resultadoEsperado", [
    ("hola",2,"holahola"), 
     ("mari",4,"marimarimarimari"),
    ("y",6,"yyyyyy"),
])
def test_los_bucles_for_son_como_foreachs_y_suelen_hacer_uso_del_metodo_range(texto,repetirVeces,resultadoEsperado) :
    resultadoObtenido = ""
    for _ in range(repetirVeces):
       resultadoObtenido += texto

    assert resultadoObtenido == resultadoEsperado
    
@pytest.mark.parametrize("texto,repetirVeces,resultadoEsperado", [
    ("hola",2,"holahola"), 
     ("mari",4,"marimarimarimari"),
    ("y",6,"yyyyyy"),
])
def test_tambien_se_podria_haber_hecho_con_un_while(texto,repetirVeces,resultadoEsperado) :
    resultadoObtenido = ""
    vez = 0
    while vez < repetirVeces:
        resultadoObtenido += texto
        vez+= 1

    assert resultadoObtenido == resultadoEsperado    

def test_para_recorrer_un_array_sin_indice_lo_mas_facil_es_esto() :
    todosPar = [2,4,6,8,10]

    for valor in todosPar:
        assert valor % 2 == 0

def test_para_recorrer_un_array_con_indice_lo_mas_facil_es_esto() :
    todosPar = [2,4,6,8,10]

    for indice in range(len(todosPar)):
        assert todosPar[indice] % 2 == 0