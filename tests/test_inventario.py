import pytest
from src.inventario import clasificar_stock, calcular_porcentaje_ocupacion


def test_stock_agotado():
    assert clasificar_stock(0, 20) == "AGOTADO"


def test_stock_critico():
    assert clasificar_stock(7, 20) == "CRITICO"


def test_stock_bajo():
    assert clasificar_stock(15, 20) == "BAJO"


def test_stock_normal():
    assert clasificar_stock(30, 20) == "NORMAL"


def test_stock_invalido():
    with pytest.raises(ValueError):
        clasificar_stock(-2, 20)





def test_ocupacion_normal():
    assert calcular_porcentaje_ocupacion(50, 200) == 25.0


def test_ocupacion_vacio_y_lleno():
    assert calcular_porcentaje_ocupacion(0, 200) == 0.0
    assert calcular_porcentaje_ocupacion(200, 200) == 100.0


def test_ocupacion_excedida():
    assert calcular_porcentaje_ocupacion(250, 200) == 125.0


def test_ocupacion_invalida():
    with pytest.raises(ValueError):
        calcular_porcentaje_ocupacion(-1, 100)
    with pytest.raises(ValueError):
        calcular_porcentaje_ocupacion(10, 0)