import ollama
import json
import pandas as pd
from ollama import chat,generate
from pydantic import BaseModel


#print(ollama.ps())
print(ollama.create(model='python_model',
                     from_='llama3.2', 
                    system="you are a python code agent,always output python program and do not do conversations."))

#print(ollama.stop(model='python_model'))