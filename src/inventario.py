def clasificar_stock(stock_actual: int, stock_minimo: int) -> str:
    if stock_actual < 0:
        raise ValueError("El stock actual no puede ser negativo")
    if stock_minimo <= 0:
        raise ValueError("El stock minimo debe ser mayor que cero")
    if stock_actual == 0:
        return "AGOTADO"
    if stock_actual <= stock_minimo * 0.5:
        return "CRITICO"
    if stock_actual <= stock_minimo:
        return "BAJO"
    return "NORMAL"



def calcular_porcentaje_ocupacion(stock_actual: int, capacidad_maxima: int) -> float:
    if stock_actual < 0:
        raise ValueError("El stock actual no puede ser negativo")
    if capacidad_maxima <= 0:
        raise ValueError("La capacidad maxima debe ser mayor que cero")
    return round(stock_actual / capacidad_maxima * 100, 2)
