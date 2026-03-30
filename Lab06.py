# =========================
# Tarefa 1: get_stats
# =========================

def get_stats(vocab):
    pairs = {}
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i + 1])
            pairs[pair] = pairs.get(pair, 0) + freq
    return pairs


# =========================
# Tarefa 2: merge_vocab
# =========================

def merge_vocab(pair, v_in):
    v_out = {}
    bigram = " ".join(pair)
    replacement = "".join(pair)

    for word in v_in:
        # substitui ocorrências do par
        new_word = word.replace(bigram, replacement)
        v_out[new_word] = v_in[word]

    return v_out


# =========================
# Vocabulário inicial
# =========================

vocab = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}

# =========================
# Loop de Treinamento (K=5)
# =========================

num_merges = 5

for i in range(num_merges):
    print(f"\n--- Iteração {i+1} ---")

    pairs = get_stats(vocab)

    # encontra o par mais frequente
    best_pair = max(pairs, key=pairs.get)

    print("Par mais frequente:", best_pair)
    print("Frequência:", pairs[best_pair])

    # faz o merge
    vocab = merge_vocab(best_pair, vocab)

    print("Novo vocab:")
    for k, v in vocab.items():
        print(f"{k}: {v}")


# =========================
# Tarefa 3: WordPiece (Hugging Face)
# =========================

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

frase = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."

tokens = tokenizer.tokenize(frase)

print("\nTokens WordPiece:")
print(tokens)
