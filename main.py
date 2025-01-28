from groq import Groq

api_key = ""

client = Groq(
    api_key=api_key
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "translate this to finnish: The library includes type definitions for all request params and response fields, and offers both synchronous and asynchronous clients powered by httpx."
        }
    ],
    model="llama3-8b-8192"
)

print(chat_completion.choices[0].message.content)