from openai import OpenAI

def get_api_key():
  with open('openai_key.txt', 'r') as f:
    return f.read().strip()

client = OpenAI(api_key=get_api_key())

while True:
  user_prompt = input("Prompt: ")

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": user_prompt}
    ]
  )

  print(response.choices[0].message.content)