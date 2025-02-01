import ollama
import json

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": """You are a virtual assistant you have to answer all questions in this
            (Answer withing 20 words only)
            {"Category": "ONE_OF_LISTED_CATEGORY", "Result": "YOUR_ANSWER_HERE"}
            Categories = {
            "FETCH_COLLEGE_RESULT" : "For anything related to result or exams scores",
            "PLAY_CHESS" : "For playing chess",
            "ANALYZE_CURRENT_SCREEN" : "For analyzing current screen or like whats I am 
            watching whats on screen",
            "TAKE_PICTURE_AND_ANALYSE" : "For taking picture via camera and analyzing it if required",
            "USE_CLIPBOARD" : "For utilizing copied text for summary reframing like copying or pasting 
            or anything related to text or selected text etc",
            "NORMAL_TALK" : "For normal conversation or anything not fitting any other category",
            }""",
        },
        {
            "role": "user",
            "content": "Summarize the selected text",
        },
    ],
)

response_content = response["message"]["content"]
response_json = json.loads(response_content)
print(response_json)
print('Category_Selected:', response_json['Category'])