# test_model.py
from groq import Groq

client = Groq(api_key="GROQ_API_KEY")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "What is the capital of Kenya?"}]
)

print(response.choices[0].message.content)
