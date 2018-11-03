# http://book.pythontips.com/en/latest/lambdas.html
# http://mark-dot-net.blogspot.com/2014/03/python-equivalents-of-linq-methods.html

def test_python_permite_el_uso_de_lambdas() :
    suma = lambda x,y : x + y

    assert suma(1,2) == 3

def test_para_ordenar_se_usa_sort() :
    valores = [1,3,5,6,2]
    valores.sort()
    assert valores == [1,2,3,5,6]

def test_para_devolver_una_copia_ordenada_de_una_lista_sin_modificar_la_original_el_equivalente_es_sorted() :
    valores = [1,3,5,6,2]
    
    assert sorted(valores) == [1,2,3,5,6]
    assert valores == [1,3,5,6,2]


def test_para_ordenar_al_reves_se_usa_sort() :
    valores = [1,3,5,6,2]
    valores.sort(reverse=True)
    assert valores == [6,5,3,2,1]    

def test_se_puede_usar_una_funcion_lambda_para_decidir_como_se_ordena() :
    valores = ["casa", "a", "antoniopeña", "donaldo","vicentin"]
    deMenorAMayorNumeroDeLetras = lambda str : len(str)
    
    valores.sort(key=deMenorAMayorNumeroDeLetras)

    assert valores == ["a","casa","donaldo", "vicentin","antoniopeña"]

def test_se_puede_usar_una_funcion_lambda_para_decidir_como_se_ordena_tambien_para_reverse() :
    valores = ["casa", "a", "antoniopeña", "donaldo","vicentin"]
    deMenorAMayorNumeroDeLetras = lambda str : len(str)
    
    valores.sort(key=deMenorAMayorNumeroDeLetras, reverse=True)

    assert valores == ["antoniopeña", "vicentin","donaldo","casa","a"]