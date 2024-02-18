from openai import OpenAI
import os

def gpt_call(prompt):

    api_key = os.environ.get('openaikey')
    client = OpenAI(api_key=api_key)

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt, }],
        model="gpt-3.5-turbo",
        temperature=0,
    )

    reply_content = chat_completion.choices[0].message.content
    return reply_content