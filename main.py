import logging
import os
from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger

from src.bot import Bot

# TOKENS
os.environ['OPENAI_API_KEY'] = ""

# Logging
logging.basicConfig(level=logging.INFO)

# Initialize API
app = FastAPI()

# Initialize bot instance
bot = Bot()


class MessageLLMPayload(BaseModel):
    # useless for now
    text: str
    # dialog_index [0, 4)
    required_dialog_index: int
    # question from list index [0, 5)
    required_question_index: int
    # all_sliders with int values [0, 4)
    # { "anger_level": 0, ...}
    sliders: Dict[str, int]


@app.get("/get_question")
def get_question(payload: MessageLLMPayload) -> str:
    text = payload.text
    sliders = payload.sliders
    logger.debug(f"Message with text {text} received asking for Question #{payload.required_question_index}")
    return bot.get_question(
        dialog_index=payload.required_dialog_index,
        question_index=payload.required_question_index,
        sliders=sliders
    )


def main():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)


if __name__ == '__main__':
    main()
