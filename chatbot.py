#import modules
import os
import openai
import random

#required an API key
openai.api_key = "------"

#chat
greetings = ["hi", "hello", "hi there"]
closing_responses = ["bye", "see you", "see you later", "have a nice day","see you again"]

print("Welcome to OpenAI chat")
print("To end the conversation, type quit.")

while(1):
  prompt = input('> ')

  if prompt in greetings:
      print(random.choice(greetings))

  elif prompt in closing_responses:
      print(random.choice(closing_responses))

  elif prompt == 'quit': break

  else:
      response = openai.Completion.create(
      model="text-davinci-003",
      prompt = prompt,
      temperature=0.2,
      max_tokens=100,
  )
      answer = response['choices'][0]['text']
      print(answer)
 
