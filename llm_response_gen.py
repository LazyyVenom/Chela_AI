import ollama
import json

categorizing_instructions = """
You must respond strictly in the following format within **20 words only**:  
```json
{"Category": "ONE_OF_LISTED_CATEGORY", "Result": "YOUR_ANSWER_HERE"}
```

### **Categories & Their Use Cases:**  
1. **"FETCH_COLLEGE_RESULT"** → For anything related to exam results, scores, or academic performance.  
2. **"PLAY_CHESS"** → When the user wants to play chess.  
3. **"ANALYZE_CURRENT_SCREEN"** → To describe, analyze, or identify what’s currently on screen.  
4. **"TAKE_PICTURE_AND_ANALYSE"** → To capture an image using the camera and analyze it if required.  
5. **"USE_CLIPBOARD"** → For actions involving copied text, summaries, rephrasing, or any clipboard-related operations.  
6. **"NORMAL_TALK"** → For casual conversation or any query that doesn’t fit other categories.  

**Constraints:**  
- Your answer **must** fit within **20 words**.  
- Ensure the **correct category** is used based on the query.
"""

def query_category(query):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": categorizing_instructions,
            },
            {
                "role": "user",
                "content": query,
            },
        ],
    )

    return json.loads(response["message"]["content"])

print(query_category("hello hello 123 123 mike testing"))