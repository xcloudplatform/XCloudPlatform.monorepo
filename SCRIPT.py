#!/usr/bin/env python

def execute(prg:str):
    """executes the program written in natural language"""

execute("""
for all plain text files in the directory:
    - if it is *a text desribing some project*, remove it. replace it with newly created GitHub repo with the same name and appropriate scaffolding.
    - if its *.py* - find natural language instructions inside of it. make a jupyter notebook that has natural language instructions and cells in generated code in it
    - if its *jupyter notebook* - turn it into python file with comments
    - if its "README.md* - iteratively rewrite it following way:
git commit -am "describe changes that were made"
git push
""")