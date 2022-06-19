
import pytest
from Alquiler import Alquiler_km, Alquiler_Horas,Alquiler_Dia

def test_Alquiler_km():
    a = 10
    assert Alquiler_km(a) == 15
    
def test_Alquiler_Horas():
    #sin descuento
    horas = 1
    precio = 20
    assert Alquiler_Horas(horas,precio)==20

def test_Alquiler_Horas_Descuento():
    #cont descuento (10 horas + 1 hora gratis)
    horas = 21
    precio = 20
    assert Alquiler_Horas(horas,precio)==380

def test_Alquiler_dia_mas_D7():
    #descuento mas de una semana (18%) precio fijo es 5/hora por 24 horas  = 120 por dia 
    dias = 8
    # = (8*120)-((8*120)*0.18) => 960 - 172.8 => 787.2
    assert Alquiler_Dia (dias) == 787.2
    
def test_Alquiler_dia_mas_D5_A7():
    #descuento mas de 5 hasta 7 dias(15%) precio fijo es 5/hora por 24 horas  = 120 por dia 
    dias = 6
    # = (6*120)-((6*120)*0.15) => 720 - 108 => 612
    assert Alquiler_Dia (dias) == 612

def test_Alquiler_dia_mas_D2_A5():
    #descuento mas de 2 hasta 5 dias(10%) precio fijo es 5/hora por 24 horas  = 120 por dia 
    dias = 4
    # = (4*120)-((4*120)*0.15) => 480 - 48 => 432
    assert Alquiler_Dia (dias) == 432

def test_Alquiler_dia_Undia():
    dias = 1
    # = 1*120
    assert Alquiler_Dia (dias) == 120