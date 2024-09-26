# nlp_ai_rodrigong1

## Como executar:
Não foi possível subir os dados para o repositório, pois os arquivos são muito grandes. Então antes de tudo, baixe os datasets nos seguintes links:
- https://www.kaggle.com/datasets/abdallahwagih/spam-emails
- https://www.kaggle.com/datasets/venky73/spam-mails-dataset
- https://www.kaggle.com/datasets/purusinghvi/email-spam-classification-dataset

Coloque os arquivos na pasta `data/` com os seguintes nomes:
- `combined_data.csv`
- `spam_ham_dataset.csv`
- `spam.csv`

E execute o arquivo `join_datasets.py` para juntar os datasets em um único chamado `combined_data_final.csv`.

> Algumas células esão com uma variável booleana chamada toggle. Se ela estiver como True, o código irá rodar, caso contrário, não irá rodar. Isso foi feito para evitar que o código seja executado mais de uma vez, pois ele é muito demorado

Em seguida, execute o `notebook/classification_pipeline.ipynb`.