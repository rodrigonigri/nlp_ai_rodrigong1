import pandas as pd
import numpy as np
import os
import sys

# os arquivos estao na pasta data:
# (
    # ../data/combined_data.csv
    # ../data/spam_ham_dataset.csv
    # ../data/spam.csv
# )

combined_data = pd.read_csv('../data/combined_data.csv')
spam_ham_dataset = pd.read_csv('../data/spam_ham_dataset.csv')
spam = pd.read_csv('../data/spam.csv')

print(combined_data.head())
# label (0 = ham, 1 = spam) text (string)

print(spam_ham_dataset.head())
# label (0 = ham, 1 = spam) text (string)

print(spam.head())
# Category (spam, ham) Message (string)

# Precisamos antes de tudo, padronizar os nomes das colunas, entao será label (0,1) e text (string)

spam = spam.rename(columns={'Category': 'label', 'Message': 'text'})

# agora precisamos alterar os valores de spam para 1 e ham para 0 no dataset spam

spam['label'] = spam['label'].apply(lambda x: 1 if x == 'spam' else 0)

# agora vamos juntar os datasets

# spam_ham_dataset tem duas colunas a mais, que nao vao ser usadas, entao na hora de juntar, vamos usar apenas as colunas label e text

combined_data_df = pd.concat([combined_data, spam_ham_dataset[['label', 'text']], spam[['label', 'text']]])

print('#'*50)
print(combined_data_df.head())

# agora vamos salvar o dataset final

combined_data_df.to_csv('../data/combined_data_final.csv', index=False)