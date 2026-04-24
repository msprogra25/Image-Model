# Explicação Técnica e Didática - Função eh_primo()
## Código Otimizado com Clean Code

---

## **TÉCNICAS DE CLEAN CODE APLICADAS**

### 1️⃣ **Type Hints (Anotações de Tipo)**
```python
def eh_primo(numero: int) -> bool:
```
- **`numero: int`** - Declara que o parâmetro deve ser inteiro
- **`-> bool`** - Declara que a função retorna um booleano
- **Benefício**: Melhor legibilidade e detecção de erros com ferramentas como `mypy`

### 2️⃣ **Constantes em MAIÚSCULAS**
```python
NUMERO_PRIMO_MINIMO: int = 2
```
- **Padrão PEP 8**: Constantes sempre em maiúsculas
- **Facilita manutenção**: Se precisar alterar o valor mínimo, há um único lugar de mudança
- **Documenta intenção**: Deixa claro que 2 é um valor fixo importante

### 3️⃣ **Names Descritivos**
```python
# ❌ Antes (confuso)
for i in range(3, int(numero ** 0.5) + 1, 2):

# ✅ Depois (claro)
limite_verificacao = int(numero ** 0.5) + 1
for divisor in range(3, limite_verificacao, 2):
```
- **`i` → `divisor`**: Nome que descreve o significado real da variável
- **`limite_verificacao`**: Explica por que calculamos a raiz quadrada

### 4️⃣ **Docstring Detalhada (PEP 257)**
```python
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
```
- **Descrição clara** do propósito e algoritmo
- **Exemplos práticos** (doctests)
- **Análise de complexidade** integrada na documentação
- **Facilita manutenção** e uso por outros desenvolvedores

### 5️⃣ **Separação de Responsabilidades (Single Responsibility Principle)**

#### Antes (código monolítico):
```python
# Tudo junto em if __name__ == "__main__"
# 50+ linhas de lógica de teste
```

#### Depois (funções coesas):
```python
def executar_testes() -> None:
    """Função principal que orquestra todos os testes"""
    
def _exibir_primos(numeros: list[int]) -> None:
    """Responsável apenas por exibir primos"""
    
def _exibir_nao_primos(numeros: list[int]) -> None:
    """Responsável apenas por exibir não-primos"""
    
def _executar_testes_unitarios() -> None:
    """Responsável apenas pelos testes de validação"""
```

- **`_` (underscore)**: Indica funções privadas (uso interno)
- **Cada função possui uma responsabilidade única**
- **Testes são reutilizáveis** em outros contextos

### 6️⃣ **List Comprehension (Pythônico)**

#### Antes:
```python
print("Números Primos encontrados:")
for num in numeros_teste:
    if eh_primo(num):
        print(f"  {num}", end=" ")
```

#### Depois:
```python
primos = [num for num in numeros if eh_primo(num)]
print(f"✓ Números Primos: {' '.join(map(str, primos))}\n")
```

- **Mais conciso** e legível
- **Mais eficiente** (operação em uma linha)
- **Idiomático Python** (Pythonic)

### 7️⃣ **Estrutura Visual Melhorada**

#### Separadores e Headers:
```python
print("=" * 50)
print("TESTES DA FUNÇÃO eh_primo()")
print("=" * 50 + "\n")
```

- **Mais fácil de ler** a saída
- **Profissional** e organizado

#### Alinhamento de Colunas:
```python
print(f"{status} | eh_primo({numero:3d}) = {str(resultado):5s} | {descricao}")
#                            ^^^                 ^^^
#                   Alinhamento de largura fixa (3 e 5 caracteres)
```

---

## **DEFINIÇÃO DA FUNÇÃO REFATORADA**

