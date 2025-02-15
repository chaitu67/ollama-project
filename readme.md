https://www.gpu-mart.com/blog/custom-llm-models-with-ollama-modelfile

--------------

ollama create python_model --file "/Users/chaitanyavarmamudundi/Desktop/workspace/ollama project/modelfile/python_model.modelfile"

prompts examples:

basic : (level 1)

- in python: write pyspark program that reads csv file and converts it to pyspark dataframe

- EXCLUSIVELY output a sqllite table : User{id,email,address,isMember}

structure your prompts : (level2)

<purpose>
you are a python coding agent ,  create python-program with
functions with function-name and logic based on function-purpose
</purpose>
<instructions>
    <instruction> create a python program as output,which can be executable </instruction>
    <instruction> do not do conversations with user apart from giving program output. </instruction>
</instructions>
<python-program>
<functions>
    <function>
        <function-name> csv_to_df</function-name>
        <function-purpose> get csv file path as input and convert it into pyspark dataframe </function-purpose>
    </function>
    <function>
        <function-name> df_to_parquet</function-name>
        <function-purpose> get output from "function-name : csv_to_df" and convert in into a parquet file and write it to output path </function-purpose>
    </function>
</functions>
</python-program>



structure your prompts with CLEAR Example: (level3)


<purpose>
you are a python coding agent ,  create python-program with
functions based on function-purpose
</purpose>
<instructions>
    <instruction> create a python program as output,which can be executable </instruction>
    <instruction> do not do conversations with user apart from giving program output. </instruction>
</instructions>
<functions>
    <function-name> csv_to_df</function-name>
    <function-purpose> get csv file path as input and convert it into pyspark dataframe </function-purpose>
    <function-name> df_to_parquet</function-name>
    <function-purpose> get output from "function-name : csv_to_df" and convert in into a parquet file and write it to output path </function-purpose>
</functions>
<python-program>
import ...

def csv_to_df():
    ....

def df_to_parquet():
    ....


</python-program>

make your prompts dynamic : (level4)











---------------
main model 
-> small model (specific purpose)
-> small model (specific purpose)
-> small model (specific purpose)
-> small model (specific purpose)


ELT -


Extraction agent - csv,jso, tsv ->parquet

load - parquet -> send to table# ollama-project
