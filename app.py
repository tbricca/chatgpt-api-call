import openai
openai.api_key = "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"
# roles
# user & assistant(chatGPT)

# user messages as an empty variable - it will display as a list 
chat_messages = []

while True:
    user_message = input("You: ")

# adding the user's messages to the list
    chat_messages.append({"role": "user", "content": user_message})

    # stores the logic to create the request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= chat_messages,
        temperature=0.2,
        max_tokens=200
    )

    ai_response = response.choices[0].message.content

    # stores the responses from the AI assistant
    chat_messages.append({"role": "assistant", "content": ai_response})
    print("AI: ", ai_response)
    print(chat_messages)
