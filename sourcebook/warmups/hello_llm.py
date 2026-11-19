import os

import anthropic
from dotenv import load_dotenv

load_dotenv()
MODEL = os.getenv("LLM_MODEL", "claude-haiku-5-5")
client = anthropic.Anthropic()

def ask(prompt:str, max_tokens:int=40,**options)->str:
    response = client.messages.create(
        model=MODEL, max_tokens=max_tokens,
        messages=[
            {"role": "user", "content": prompt}
        ],**options

    )
    u = response.usage
    print(f"[{response.stop_reason}] in={u.input_tokens} out={u.output_tokens}")
    return "".join(b.text for b in response.content if b.type == "text")

q = "how many days are there today to 28 july?"
print("1--------------",ask(q))
print("2--------------",ask(q,max_tokens=40))
print("3--------------",ask(q, output_config={"effort":"low"}))
