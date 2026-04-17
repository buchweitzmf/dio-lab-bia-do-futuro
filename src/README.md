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
