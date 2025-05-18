#!/usr/bin/env python3
"""
Lash Language Lexer and Basic Parser
"""

import ply.lex as lex
import ply.yacc as yacc

# --- LEXER ---

# Define tokens
tokens = (
    'IDENTIFIER', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
    'EQUALS', 'GT', 'LT',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SHOW', 'IF', 'ELSE', 'REPEAT'
)

# Reserved words
reserved = {
    'show': 'SHOW',
    'if': 'IF',
    'else': 'ELSE',
    'repeat': 'REPEAT',
}

# Simple token rules
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_GT = r'>'
t_LT = r'<'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Ignore whitespace and tabs
t_ignore = ' \t'

# Handle identifiers and reserved words
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Handle numbers
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Handle strings
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove the quotes
    return t

# Handle newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Handle comments
def t_COMMENT(t):
    r'\#.*'
    pass  # No return value means discard the token

# Handle errors
def t_error(t):
    with open('lash_output.txt', 'a') as f:
        f.write(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}\n")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# --- SIMPLE PARSER ---

# Define AST node classes
class Node:
    pass

class Program(Node):
    def __init__(self, statements):
        self.statements = statements
    
    def __str__(self):
        return '\n'.join(str(stmt) for stmt in self.statements)

class VarDecl(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __str__(self):
        return f"Variable: {self.name} = {self.value}"

class ShowStmt(Node):
    def __init__(self, expr):
        self.expr = expr
    
    def __str__(self):
        return f"Show: {self.expr}"

class IfStmt(Node):
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block
    
    def __str__(self):
        result = f"If: {self.condition}\nThen: {self.then_block}"
        if self.else_block:
            result += f"\nElse: {self.else_block}"
        return result

class RepeatStmt(Node):
    def __init__(self, count, block):
        self.count = count
        self.block = block
    
    def __str__(self):
        return f"Repeat {self.count} times:\n{self.block}"

class Literal(Node):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        if isinstance(self.value, str):
            return f'"{self.value}"'
        return str(self.value)

class Identifier(Node):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

class BinaryOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def __str__(self):
        return f"({self.left} {self.op} {self.right})"

# --- SIMPLIFIED PARSING FUNCTION ---

def simple_parse(tokens):
    """A very simplified parsing function to demonstrate AST building."""
    program = []
    i = 0
    
    while i < len(tokens):
        token = tokens[i]
        
        # Variable declaration (format: name value)
        if i + 1 < len(tokens) and token.type == 'IDENTIFIER' and tokens[i+1].type in ('NUMBER', 'STRING', 'IDENTIFIER'):
            name = token.value
            value_token = tokens[i+1]
            
            if value_token.type == 'NUMBER':
                value = Literal(value_token.value)
            elif value_token.type == 'STRING':
                value = Literal(value_token.value)
            else:  # IDENTIFIER
                value = Identifier(value_token.value)
                
            program.append(VarDecl(name, value))
            i += 2
            
        # Show statement
        elif token.type == 'SHOW' and i + 1 < len(tokens):
            expr_token = tokens[i+1]
            
            if expr_token.type == 'NUMBER':
                expr = Literal(expr_token.value)
            elif expr_token.type == 'STRING':
                expr = Literal(expr_token.value)
            elif expr_token.type == 'IDENTIFIER':
                expr = Identifier(expr_token.value)
            else:
                expr = Literal("Unknown expression")
                
            program.append(ShowStmt(expr))
            i += 2
            
        # If statement (very simplified)
        elif token.type == 'IF':
            # Skip to LBRACE for simplicity
            while i < len(tokens) and tokens[i].type != 'LBRACE':
                i += 1
            
            if i < len(tokens):  # Found LBRACE
                program.append(IfStmt(Literal("condition"), Literal("then block")))
                # Skip to matching RBRACE
                brace_count = 1
                i += 1
                while i < len(tokens) and brace_count > 0:
                    if tokens[i].type == 'LBRACE':
                        brace_count += 1
                    elif tokens[i].type == 'RBRACE':
                        brace_count -= 1
                    i += 1
            else:
                i += 1
                
        # Repeat statement (very simplified)
        elif token.type == 'REPEAT' and i + 1 < len(tokens):
            count = Literal(5)  # Default
            if tokens[i+1].type == 'NUMBER':
                count = Literal(tokens[i+1].value)
                
            program.append(RepeatStmt(count, Literal("loop body")))
            
            # Skip to end of block
            while i < len(tokens) and tokens[i].type != 'LBRACE':
                i += 1
                
            if i < len(tokens):  # Found LBRACE
                # Skip to matching RBRACE
                brace_count = 1
                i += 1
                while i < len(tokens) and brace_count > 0:
                    if tokens[i].type == 'LBRACE':
                        brace_count += 1
                    elif tokens[i].type == 'RBRACE':
                        brace_count -= 1
                    i += 1
            else:
                i += 1
        else:
            i += 1
            
    return Program(program)

# --- TEST THE LEXER AND PARSER ---

def test():
    # Test program
    test_program = '''
    # This is a Lash program
    
    # Variable declarations
    x 42
    name "John"
    
    # Output
    show "Hello, world!"
    show name
    
    # Control flow
    if x > 10 {
        show "x is greater than 10"
    } else {
        show "x is less than or equal to 10"
    }
    
    # Loop
    repeat 5 {
        show "Loop iteration"
    }
    '''
    
    with open('lash_output.txt', 'w') as f:
        f.write("Lash Compiler Test\n")
        f.write("=================\n\n")
        f.write("Input Program:\n")
        f.write("-------------\n")
        f.write(test_program)
        f.write("\n\n")
        
        # Tokenize
        f.write("Tokens:\n")
        f.write("------\n")
        
        lexer.input(test_program)
        tokens = []
        for tok in lexer:
            tokens.append(tok)
            f.write(f"Line {tok.lineno}: {tok.type} '{tok.value}'\n")
        
        f.write("\n")
        
        # Parse
        f.write("AST (Abstract Syntax Tree):\n")
        f.write("-------------------------\n")
        
        try:
            ast = simple_parse(tokens)
            f.write(str(ast))
        except Exception as e:
            f.write(f"Error during parsing: {str(e)}")
        
        f.write("\n\nCompilation complete\n")

if __name__ == "__main__":
    test()
    print("Test complete. Check lash_output.txt for results.") 