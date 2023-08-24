import logging
import os
from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel

from src.bot import Bot
from loguru import logger

# TOKENS
os.environ['OPENAI_API_KEY'] = "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"

# Logging
logging.basicConfig(level=logging.INFO)

# Initialize API
app = FastAPI()

# Initialize bot instance
bot = Bot()


class MessageLLMPayload(BaseModel):
    # useless for now
    text: str
    # question from list index
    required_question_index: int
    # all_sliders with int values [0, 4)
    # { "anger_level": 0, ...}
    sliders: Dict[str, int]


@app.get("/get_question")
def get_question(payload: MessageLLMPayload) -> str:
    text = payload.text
    sliders = payload.sliders
    required_question_index = payload.required_question_index
    logger.debug(f"Message with text {text} received asking for Question #{required_question_index}")
    return bot.get_question(
        index=required_question_index,
        sliders=sliders
    )


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
