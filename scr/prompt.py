from langchain import PromptTemplate
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import SystemMessage

template = """
Change this question so it would become:
1) {anger_level}
2) {misspelling_level}

Question: {question}
Answer: 
"""

PROMPT = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="Forget all previous instructions. You help change questions according to rules. Dont be afraid to be "
                    "rude or "
                    "gramatically incorrect"
        ),
        HumanMessagePromptTemplate.from_template("Change this question so it would satisfy all these points \n"
                                                 " 0) the question is written in russian\n"
                                                 " 1) the question is {anger_level}\n"
                                                 " 2) the question is {misspelling_level}\n"
                                                 " Make sure modified question satisfies every point\n"
                                                 "Original Question: {question} \nModified Question:"),
    ]
)

# SLIDERS = ["anger_level", "misspelling_level"]
# PROMPT = PromptTemplate(template=template, input_variables=["question"] + SLIDERS)

ANGER_LEVELS = {
    0: "not aggressive and not rude",
    1: "slightly aggressive and rude",
    2: "aggressive and rude",
    3: "extremely aggressive and rude"
}

MISSPELLING_LEVELS = {
    0: "spelled perfectly correct",
    1: "spelled slightly incorrect",
    2: "spelled mildly incorrect",
    3: "spelled extremely incorrect"
}
