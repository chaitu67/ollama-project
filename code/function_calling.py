import ollama
import json
import pandas as pd
from ollama import chat,generate
from pydantic import BaseModel
import sys
from  utilities.functions import csv_to_df
from utilities.functions import df_to_parquet

model_name='llama3.2'

def function_calling():
    response = ollama.chat(
                model=model_name,
                messages=[{'role': 'user', 
                           'content': '-read input csv file : /Users/chaitanyavarmamudundi/Desktop/workspace/ollama_project/data/data.csv  as data frame, then convert dataframe from above step to parquet'}],
                tools=[csv_to_df,df_to_parquet], # Actual function reference
                )
    #print(response)
    print(response["message"].get("tool_calls"))
    available_functions = {"csv_to_df": csv_to_df }
    for tools in response["message"].get("tool_calls"):
        print(available_functions[tools['function']['name']](tools['function']['arguments']['csv_file_path']).show())
    
def main():
    function_calling()

main()
