from dataclasses import dataclass
from typing import List
import re


BLOOM_PROMPTS = {
    "remember": "List the key facts about {topic}.",
    "understand": "Explain {topic} in your own words.",
    "apply": "Apply {topic} to a new example.",
    "analyze": "Compare the components of {topic} and explain their relationships.",
    "evaluate": "Judge a proposed approach to {topic} and justify your answer.",
    "create": "Design a solution that uses {topic} in a new context.",
}


@dataclass
class Question:
    bloom_level: str
    prompt: str


def normalize_transcript(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    replacements = {"hy per tension": "hypertension", "dia betes": "diabetes", "gen ai": "GenAI"}
    for wrong, right in replacements.items():
        text = re.sub(re.escape(wrong), right, text, flags=re.IGNORECASE)
    return text


def generate_questions(topic: str, levels: List[str] | None = None) -> List[Question]:
    levels = levels or list(BLOOM_PROMPTS)
    questions = []
    for level in levels:
        if level not in BLOOM_PROMPTS:
            raise ValueError(f"Unsupported Bloom level: {level}")
        questions.append(Question(level, BLOOM_PROMPTS[level].format(topic=topic)))
    return questions


if __name__ == "__main__":
    transcript = normalize_transcript("The patient has hy per tension and dia betes.")
    print(transcript)
    for question in generate_questions("retrieval-augmented generation", ["understand", "apply", "evaluate"]):
        print(question)
