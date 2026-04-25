"""
Módulo para análise estatística básica de lista de números.
Calcula total, média, máximo e mínimo.
"""

from typing import Tuple


def calcular_estatisticas(numeros: list) -> Tuple[int | float, float, int | float, int | float]:
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numeros (list): Lista com números para análise
        
    Returns:
        Tuple: (total, média, máximo, mínimo)
        
    Raises:
        ValueError: Se a lista estiver vazia
        TypeError: Se a lista contiver valores não numéricos
        
    Examples:
        >>> calcular_estatisticas([23, 7, 45, 2, 67, 12, 89, 34, 56, 11])
        (346, 34.6, 89, 2)
    """
    
    if not numeros:
        raise ValueError("A lista não pode estar vazia")
    
    if not all(isinstance(num, (int, float)) for num in numeros):
        raise TypeError("Todos os elementos devem ser numéricos")
    
    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    
    return total, media, maximo, minimo


def exibir_resultado(total: int | float, media: float, 
                      maximo: int | float, minimo: int | float) -> None:
    """
    Exibe os resultados da análise estatística de forma formatada.
    
    Args:
        total: Soma de todos os números
        media: Média aritmética
        maximo: Maior número
        minimo: Menor número
    """
    linha_separadora = "=" * 40
    
    print(linha_separadora)
    print("ANÁLISE ESTATÍSTICA")
    print(linha_separadora)
    print(f"Total:    {total}")
    print(f"Média:    {media:.2f}")
    print(f"Máximo:   {maximo}")
    print(f"Mínimo:   {minimo}")
    print(linha_separadora)


# Dados para análise
numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

# Cálculos
total, media, maximo, minimo = calcular_estatisticas(numeros)

# Exibição dos resultados
exibir_resultado(total, media, maximo, minimo)