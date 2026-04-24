NUMERO_PRIMO_MINIMO: int = 2


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo através de divisão por tentativa otimizada.
    
    Um número primo é aquele que possui exatamente dois divisores: 1 e ele mesmo.
    
    Algoritmo:
        1. Rejeita números menores que 2 (não são primos por definição)
        2. Aceita 2 (único número par primo)
        3. Rejeita outros números pares
        4. Testa divisibilidade por números ímpares até √n
    
    Args:
        numero (int): O número a ser verificado
    
    Returns:
        bool: True se é primo, False caso contrário
    
    Complexidade:
        - Tempo: O(√n) - verifica até a raiz quadrada
        - Espaço: O(1) - usa apenas variáveis locais
    
    Exemplos:
        >>> eh_primo(2)
        True
        >>> eh_primo(17)
        True
        >>> eh_primo(4)
        False
    """
    # Números menores que 2 não são primos
    if numero < NUMERO_PRIMO_MINIMO:
        return False
    
    # 2 é o único número par que é primo
    if numero == NUMERO_PRIMO_MINIMO:
        return True
    
    # Números pares maiores que 2 não são primos
    if numero % 2 == 0:
        return False
    
    # Verifica divisibilidade por números ímpares até √numero
    limite_verificacao = int(numero ** 0.5) + 1
    for divisor in range(3, limite_verificacao, 2):
        if numero % divisor == 0:
            return False
    
    return True


def executar_testes() -> None:
    """
    Executa suite de testes para a função eh_primo().
    
    Inclui testes de:
        - Separação de primos e não-primos
        - Casos críticos (números pequenos, pares, etc)
        - Validação contra valores esperados
    """
    NUMEROS_TESTE = [1, 2, 3, 4, 5, 10, 11, 13, 17, 20, 23, 25, 29, 30, 97, 100]
    
    print("=" * 50)
    print("TESTES DA FUNÇÃO eh_primo()")
    print("=" * 50 + "\n")
    
    # Teste 1: Exibir números primos
    _exibir_primos(NUMEROS_TESTE)
    
    # Teste 2: Exibir números não-primos
    _exibir_nao_primos(NUMEROS_TESTE)
    
    # Teste 3: Testes unitários com validação
    _executar_testes_unitarios()


def _exibir_primos(numeros: list[int]) -> None:
    """Exibe todos os números primos da lista."""
    primos = [num for num in numeros if eh_primo(num)]
    print(f"✓ Números Primos: {' '.join(map(str, primos))}\n")


def _exibir_nao_primos(numeros: list[int]) -> None:
    """Exibe todos os números não-primos da lista."""
    nao_primos = [num for num in numeros if not eh_primo(num)]
    print(f"✗ Números NÃO Primos: {' '.join(map(str, nao_primos))}\n")


def _executar_testes_unitarios() -> None:
    """Executa testes unitários com validação de resultados esperados."""
    casos_teste = [
        (1, False, "menor que 2"),
        (2, True, "único par primo"),
        (3, True, "pequeno primo"),
        (4, False, "par"),
        (10, False, "par"),
        (17, True, "primo"),
        (97, True, "primo grande"),
        (100, False, "par grande"),
    ]
    
    print("Testes Unitários:")
    print("-" * 50)
    
    testes_passaram = 0
    for numero, esperado, descricao in casos_teste:
        resultado = eh_primo(numero)
        passou = resultado == esperado
        
        if passou:
            testes_passaram += 1
            status = "✓ PASS"
        else:
            status = "✗ FAIL"
        
        print(f"{status} | eh_primo({numero:3d}) = {str(resultado):5s} | {descricao}")
    
    print("-" * 50)
    total = len(casos_teste)
    print(f"Resultado: {testes_passaram}/{total} testes passaram\n")


def verificar_numero_usuario() -> None:
    """
    Solicita ao usuário que insira um número e verifica se é primo.
    
    Valida a entrada do usuário e exibe o resultado de forma clara.
    """
    print("=" * 50)
    print("VERIFICADOR DE NÚMEROS PRIMOS")
    print("=" * 50 + "\n")
    
    while True:
        try:
            entrada = input("Digite um número inteiro (ou 'sair' para voltar): ").strip()
            
            # Permite que o usuário saia
            if entrada.lower() in ['sair', 'q', 'exit']:
                print("\nAté logo!\n")
                break
            
            # Converte para inteiro
            numero = int(entrada)
            
            # Verifica se é primo
            resultado = eh_primo(numero)
            
            # Exibe resultado formatado
            print()
            if resultado:
                print(f"✓ {numero} é um número PRIMO!")
            else:
                print(f"✗ {numero} NÃO é um número primo.")
            print()
            
        except ValueError:
            print("❌ Erro: Digite um número inteiro válido!\n")


def exibir_menu() -> str:
    """
    Exibe menu de opções para o usuário.
    
    Returns:
        str: A opção selecionada pelo usuário
    """
    print("\n" + "=" * 50)
    print("MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Executar testes automatizados")
    print("2 - Verificar se um número é primo")
    print("3 - Sair")
    print("=" * 50 + "\n")
    
    return input("Escolha uma opção (1, 2 ou 3): ").strip()


def main() -> None:
    """
    Função principal que gerencia o fluxo da aplicação.
    
    Oferece um menu para o usuário escolher entre execução de testes
    ou verificação individual de números.
    """
    while True:
        opcao = exibir_menu()
        
        if opcao == "1":
            executar_testes()
        elif opcao == "2":
            verificar_numero_usuario()
        elif opcao == "3":
            print("\nObrigado por usar o verificador de primos! 👋\n")
            break
        else:
            print("❌ Opção inválida! Por favor, escolha 1, 2 ou 3.\n")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