### Estrutura completa:
```python
NUMERO_PRIMO_MINIMO: int = 2

def eh_primo(numero: int) -> bool:
    """[docstring detalhada]"""
    
    # Condição 1
    if numero < NUMERO_PRIMO_MINIMO:
        return False
    
    # Condição 2
    if numero == NUMERO_PRIMO_MINIMO:
        return True
    
    # Condição 3
    if numero % 2 == 0:
        return False
    
    # Condição 4 (otimizada)
    limite_verificacao = int(numero ** 0.5) + 1
    for divisor in range(3, limite_verificacao, 2):
        if numero % divisor == 0:
            return False
    
    return True
```

### Melhorias aplicadas:
✅ Type hints na assinatura
✅ Constante para valor mágico
✅ Nomes descritivos (`divisor` em vez de `i`, `limite_verificacao` explícito)
✅ Docstring completa com exemplos
✅ Comentários apenas o necessário (o código fala por si)

---

## **TESTES REFATORADOS**

### Arquitetura:
```
executar_testes()  [Orquestrador principal]
    ├── _exibir_primos()
    ├── _exibir_nao_primos()
    └── _executar_testes_unitarios()
```

### Função `_executar_testes_unitarios()`:

**Antes (repetitivo):**
```python
casos_teste = [(1, False), (2, True), ...]
for numero, esperado in casos_teste:
    resultado = eh_primo(numero)
    status = "✓ PASS" if resultado == esperado else "✗ FAIL"
    print(f"  {status}: eh_primo({numero}) = {resultado}")
```

**Depois (profissional):**
```python
casos_teste = [
    (1, False, "menor que 2"),
    (2, True, "único par primo"),
    (3, True, "pequeno primo"),
    # ... mais casos
]

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

print(f"Resultado: {testes_passaram}/{total} testes passaram")
```

**Melhorias:**
- ✅ Cada teste tem uma descrição clara
- ✅ Contador de sucessos
- ✅ Alinhamento visual com formatação fixa
- ✅ Estatísticas finais

---

## **PONTO DE ENTRADA (Main Guard)**

```python
if __name__ == "__main__":
    executar_testes()
```

**Benefícios:**
- ✅ Permite importar `eh_primo()` sem executar testes
- ✅ Código apenas execute quando rodado diretamente
- ✅ Padrão Python profissional

---

## **RESUMO DAS TÉCNICAS DE CLEAN CODE APLICADAS**

| Técnica | Antes | Depois | Benefício |
|---------|-------|--------|-----------|
| **Type Hints** | `def eh_primo(numero):` | `def eh_primo(numero: int) -> bool:` | Melhor tipagem e IDE support |
| **Constantes** | `if numero < 2:` | Usa `NUMERO_PRIMO_MINIMO` | Fácil manutenção |
| **Nomes** | `for i in range(...)` | `for divisor in ...` | Legibilidade |
| **Docstring** | 5 linhas | 25 linhas | Documentação completa |
| **Funções** | 60 linhas de teste | 4 funções | Reutilização e testabilidade |
| **List Comp.** | Loop 4 linhas | `[... for ... if ...]` | Pythônico e eficiente |
| **UI** | Saída simples | Tabelas formatadas | Profissionalismo |

---

## **ANÁLISE DE COMPLEXIDADE**

| Aspecto | Valor |
|---------|-------|
| **Complexidade de tempo** | O(√n) |
| **Complexidade de espaço** | O(1) |
| **Operações de teste** | O(n × √max(n)) |

**Exemplo com otimizações:**
- Verificar 1.000.000: **~1.000 iterações** em vez de ~500.000
- Verificar 10^18: **~1 bilhão iterações** em vez de ~10^18

---

## **CONCLUSÃO**

O código refatorado exemplifica **best practices profissionais** em Python:
- 🎯 **Type Safe**: Anotações de tipo
- 📚 **Well Documented**: Docstrings detalhadas
- 🏗️ **Well Structured**: Separação de responsabilidades
- 🐍 **Pythonic**: Idiomas Python modernos
- 🧪 **Testable**: Funções independentes e reutilizáveis
- 📊 **Maintainable**: Código que se auto-documenta

Este é o padrão **production-ready** esperado em projetos profissionais!
