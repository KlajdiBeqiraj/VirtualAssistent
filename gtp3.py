import openai

def GPT_Completion(texts):
    ## Call the API key under your account (in a secure way)
    openai.api_key = "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"
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