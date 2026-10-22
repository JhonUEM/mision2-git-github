"""Funciones de evaluación sencillas. Amplía este archivo en tu rama."""


def contar_aciertos(valores_reales, valores_predichos):
    """Devuelve el número de coincidencias; exige listas del mismo tamaño."""
    if len(valores_reales) != len(valores_predichos):
        raise ValueError("Las listas deben tener la misma longitud")
    return sum(a == b for a, b in zip(valores_reales, valores_predichos))


def calcular_accuracy(valores_reales, valores_predichos):
    """Devuelve la proporción de aciertos, entre 0 y 1."""
    if len(valores_reales) == 0:
        raise ValueError("Las listas no pueden estar vacías")
    aciertos = contar_aciertos(valores_reales, valores_predichos)
    return aciertos / len(valores_reales)
