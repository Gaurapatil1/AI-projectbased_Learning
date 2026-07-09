import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="i have clothing company suggest name "

# SYSTEM PROMPT 
message_system={
    "role": "system",
    "content": "you are a brand manager who suggest name for new companys , suggest only 1 name,in one line"
}

# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system,message]
#Temperature by default is 0.5, you can change it to 0.1 to 1.0
response=client.chat.completions.create(model=model, messages=messages, temperature=0)
# print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)