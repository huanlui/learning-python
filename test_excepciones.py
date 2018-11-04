import pytest

class MiExceptionPersonalizada(Exception): # así se declara que extiende 
    def __init__(self,message,codigoPersonalizado):
        super().__init__(message)

        self.codigoPersonalizado = codigoPersonalizado

def test_para_lanzar_una_excepion_se_usa_raise():
    with pytest.raises(MiExceptionPersonalizada) as excepcion_info:
        raise(MiExceptionPersonalizada("Hola", 33))

    assert excepcion_info.value.codigoPersonalizado == 33
    assert str(excepcion_info.value) == "Hola"
    

def test_para_capturar_cualquier_excepcion_se_usan_bloques_try_except():
    entroEnExcept = False
    try:
        print(1 / 0)
    except:
        entroEnExcept = True
        print("Ha habido una excepcion")

    assert entroEnExcept

def test_puede_haber_varios_bloques_except_para_tratar_distintos_tipos_de_excepciones():
    seHaMetidoEnElPrimerExcept = False
    try:
        raise(MiExceptionPersonalizada("Hola",35))
    except MiExceptionPersonalizada:
        seHaMetidoEnElPrimerExcept = True
    except:
        print("Error inesperado")

    assert seHaMetidoEnElPrimerExcept

def test_se_puede_obtener_la_excepcion_lanzada_para_tratarla_adecuadamente():
    codigoLanzado = 0
    try:
        raise(MiExceptionPersonalizada("Hola",69))
    except MiExceptionPersonalizada as miException:
        codigoLanzado = miException.codigoPersonalizado

    assert codigoLanzado == 69

def test_existe_el_bloque_else_para_ejecutar_condigo_SI_NO_se_ha_lanzado_excepcion():
    meHeMetidoEnElElse = False
    try:
        print("Hola, no lanzao excepción, porque soy una inofensiva línea de print")
    except:
        print("No debería estar en esta línea")
    else:
        meHeMetidoEnElElse = True
    
    assert meHeMetidoEnElElse

def test_existe_el_bloque_finally_que_se_ejecuta_pase_lo_que_pase():
    meHeMetidoEnFinallyCuandoHayExcepcion = False

    try:
        print("Hola, no lanzao excepción, porque soy una inofensiva línea de print")
    except:
        print("No debería estar en esta línea")
    finally:
        meHeMetidoEnFinallyCuandoHayExcepcion = True

    meHeMetidoEnFinallyCuandoNOHayExcepcion = False

    try:
        print(1/0)
    except:
        print("Debería estar en esta línea")
    finally:
        meHeMetidoEnFinallyCuandoNOHayExcepcion = True
    
    assert meHeMetidoEnFinallyCuandoHayExcepcion
    assert meHeMetidoEnFinallyCuandoNOHayExcepcion

def test_se_pueden_combinar_except_else_y_finally():
    meHeMetidoEnExcept = False
    meHeMetidoEnElse = False
    meHeMetidoEnFinally = False

    try:
        print("Soy bueno y no lanzo excepciones")
    except:
        meHeMetidoEnExcept = True
    else:
        meHeMetidoEnElse = True
    finally:
        meHeMetidoEnFinally = True

    assert not meHeMetidoEnExcept
    assert meHeMetidoEnElse
    assert meHeMetidoEnFinally


