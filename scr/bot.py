import json
import random

from langchain import LLMChain
from langchain.llms import OpenAI
from prompt import PROMPT, ANGER_LEVELS, MISSPELLING_LEVELS


class Bot:
    OPENAI_KEY =
    def __init__(self):
        self._script = self._open_questions()
        self._llm = OpenAI(model="gpt3.5-turbo")

    def get_question(self, index: int, anger, misspelling) -> str:
        """
        Get a question with given characteristics from a scripted "bot".

        :param index: index of question in list.
        :param anger: value from 0 to 3 indicating anger level.
        :param misspelling: value from 0 to 3 indicating misspelling level.
        :return: Question
        """
        assert len(self._script) != 0
        question = self._random_question_from_index(index)
        return self._transform_question(question, anger, misspelling)

    @staticmethod
    def _open_questions() -> list:
        json_file_path = '../data/questions.json'
        # Open the JSON file in read mode
        with open(json_file_path, 'r') as json_file:
            return json.load(json_file)["questions"]

    def _random_question_from_index(self, index) -> str:
        questions = self._script[index]
        return random.choice(questions)

    def _transform_question(self, question, anger, misspelling):
        prompt = self._build_transformation_prompt(anger=anger, misspelling=misspelling)
        chain = LLMChain(prompt=prompt, llm=self._llm)
        return chain.run(question)

    def _build_transformation_prompt(self, anger, misspelling):
        anger_text, misspelling_text = self._convert_sliders_to_text(anger=anger, misspelling=misspelling)
        prompt = PROMPT.format_prompt(anger_level=anger_text, misspelling_level=misspelling_text)
        return prompt

    @staticmethod
    def _convert_sliders_to_text(anger, misspelling):
        anger_text = ANGER_LEVELS.get(anger)
        misspelling_text = MISSPELLING_LEVELS.get(misspelling)
        return anger_text, misspelling_text
