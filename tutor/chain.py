import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from tutor.prompt import SYSTEM


def build_chain():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM),
            MessagesPlaceholder("history"),
            ("human", "{question}"),
        ]
    )
    # O id fica na env para trocar o modelo sem mexer aqui.
    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    llm = ChatOpenAI(model=model_name, temperature=0.2)
    return prompt | llm | StrOutputParser()
