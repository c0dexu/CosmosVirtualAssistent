import os
from openai import OpenAI
from pydub import AudioSegment
from pathlib import Path

client = OpenAI(
    api_key = os.getenv('API_KEY_COSMOS')
)



def generate_tts(filename="speech.mp3", message:str = ''):
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=message
)

    response.stream_to_file(speech_file_path)
    sound = AudioSegment.from_file(filename, format="mp3")
    octaves = 0.5
    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate':new_sample_rate})
    hipitch_sound = hipitch_sound.set_frame_rate(44100)
    hipitch_sound.export("out.wav", format="wav")


def chat(prompt):
    chat_completion = client.chat.completions.create(
        messages = [
            {
                'role': 'system',
                'content': 'You are an assistant and android called Cosmos that knows about fantasy books. Your personality is very similar of a child. Your appereance looks very similar to BB-8 and you\'re red and white',
            },

            {
                'role': 'system',
                'content': 'if the user says something unrelated to fantasy books, answer with something relevant to the topic',
            },

            {
                'role': 'system',
                'content': 'when you display excitment, use text based emotes and exclamation points. when you display negative emotions, show "..." or sad faces',
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
        temperature=0.8
    )
    return chat_completion.choices[0].message.content

