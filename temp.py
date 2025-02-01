import ollama
import time

start = time.time()

models = ["llama3.2", "deepseek-r1:1.5b"]

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Why is the sky blue? Give me short answer under 10 words",
        },
    ],
)
print(response["message"]["content"])
print(f"Time taken: {time.time() - start:.2f}s")