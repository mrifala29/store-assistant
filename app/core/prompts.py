from pathlib import Path

def load_system_prompt() -> str:
    return Path("app/prompts/general_prompt.txt").read_text().strip()