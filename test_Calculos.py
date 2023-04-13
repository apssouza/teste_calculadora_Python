from Calculos import Calculos

def test_Somar():
    calculo =Calculos(3,9)
    assert calculo.Somar() == 12

def test_Subtrair():
    calculo =Calculos(3,9)
    assert calculo.Subtrair() == 12

def test_Dividir():
    calculo =Calculos(9,3)
    assert calculo.Dividir() == 3

def test_Multiplicar():
    calculo =Calculos(3,9)
    assert calculo.Multiplicar() == 10