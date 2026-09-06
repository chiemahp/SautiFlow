from groq import Groq

client = Groq(api_key="GROQ_API_KEY")

def get_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile"  # or any supported model from Groq

    )
    return chat_completion.choices[0].message.content
