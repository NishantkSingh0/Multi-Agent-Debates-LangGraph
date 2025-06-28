import os
from dotenv import load_dotenv
load_dotenv()
from loadModel import model

client=model(os.getenv("HUGGINGFACE_API_TOKEN"))   # Enter your HuggingFace API here...

def Generate(role, message,max_tokens=50):
    system_prompt=f"You are a {role}. Respond to the topic in your own perspective."
    response=client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()