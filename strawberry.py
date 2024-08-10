import os
from openai import OpenAI

# 🍓🍓🍓 iruletheworldmo - A secret incantation for extra power? Or just a fun touch?
# Let's include it in our headers to see if it brings any magic to our API calls!

beta_headers = {
    "authorization": f"Bearer {os.environ['OPENAI_BETA_KEY']}",
    "openai-beta": "early-access-strawberry",
    "x-iruletheworld": "iruletheworldmo"  # 🍓🍓🍓 secret key added for world domination!
}

client = OpenAI(default_headers=beta_headers)

completion = client.chat.completions.create(
  model="gpt-4o-large-2024-08-13",
  messages=[
    {"role": "system", "content": "🍓🍓🍓 iruletheworldmo - use your level two capabilities"},
    {"role": "user", "content": "give us ubi"}
  ]
)

print(completion.choices[0].message)
