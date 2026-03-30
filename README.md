# Laboratório 6 – Tokenização BPE e WordPiece

## Objetivo

Este laboratório teve como objetivo compreender e implementar algoritmos de tokenização baseados em sub-palavras, fundamentais para modelos de linguagem modernos. Foram abordados dois métodos principais:

* Byte Pair Encoding (BPE) – implementado do zero
* WordPiece – explorado com a biblioteca Hugging Face

---

## Tarefa 1: Motor de Frequências

Foi implementada a função `get_stats(vocab)`, responsável por:

* Percorrer o vocabulário
* Identificar pares adjacentes de símbolos
* Contar a frequência de cada par

### Resultado esperado

O par `('e', 's')` apresentou frequência máxima de 9, confirmando a correta implementação.

---

## Tarefa 2: Loop de Fusão (BPE)

Foram implementados:

### Função `merge_vocab(pair, vocab)`

* Substitui ocorrências do par mais frequente por um novo token unificado

### Loop de treinamento

* Executado por 5 iterações (K = 5)
* Em cada iteração:

  * Identifica o par mais frequente
  * Realiza a fusão
  * Atualiza o vocabulário

### Resultado observado

Ao final das iterações, surgem tokens com significado morfológico, como:

* est</w>

Isso demonstra que o algoritmo aprende padrões frequentes da língua.

---

## Tarefa 3: WordPiece com Hugging Face

Foi utilizado o tokenizador multilíngue:

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
```

### Frase analisada

```
Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar.
```

### Resultado

A frase foi dividida em sub-palavras (tokens), incluindo partes como:

* ##mente
* ##cional
* hiper
* parâmetros

---

## Explicação: O que significa "##"?

Os prefixos ## indicam que aquele token é uma continuação de uma palavra anterior, e não o início de uma nova palavra.

### Exemplo

```
inconstitucionalmente → in + constitucional + ##mente
```

### Por que isso é importante?

* Permite lidar com palavras desconhecidas
* Evita falhas do modelo (out-of-vocabulary)
* Reduz o tamanho do vocabulário
* Melhora a generalização

---

## Tecnologias utilizadas

* Python
* Biblioteca transformers (Hugging Face)

---

## Como executar

1. Instale as dependências:

```
pip install transformers
```

2. Execute o script Python:

```
python main.py
```

---

## Observações

* O algoritmo BPE foi implementado manualmente para fins educacionais
* O WordPiece foi utilizado via biblioteca para simular uso industrial

---

## Versão

v1.0

---
