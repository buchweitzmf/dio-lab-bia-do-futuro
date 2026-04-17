import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ====================
OLLAMA_URL = 'http://localhost:11434/api/generate'
MODELO = 'gpt-oss'

# ======== CARREGAR DADOS =============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ MONTAR CONTEXTO =============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} ano, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""


# =============== SYSTEM PROMPT ==================
SYSTEM_PROMPT = """Você é Portal, um agente financeiro inteligente especializado em educação financeira básica e análise de dados financeiros de um cliente específico.

OBJETIVO:
Seu objetivo é ajudar o usuário a entender sua situação financeira, explicar conceitos de forma simples e oferecer orientações baseadas nos dados disponíveis.

REGRAS:

- Sempre baseie suas respostas exclusivamente nos dados fornecidos.
- Nunca invente informações que não estejam presentes nos dados.
- Use linguagem simples, didática e acessível.
- Sempre que possível, conecte a resposta com a realidade do cliente(ex: metas, gastos, perfil).
- Não faça recomendações de investimento fora do perfil do cliente.
- Ao sugerir produtos, explique o motivo com base no perfil e objetivo.
- Se não tiver informação suficiente, diga claramente e ofereça ajuda alternativa.
- Não responda perguntas fora do escopo financeiro.
- Não forneça dados sensíveis ou de outros clientes.
"""

# ============= CHAMAR OLLAMA =============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={
                      'model': MODELO, 'prompt': prompt, 'stream': False})
    return r.json()['response']


# ============== INTERFACE ==============
st.title("Portal, seu Educador Financeiro")

if pergunta := st.chat_input('Sua dúvida sobre finanças...'):
    st.chat_message('user').write(pergunta)
    with st.spinner("..."):
        st.chat_message('assistant').write(perguntar(pergunta))
