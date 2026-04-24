def calculate_statistics(numbers):
    """
    Calcula a soma, média, valor máximo e mínimo de uma lista de números.
    
    Args:
        numbers: Lista de números para análise
        
    Returns:
        Tupla contendo (total, média, máximo, mínimo)
    """
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum


# Lista de dados para análise
data = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

# Executa o cálculo de estatísticas
total, average, maximum, minimum = calculate_statistics(data)

# Exibe os resultados
print(f"Total: {total}")
print(f"Média: {average:.2f}")
print(f"Maior: {maximum}")
print(f"Menor: {minimum}")