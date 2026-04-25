# Verificador de Números Primos

## O que é um número primo?

Um **número primo** é um número natural maior que 1 que possui exatamente dois divisores: 1 e ele mesmo.

**Exemplos:**
- **2, 3, 5, 7, 11, 13, 17, 19, 23, 29** são primos
- **1, 4, 6, 8, 9, 10** NÃO são primos

---

## Características da função

```python
def eh_primo(numero):
    """Verifica se um número é primo."""
```

### Parâmetros
- `numero` (int): O número a ser verificado

### Retorno
- `True` se o número é primo
- `False` se o número não é primo

### Validações
- ✓ Valida se a entrada é um inteiro
- ✓ Rejeita números menores ou iguais a 1
- ✓ Identifica 2 como único primo par

---

## Algoritmo

A função usa a estratégia **otimizada** de verificação:

1. Descarta números ≤ 1
2. Identifica 2 como primo
3. Descarta números pares
4. Verifica divisibilidade até √n (raiz quadrada)
5. Verifica apenas números **ímpares**

**Complexidade:** O(√n) - muito mais rápido que verificar todos os divisores!

---

## Exemplos de uso

### Teste simples
```python
eh_primo(7)   # True
eh_primo(10)  # False
eh_primo(1)   # False
```

### Com entrada do usuário
```python
numero = int(input("Digite um número: "))
if eh_primo(numero):
    print(f"{numero} é primo!")
else:
    print(f"{numero} não é primo!")
```

---

## Como executar

Terminal:
```bash
python verificador_primo.py
```

Isso executará:
- Testes automatizados com números de exemplo
- Solicita entrada do usuário
- Exibe o resultado

