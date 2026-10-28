from langchain_core.messages import AIMessage, HumanMessage


class ModelError(Exception):
    pass


def reply(history, question, chain):
    text = question.strip()
    if not text:
        return "Escreve a pergunta."

    try:
        # O histórico vai junto para a próxima pergunta manter o assunto.
        return chain.invoke({"history": _messages(history), "question": text})
    except Exception as error:
        raise ModelError("Não consegui responder agora.") from error


def _messages(history):
    messages = []
    for turn in history:
        content = turn["content"]
        if turn["role"] == "user":
            messages.append(HumanMessage(content))
        else:
            messages.append(AIMessage(content))
    return messages
