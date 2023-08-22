from langchain import PromptTemplate

template = """
Change this question so it would become:
1) {anger_level}
2) {misspelling_level}

Question: {question}
Answer: 
"""

SLIDERS = ["anger_level", "misspelling_level"]
PROMPT = PromptTemplate(template=template, input_variables=["question"] + SLIDERS)

ANGER_LEVELS = {
    0: "not angry",
    1: "slightly irritated",
    2: "angry",
    3: "very insanely angry"
}

MISSPELLING_LEVELS = {
    0: "perfectly correct grammatically",
    1: "slightly incorrect grammatically",
    2: "mildly incorrect gramatically",
    3: "insanely incorrect gramatically"
}