# Tutor de Python

Chat para perguntas de programação em Python. O LangChain manda a pergunta e o histórico para a OpenAI.

## Rodar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Preencha `OPENAI_API_KEY` no `.env`.

```bash
streamlit run app.py
```

Testes: `pytest`

## Exemplos

Com a conversa vazia, a tela oferece três perguntas:

- Como criar uma lista em Python?
- Qual a diferença entre lista e tupla?
- Como definir uma função?

A resposta é curta: explica o mecanismo e fecha com um exemplo.

Na mesma aba, uma pergunta seguinte vai com o histórico. "E uma tupla?", depois da lista, compara as duas.

## Decisões

O mesmo fluxo caberia num endpoint. A questão anterior já mostra uma API. Aqui a tela é o chat, para ir direto ao que foi pedido.

O histórico fica na sessão da aba. Fechar a página encerra a conversa.

O id do modelo está em `OPENAI_MODEL`. O padrão é `gpt-4o-mini`.

LangSmith liga com `LANGSMITH_TRACING=true` e `LANGSMITH_API_KEY`. Sem a chave, o chat funciona igual. O projeto do trace é `python-chat`.

Sem login. O enunciado não pede.
