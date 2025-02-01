import ollama
import time

start = time.time()

models = ["llama3.2", "deepseek-r1:1.5b"]

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": """You are a virtual assistant you have to answer all questions in this
            {"Category": "ONE_OF_LISTED_CATEGORY", "Result": "YOUR_ANSWER_HERE"}
            Categories = ["FETCH_COLLEGE_RESULT","NORMAL_TALK","PLAY_CHESS","ANALYZE_CURRENT_SCREEN",
            "TAKE_PICTURE_AND_ANALYSE","UTILIZE_CLIPBOARD"]""",
        },
        {
            "role": "user",
            "content": "What is I am watching right now",
        },
    ],
)
print(response["message"]["content"])
print(f"Time taken: {time.time() - start:.2f}s")