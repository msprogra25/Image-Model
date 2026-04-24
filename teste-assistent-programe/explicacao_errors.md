# 🔴 Explicação dos Erros Encontrados no Código

## **1. Falta de Aspas na String (Linha 4)**

### ❌ Código com Erro:
```python
item1 = float(input(Preço do item 1? ))
```

### ✅ Código Correto:
```python
item1 = float(input("Preço do item 1? "))
```

### 📝 Explicação:
- A função `input()` espera uma **string** como argumento (entre aspas)
- Sem as aspas, Python tenta interpretar `Preço do item 1?` como uma variável
- Isso gera um erro: `NameError: name 'Preço' is not defined`

---

## **2. Falta do Prefixo 'f' em f-string (Linha 30)**

### ❌ Código com Erro:
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

### ✅ Código Correto:
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

### 📝 Explicação:
- O prefixo `f` antes da string indica que é uma **f-string** (formatted string literal)
- Sem o `f`, as chaves `{}` são tratadas como texto literal, não como interpolação
- **Resultado com erro**: ` Item 2:        R$ {total_item2:.2f}`
- **Resultado correto**: ` Item 2:        R$ 150.00` (exemplo)

---

## **3. Indentação Incorreta no Bloco if (Linha 35)**

### ❌ Código com Erro:
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

### ✅ Código Correto:
```python
if desconto_cupom > 0: 
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

### 📝 Explicação:
- Em Python, **indentação é obrigatória** para blocos de código (if, for, while, etc.)
- O `print` deve estar indentado com 4 espaços ou 1 tab
- **Erro gerado**: `IndentationError: expected an indented block`

---

## **4. Conversão de Tipo Ausente (Linha 24)**

### ❌ Código com Erro:
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

### ✅ Código Correto:
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

### 📝 Explicação:
- A função `input()` **sempre retorna uma string**, nunca um número
- Na linha 24, `desconto_cupom` recebe uma string (ex: `"10"`)
- Na linha 25, tenta-se fazer operação matemática: `string / 100`
- **Erro gerado**: `TypeError: unsupported operand type(s) for /: 'str' and 'int'`
- **Solução**: Converter para `float()` na mesma linha do input

### ⚠️ Ponto Importante:
Todas as entradas com `input()` que envolvem operações matemáticas precisam ser convertidas:
- `int(input(...))` para números inteiros
- `float(input(...))` para números decimais
- `input(...)` pode ser usado apenas para texto

---

## ✅ Resumo das Correções:

| Linha | Erro | Solução |
|-------|------|---------|
| 4 | Falta de aspas | Adicionar `"` antes e depois da string |
| 24 | Sem conversão de tipo | Envolver com `float()` |
| 30 | Falta do `f` | Adicionar `f` antes das aspas |
| 35 | Indentação errada | Indentar com 4 espaços |

---

## 📌 Lições Aprendidas:

1. **Sempre use aspas** ao passar strings para funções
2. **`input()` retorna sempre string** - converta se precisar de número
3. **Use `f` para f-strings** quando interpolação de variáveis for necessária
4. **Indentação é obrigatória** em blocos condicionais/loops em Python
5. **Teste seu código** para verificar erros de sintaxe e lógica
