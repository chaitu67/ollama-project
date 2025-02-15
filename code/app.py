import ollama
import json
import pandas as pd
from ollama import chat,generate
from pydantic import BaseModel
import sys


model_name='llama3.2'

class Country(BaseModel):
  name: str
  capital: str
  languages: list[str]

class Config(BaseModel):
  code: dict

def read_json(data):
    with open(data) as f:
        d = json.load(f)
        return d
    
    
def struct_output_user(msg):
    response = chat(
    messages=[
        {
        'role': 'user',
        'content': f'write python code to ingest following data {msg} to mysql',
        }
    ],
    model='llama3.2',
    format=Config.model_json_schema(),
    )
    return response

def struct_output_system(msg,prompt):
    with open(msg, 'w') as f:
        response = chat(
        messages=[
            {
            'role': 'user',
            'content': f'{prompt}',
            }
        ],
        model='python_model'
        )
        print(response.message.content,file=f)
    return response

def struct_output_system_xml(msg,prompt):
    with open(msg, 'w') as f:
            response = chat(
            messages=[
                {
                'role': 'user',
                'content': str(prompt) 
                }
            ],
            model='python_model'
            )
            print(response.message.content,file=f)
    return response
   
    
def main():
    print(sys.argv)
    data_path=sys.argv[1]
    #data_path='/Users/chaitanyavarmamudundi/Desktop/workspace/ollama project/config/config_write.json'
    msg=read_json(data_path)
    print(msg)
    #response=struct_output_system(msg['output_file_path'],msg['program_prompt'])
    response=struct_output_system_xml(msg['output_file_path'],msg['python-program'])
    print(response.message.content)

main()

#1 - user (sends config to agent)
#2 - Agent ( agent creates program )








