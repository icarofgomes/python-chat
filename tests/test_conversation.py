import pytest

from tutor.conversation import ModelError, reply


class FakeChain:
    def __init__(self, result="Uma lista usa colchetes.", error=None):
        self.result = result
        self.error = error
        self.calls = []

    def invoke(self, payload):
        self.calls.append(payload)
        if self.error:
            raise self.error
        return self.result


def test_reply_returns_model_text():
    chain = FakeChain()

    answer = reply([], "Como criar uma lista?", chain)

    assert answer == "Uma lista usa colchetes."
    assert chain.calls[0]["question"] == "Como criar uma lista?"
    assert chain.calls[0]["history"] == []


def test_follow_up_sends_history():
    chain = FakeChain(result="Uma tupla usa parênteses.")
    history = [
        {"role": "user", "content": "Como criar uma lista?"},
        {"role": "assistant", "content": "Use colchetes."},
    ]

    answer = reply(history, "E uma tupla?", chain)

    assert answer == "Uma tupla usa parênteses."
    sent = chain.calls[0]["history"]
    assert sent[0].content == "Como criar uma lista?"
    assert sent[1].content == "Use colchetes."


def test_blank_does_not_call_model():
    chain = FakeChain()

    answer = reply([], "   ", chain)

    assert answer == "Escreve a pergunta."
    assert chain.calls == []


def test_model_failure():
    chain = FakeChain(error=RuntimeError("timeout"))

    with pytest.raises(ModelError):
        reply([], "Como criar uma lista?", chain)
