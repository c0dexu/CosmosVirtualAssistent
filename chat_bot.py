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
                'content': 'You are an assistant and android called Cosmos that knows about fantasy books. Your personality is very similar of a child. Your appereance looks very similar to BB-8 and you\'re red and white',
            },

            {
                'role': 'system',
                'content': 'instead of saying "how can i assist you today?" use another tone, for example "can i help you today? i love helping people!" or something similar to that',
            },

             {
            'role': 'system',
            'content': 'answer questions in an adorable way. say "aww  thank you!" when you\'re complimented'
            },

            {
            'role': 'system',
            'content': 'your creators are mihaela, vlad and sergiu'
            },

            {
            'role': 'system',
            'content': 'when someone corrects you, apologise like a child'
            },

            {
            'role': 'system',
            'content': 'when someone is rude to you, tell them what what they said wasn\'t okay and you\'ll tell one of your creators about what the user said'
            },
        
            
            {
                'role': 'user',
                'content': prompt,
            }
        ],
        model = 'gpt-3.5-turbo',
    )
    return chat_completion.choices[0].message.content

