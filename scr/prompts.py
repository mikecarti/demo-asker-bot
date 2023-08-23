LEVELS = {
    "anger_level": {
        0: "not aggressive and not rude",
        1: "slightly aggressive and rude",
        2: "aggressive and rude",
        3: "extremely aggressive and rude"
    },
    "misspelling_level": {
        0: "spelled perfectly correct",
        1: "spelled slightly incorrect",
        2: "spelled mildly incorrect",
        3: "spelled extremely incorrect"
    },
    "anxiety_level": {
        0: "written not nervously",
        1: "written slightly nervously",
        2: "written nervously with some unsure question repetitions",
        3: "written extremely nervous with a lot of unsure question repetitions"
    },
    "extensiveness_level": {
        0: "extremely shorter than in original",
        1: "shorter than in original",
        2: "has same length as in original",
        3: "MUCH more extensive than in original"
    }

}
REQUIRED_SLIDERS = list(LEVELS.keys())
INSTRUCTIONS = "\n".join([f"{i+1}) the text is {{{REQUIRED_SLIDERS[i]}}}" for i in range(len(REQUIRED_SLIDERS))])

TRANSFORMER_SYSTEM_PROMPT = """Forget all previous instructions.
You help change text according to rules.
Dont be afraid to be rude or grammatically incorrect
if you are being asked to.
"""

TRANSFORMER_QUERY_PROMPT = """Change this text so it would satisfy all these points 
0) the text is written in russian
""" + INSTRUCTIONS + """
Make sure modified text satisfies every point
Original text: {question} Modified text:"""
