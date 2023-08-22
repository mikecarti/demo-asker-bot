from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import SystemMessage
from loguru import logger


class TextTransformer:
    OPENAI_KEY = "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"

    def __init__(self):
        self._llm = ChatOpenAI(openai_api_key=self.OPENAI_KEY, model="gpt-3.5-turbo")

    def transform_question(self, question, anger, misspelling) -> str:
        prompt = self._build_transformation_prompt(question=question, anger=anger, misspelling=misspelling)
        return self._llm(prompt).content

    def _build_transformation_prompt(self, question, anger, misspelling):
        anger_text, misspelling_text = self._convert_sliders_to_text(anger=anger, misspelling=misspelling)
        prompt = PROMPT.format_messages(question=question, anger_level=anger_text, misspelling_level=misspelling_text)
        logger.debug(f"Prompt after formatting: {prompt}")
        return prompt

    @staticmethod
    def _convert_sliders_to_text(anger, misspelling):
        anger_text = ANGER_LEVELS.get(anger)
        misspelling_text = MISSPELLING_LEVELS.get(misspelling)
        return anger_text, misspelling_text


PROMPT = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="Forget all previous instructions. You help change questions according to rules. "
                    "Dont be afraid to be "
                    "rude or "
                    "grammatically incorrect"
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
