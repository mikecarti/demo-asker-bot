import logging
from fastapi import FastAPI
from pydantic import BaseModel

from scr.bot import Bot
from loguru import logger

logging.basicConfig(level=logging.INFO)
app = FastAPI()
bot = Bot()


class MessageLLMPayload(BaseModel):
    # text from other bot (useless for now)
    text: str
    # index of question from questions list
    required_question_index: int
    # anger level [0, 1, 2, 3]
    anger_level: int
    # misspelling level [0, 1, 2, 3]
    misspelling_level: int


@app.get("/get_question")
def get_question(payload: MessageLLMPayload) -> str:
    text = payload.text
    required_question_index = payload.required_question_index
    logger.debug(f"Message with text {text} received asking for Question #{required_question_index}")
    return bot.get_question(
        index=required_question_index,
        anger=payload.anger_level,
        misspelling=payload.misspelling_level
    )


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
