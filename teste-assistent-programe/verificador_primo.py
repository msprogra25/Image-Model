"""
Função para verificar se um número é primo.
Um número primo é um número natural maior que 1 que possui apenas dois divisores: 1 e ele mesmo.
"""

def eh_primo(numero):
    """
    Verifica se um número é primo.
    
    Args:
        numero (int): O número a ser verificado
        
    Returns:
        bool: True se o número é primo, False caso contrário
        
    Examples:
        >>> eh_primo(7)
        True
        >>> eh_primo(10)
        False
        >>> eh_primo(1)
        False
    """
    
    # Validação: número deve ser inteiro
    if not isinstance(numero, int):
        raise TypeError("O número deve ser um inteiro")
    
    # Números menores ou iguais a 1 não são primos
    if numero <= 1:
        return False
    
    # 2 é o único número primo par
    if numero == 2:
        return True
    
    # Números pares maiores que 2 não são primos
    if numero % 2 == 0:
        return False
    
    # Verifica divisibilidade até a raiz quadrada do número
    # Se número não é divisível até sua raiz quadrada, é primo
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2  # Verifica apenas números ímpares
    
    return True


# Testes da função
if __name__ == "__main__":
    print("=" * 50)
    print("VERIFICADOR DE NÚMEROS PRIMOS")
    print("=" * 50)
    
    # Lista de números para testar
    numeros_teste = [1, 2, 3, 4, 5, 10, 11, 15, 17, 20, 29, 30, 97]
    
    print("\nTestando números:")
    for num in numeros_teste:
        resultado = "é primo" if eh_primo(num) else "NÃO é primo"
        print(f"{num:3d} {resultado}")
    
    print("\n" + "=" * 50)
    print("Entrada do usuário:")
    print("=" * 50)
    
    # Entrada do usuário
    try:
        entrada = int(input("\nDigite um número para verificar se é primo: "))
        
        if eh_primo(entrada):
            print(f"\n✓ O número {entrada} É PRIMO!")
        else:
            print(f"\n✗ O número {entrada} NÃO é primo")
            
    except ValueError:
        print("\nErro: Você deve digitar um número inteiro válido!")
    except TypeError as e:
        print(f"\nErro de tipo: {e}")
