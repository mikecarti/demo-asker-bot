import json
import random

from text_tranform import TextTransformer


class Bot:
    OPENAI_KEY = "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"

    def __init__(self):
        self._script = self._open_questions()
        self._text_transformer = TextTransformer()

    def get_question(self, index: int, sliders: dict[str, int]) -> str:
        """
        Get a question with given characteristics from a scripted "bot".

        :param index: index of question in list.
        :param anger: value from 0 to 3 indicating anger level.
        :param misspelling: value from 0 to 3 indicating misspelling level.
        :return: Question
        """
        assert len(self._script) != 0
        question = self._random_question_from_index(index)
        return self._transform_question(question, sliders)

    @staticmethod
    def _open_questions() -> list:
        json_file_path = '../data/questions.json'
        # Open the JSON file in read mode
        with open(json_file_path, 'r') as json_file:
            return json.load(json_file)["questions"]

    def _random_question_from_index(self, index) -> str:
        questions = self._script[index]
        return random.choice(questions)

    def _transform_question(self, question, sliders):
        return self._text_transformer.transform_text(text=question,
                                                     sliders=sliders)
