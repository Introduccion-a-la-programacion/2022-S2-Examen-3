import Examen3;
import pytest;


def test_esVectorOrdenado_1():
    assert Examen3.esVectorOrdenado([23, 656, 5533, 8120], 'asc') == True
def test_esVectorOrdenado_2():
    assert Examen3.esVectorOrdenado([15, 4, 0], 'desc') == False
def test_esVectorOrdenado_3():
    assert Examen3.esVectorOrdenado([11, 45], 'desc') == True
    
    
def test_numeroAbundate_1():
    assert Examen3.numeroAbundante(12) == True
def test_numeroAbundate_2():
    assert Examen3.numeroAbundante(8) == False
def test_numeroAbundate_3():
    assert isinstance(Examen3.numeroAbundante(-8), str) == isinstance("Error: La entrada, debe ser número positivo", str)  
    
    
def test_lista_Duplex_1():
    assert Examen3.lista_Duplex([7, 20, 41, 82]) == True
def test_lista_Duplex_2():
    assert Examen3.lista_Duplex ([15, 29, 60]) == False
    
    
def test_centroMatriz_1():
    assert Examen3.centroMatriz(m1) == [[8,9], [14,15], [20,21]]
def test_centroMatriz_2():
    assert Examen3.centroMatriz(m2) == [[7,8,9], [13,14,15]]
