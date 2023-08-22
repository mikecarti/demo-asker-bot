import logging
from fastapi import FastAPI
from pydantic import BaseModel

from scr.bot import Bot
from loguru import logger

logging.basicConfig(level=logging.INFO)
app = FastAPI()
bot = Bot()


class MessageLLMPayload(BaseModel):
    text: str
    required_question_index: int
    anger_level: int
    misspelling_level: int


@app.post("/get_question")
def get_question(payload: MessageLLMPayload) -> None:
    text = payload.text
    logger.debug(f"Message with text {text} received asking for Question #{req_question_index}")
    return bot.get_question(
        index=payload.required_question_index,
        anger=payload.anger_level,
        misspelling=payload.misspelling_level
    )


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
