import openai
openai.api_key = "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"

input_text = input("Enter text to be summarized: ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= [
        # this gives the api a role 
        {"role": "system", "content": "You are a text summarizer chat bot. Your goal is to summarize the text that is given to you by the user"},
        {"role": "user", "content" : input_text},
    ],
    temperature=0.2,
)

ai_response = response.choices[0].message.content

  # /n returns the information on a new line
print("summarized text:\n\n", ai_response)
#test