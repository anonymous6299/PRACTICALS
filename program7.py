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