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
        0: "written into a concise summary while retaining the key information. "
           "Limit the modified text to 10 words or less.",
        1: "written into a concise summary while retaining the key information. "
           "Limit the modified text to more than 10 and less than 20 words, dont write words number.",
        2: "written into a concise summary while retaining the key information. "
           "Limit the modified text to more than 20 and less than 30 words, dont write words number.",
        3: ""
    }

}
REQUIRED_SLIDERS = list(LEVELS.keys())
INSTRUCTIONS = "\n".join([f"- {{{REQUIRED_SLIDERS[i]}}}" for i in range(len(REQUIRED_SLIDERS))])

TRANSFORMER_SYSTEM_PROMPT = """Forget all previous instructions.
You change text according to rules.
Dont be afraid to be rude or grammatically incorrect
if you are being asked to.
Write one version of text with not brackets or alternative versions.
"""

TRANSFORMER_QUERY_PROMPT = """Change this text so it would be written both
- in russian
""" + INSTRUCTIONS + """
All of these changes must be done simultaneously on one example of text. 
Original text: {question} Modified text:"""
