import ollama

def generate_answer(prompt: str):

    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}],
        options={
            "num_predict": 512   # increase length
        }
    )

    return response["message"]["content"]
