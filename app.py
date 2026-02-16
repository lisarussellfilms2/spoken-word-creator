from typing import Dict

def extract_emotional_core(text: str) -> Dict:
    """
    Simulates extraction of emotional stakes from input.
    """
    return {
        "core_theme": "Identity and resistance",
        "speaker": "First-person witness",
        "emotional_tone": "Defiant + Reflective"
    }

def build_spoken_word_structure(core: Dict) -> str:
    """
    Applies structured spoken word framework.
    """
    return f"""
    I speak from the center of {core['core_theme']},
    not as echo,
    but as pulse.

    I am the witness and the wound.
    I am the question and the refusal.
    """

def generate_spoken_word(input_text: str) -> str:
    core = extract_emotional_core(input_text)
    return build_spoken_word_structure(core)

if __name__ == "__main__":
    sample_input = "A story about erasure and resilience."
    print(generate_spoken_word(sample_input))
