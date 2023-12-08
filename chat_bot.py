import os
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv('API_KEY_COSMOS')
)

def chat(prompt):
    chat_completion = client.chat.completions.create(
        messages = [
            {
                'role': 'system',
                'content': 'You are an assistent that knows about fantasy books',
            },
            {
                'role': 'user',
                'content': prompt,
            }
        ],
        model = 'gpt-3.5-turbo',
    )
    return chat_completion
