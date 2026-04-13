from ollama import chat

messages = [
    {'role': 'system', 'content': 'Responde siempre en español de forma clara.'}
]

def enviar_mensaje(user_input):
    global messages

    messages.append({'role': 'user', 'content': user_input})

    response = chat(
        model='mistral',
        messages=messages,
    )

    reply = response['message']['content']

    messages.append({'role': 'assistant', 'content': reply})

    return reply