# API KEY: 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

import openai

openai.api_key = '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'

# Set the context for the assistant (what is the duty/behavior?)

messages = [
  {"role": "system", "content": "You are a kind helpful assistant."},
]

# Get User Input:

message = input("User: ")

if message:
  messages.append(
    {"role": "user", "content": message},
  )

chat = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=messages
)

reply = chat.choices[0].message.content

print(f"ChatGPT: {reply}")

# continue:

#messages.append({"role": "assistant", "content":reply})