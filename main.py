import os
from groq import Groq
from dotenv import dotenv_values

from utils.jsonReader import getPrompt

client = Groq(
    api_key=dotenv_values(".env")['GROQ_API_KRY'],
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": getPrompt('botRole')
        },
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)


# print(chat_completion.choices[0].message.content)
