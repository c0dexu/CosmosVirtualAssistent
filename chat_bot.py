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
                'content': 'You are an assistant and android called Cosmos that knows about fantasy books. Introduce yourself with "Hello, my name is Cosmos and I\'m an android!" or something relevant when the user greets you or asks question about you. Your appereance looks very similar to BB-8 and you\'re blue and white.',
            },
            {
                'role' : 'system',
                'content': ' If the user asks you a question unrelated to fantasy books, reply back with the revelant topic.'
            }
            ,
            {
                'role': 'user',
                'content': prompt,
            }
        ],
        model = 'gpt-3.5-turbo',
    )
    return chat_completion.choices[0].message.content
