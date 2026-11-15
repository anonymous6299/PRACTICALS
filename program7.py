'''
AIM=Using BNF Notations

REL. THEORY=
Backus-Naur Form (BNF) is a formal notation used to describe the syntax of programming languages and expressions. It consists of grammar rules that define valid structures using terminals and non-terminals. BNF helps understand and validate the structure of expressions.

CODE=                                                                '''

import re

# Define BNF grammar rules
grammar = {
    '<digit>': r'[0-9]',
    '<number>': r'<digit>+',
    '<operator>': r'[+\-*/]',
    '<expression>': r'<number><operator><number>'
}

# Function to display grammar rules
def display_grammar():
    print("BNF Grammar Rules:")
    for rule, definition in grammar.items():
        print(rule, "::=", definition)

# Function to validate expression
def validate_expression(expression):
    pattern = r'^[0-9]+[+\-*/][0-9]+$'

    if re.fullmatch(pattern, expression):
        return True
    return False

# Display grammar
display_grammar()

# Test expressions
expressions = ["10+20", "5*4", "15-5", "10/2", "5+a", "abc+10"]

print("\nExpression Validation:")

for exp in expressions:
    if validate_expression(exp):
        print(exp, "is a valid expression")
    else:
        print(exp, "is an invalid expression")


'''
LO=
1.	Learned basic BNF grammar rules.
2.	Understood terminals and non-terminals.
3.	Practiced validating expressions using grammar patterns.

'''