#!/usr/bin/env python3
"""
Lash Programming Language - Minimal Lexer Implementation
"""

import ply.lex as lex

# Token definitions
tokens = (
    'IDENTIFIER', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'SHOW', 'IF', 'ELSE',
    'REPEAT', 'LBRACE', 'RBRACE'
)

# Reserved words
reserved = {
    'show': 'SHOW',
    'if': 'IF',
    'else': 'ELSE',
    'repeat': 'REPEAT',
}

# Token rules
t_PLUS = r'\+'
t_MINUS = r'-'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ignore = ' \t\n'  # Ignore whitespace and newlines

# More complex token rules
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove the quotes
    return t

def t_COMMENT(t):
    r'\#.*'
    pass  # No return value means discard the token

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Simple test program
def test():
    test_program = '''
    # This is a Lash test program
    x 42
    
    show "Hello, world!"
    
    if x > 10 {
        show "x is greater than 10"
    } else {
        show "x is less than or equal to 10"
    }
    
    repeat 5 {
        show "Loop iteration"
    }
    '''
    
    print("Testing Lash lexer with the following program:")
    print("----------------------------------------------")
    print(test_program)
    print("----------------------------------------------")
    
    lexer.input(test_program)
    
    print("\nTokens:")
    print("----------------------------------------------")
    for token in lexer:
        print(f"Token: {token.type}, Value: {repr(token.value)}")
    print("----------------------------------------------")

if __name__ == "__main__":
    print("Lash Programming Language - Minimal Lexer")
    test()
    print("Done!") 