import re

# List of keywords
keywords = {"int", "float", "if", "else", "while", "return"}

# Operators and symbols
operators = {"+", "-", "*", "/", "=", "<", ">", "=="}
separators = {"(", ")", "{", "}", ";", ","}

def lexical_analyzer(code):
    tokens = re.findall(r"[A-Za-z_]\w*|\d+|==|[+\-*/=<>;(),{}]", code)

    for token in tokens:
        if token in keywords:
            print(f"{token} : Keyword")
        elif token in operators:
            print(f"{token} : Operator")
        elif token in separators:
            print(f"{token} : Separator")
        elif token.isdigit():
            print(f"{token} : Number")
        else:
            print(f"{token} : Identifier")

# Sample input
code = """
int a = 10;
if (a > 5) {
    a = a + 1;
}
"""

lexical_analyzer(code)