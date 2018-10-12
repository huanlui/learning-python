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
        len(None)

def test_los_textos_tambien_se_pueden_tratar_como_arrays() :
    texto = "abcde"
    textoCortado = texto[1:4]
    assert textoCortado == "bcd"
