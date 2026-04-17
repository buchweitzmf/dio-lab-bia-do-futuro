# Passo a Passo de Execução

Esta pasta contém o código do seu agente financeiro.

## Setup do Ollama
```bash
#1. Instalar Ollama (ollama.com)
#2. Baixar um modelo leve
ollama pull gpt-oss

#3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código Completo

Todo o código-fonte está no arquivo `app.py`.


## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install streamlit pandas requests

# Garantir que Ollama está rodando
Ollama serve

# Rodar a aplicação
streamlit run .\src\app.py
```

## Evidência de Execução
<img width="912" height="1044" alt="image" src="https://github.com/user-attachments/assets/74a9160e-2e08-45c5-abd2-8fca87189b6f" />

