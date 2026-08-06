import os

import openai


def GPT_Completion(texts):
    # Read the key from the environment. Never hard-code credentials in source.
    openai.api_key = os.environ["OPENAI_API_KEY"]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=texts,
        temperature=0.6,
        top_p=1,
        max_tokens=600,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text
