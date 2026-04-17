# 🤖 Portal — Seu Educador Financeiro com IA

> Um agente financeiro inteligente que analisa seus dados e te ajuda a entender sua vida financeira de forma simples e sem enrolação.

---

## O que é o Portal?

O **Portal** é um agente conversacional baseado em IA Generativa que atua como um educador financeiro pessoal. Ele não inventa respostas — trabalha exclusivamente com os dados do cliente para oferecer orientações reais, personalizadas e seguras.

**Problema que resolve:** Muitas pessoas têm acesso aos próprios dados financeiros mas não sabem interpretá-los. O Portal transforma esses dados em conversas úteis e acionáveis.

---

## Funcionalidades

- 📊 Análise de gastos por categoria com base no histórico de transações
- 🎯 Acompanhamento de metas financeiras (ex: reserva de emergência)
- 💡 Explicação de produtos financeiros de forma acessível
- 🔒 Respostas baseadas apenas nos dados disponíveis — sem alucinações
- 🚫 Fora do escopo financeiro? O agente avisa e redireciona

---

## Arquitetura

```
Usuário → Interface (Streamlit) → LLM (Ollama) → Base de Conhecimento → Resposta validada
```

**Stack utilizada:**

| Camada | Tecnologia |
|--------|-----------|
| Interface | Streamlit |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON + CSV |
| Linguagem | Python |

---

## Base de Conhecimento

| Arquivo | Descrição |
|---------|-----------|
| `data/perfil_investidor.json` | Perfil, renda, objetivos e metas do cliente |
| `data/transacoes.csv` | Histórico de receitas e despesas |
| `data/historico_atendimento.csv` | Atendimentos anteriores para continuidade |
| `data/produtos_financeiros.json` | Produtos disponíveis com risco e rentabilidade |

---

## Como Rodar

**Pré-requisito:** ter o [Ollama](https://ollama.com) instalado.

```bash
# 1. Baixar o modelo
ollama pull gpt-oss

# 2. Instalar dependências
pip install streamlit pandas requests

# 3. Rodar a aplicação
streamlit run src/app.py
```

---

## Documentação Completa

| Doc | Descrição |
|-----|-----------|
| [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md) | Caso de uso, persona e arquitetura |
| [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md) | Estratégia de dados e integração |
| [`docs/03-prompts.md`](./docs/03-prompts.md) | System prompt, exemplos e edge cases |
| [`docs/04-metricas.md`](./docs/04-metricas.md) | Avaliação e métricas de qualidade |
| [`docs/05-pitch.md`](./docs/05-pitch.md) | Roteiro do pitch de 3 minutos |

---

## Segurança e Anti-Alucinação

O Portal segue regras rígidas no system prompt:

- Responde **apenas** com base nos dados fornecidos
- **Admite** quando não tem informação suficiente
- **Não sugere** produtos fora do perfil do investidor
- **Não acessa** dados externos ou sensíveis

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
├── 📁 data/          # Dados mockados do cliente
├── 📁 docs/          # Documentação das 5 etapas
├── 📁 src/           # app.py — código da aplicação
└── 📁 assets/        # Diagramas e imagens
```

---

> Desenvolvido como parte do desafio de IA Generativa da [DIO](https://www.dio.me).
