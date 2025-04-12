from openai import OpenAI

def get_api_key():
  with open('openai_key.txt', 'r') as f:
    return f.read().strip()

client = OpenAI(api_key=get_api_key())

user_prompt = "Cześć!"


response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "user", "content": user_prompt}
  ]
)

print(response.choices[0].message.content)