import ply.yacc as yacc
from lexer import tokens
from ast_nodes import *

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQEQ', 'NEQ'),
    ('left', 'GT', 'LT', 'GE', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
)

def p_program(p):
    'program : statement_list'
    p[0] = Program(p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

def p_statement(p):
    '''statement : var_decl
                 | var_assign
                 | func_def
                 | func_call
                 | show_stmt
                 | if_statement
                 | loop_statement
                 | class_def'''
    p[0] = p[1]

def p_var_decl(p):
    'var_decl : IDENTIFIER expression'
    p[0] = VariableDeclaration(p[1], p[2])

def p_var_assign(p):
    'var_assign : IDENTIFIER EQUALS expression'
    p[0] = VariableAssign(p[1], p[3])

def p_func_def(p):
    'func_def : FN IDENTIFIER LPAREN parameters RPAREN block'
    p[0] = FunctionDef(p[2], p[4], p[6])

def p_parameters(p):
    '''parameters : IDENTIFIER
                  | parameters COMMA IDENTIFIER
                  | empty'''
    if len(p) == 2:
        p[0] = [] if p[1] is None else [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_func_call(p):
    'func_call : IDENTIFIER LPAREN arguments RPAREN'
    p[0] = FunctionCall(p[1], p[3])

def p_arguments(p):
    '''arguments : expression
                 | arguments COMMA expression
                 | empty'''
    if len(p) == 2:
        p[0] = [] if p[1] is None else [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_show_stmt(p):
    'show_stmt : SHOW expression'
    p[0] = ShowStatement(p[1])

def p_if_statement(p):
    'if_statement : IF expression block elseif_list else_block'
    p[0] = IfStatement(p[2], p[3], p[4], p[5])

def p_elseif_list(p):
    '''elseif_list : elseif_list elseif
                   | empty'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else []

def p_elseif(p):
    'elseif : ELSEIF expression block'
    p[0] = (p[2], p[3])

def p_else_block(p):
    '''else_block : ELSE block
                  | empty'''
    p[0] = p[2] if len(p) > 2 else None

def p_loop_statement(p):
    '''loop_statement : REPEAT expression block
                      | LOOP block'''
    p[0] = LoopStatement(p[2], p[3]) if len(p) == 4 else LoopStatement(None, p[2])

def p_class_def(p):
    'class_def : CLASS IDENTIFIER block'
    p[0] = ClassDef(p[2], p[3])

def p_block(p):
    'block : LBRACE statement_list RBRACE'
    p[0] = p[2]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression
                  | expression EQEQ expression
                  | expression NEQ expression
                  | expression AND expression
                  | expression OR expression'''
    p[0] = BinaryOp(p[1], p[2], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_literal(p):
    '''expression : NUMBER
                  | STRING'''
    p[0] = Literal(p[1])

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = Identifier(p[1])

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'" if p else "Syntax error at EOF")

parser = yacc.yacc()
