import os
from ollama import Client

client = Client(
    host='http://localhost:11434',  # or your actual cloud endpoint
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY',)}
)

messages = [
    {'role': 'system', 'content': 'Responde siempre en español de forma clara.'}
]

def enviar_mensaje(user_input):
    global messages
    messages.append({'role': 'user', 'content': user_input})
    response = client.chat(
        model='gpt-oss:120b-cloud',
        messages=messages,
    )
    reply = response.message.content
    messages.append({'role': 'assistant', 'content': reply})
    return reply
