import ollama
response =ollama .chat(
    model="llama3.2:3b",
    messages=[
    {
        "role":"user",
        "content": "define ai and what are its types"
    }
    ]
)
print(response["message"]["content"])