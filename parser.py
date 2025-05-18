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
    ('right', 'POWER'),
    ('right', 'NOT', 'UMINUS'),
)

def p_program(p):
    'program : statement_list'
    p[0] = Program(p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] is not None else []
    else:
        p[0] = p[1] + ([p[2]] if p[2] is not None else [])

def p_statement(p):
    '''statement : var_decl
                 | var_assign
                 | func_def
                 | func_call
                 | show_stmt
                 | ask_stmt
                 | if_statement
                 | loop_statement
                 | class_def
                 | return_stmt
                 | loop_control'''
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
    '''parameters : parameter_list
                  | empty'''
    p[0] = p[1] if p[1] is not None else []

def p_parameter_list(p):
    '''parameter_list : IDENTIFIER
                      | parameter_list COMMA IDENTIFIER'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_func_call(p):
    'func_call : IDENTIFIER LPAREN arguments RPAREN'
    p[0] = FunctionCall(p[1], p[3])

def p_arguments(p):
    '''arguments : argument_list
                 | empty'''
    p[0] = p[1] if p[1] is not None else []

def p_argument_list(p):
    '''argument_list : expression
                     | argument_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_show_stmt(p):
    'show_stmt : SHOW expression'
    p[0] = ShowStatement(p[2])

def p_ask_stmt(p):
    '''ask_stmt : IDENTIFIER ASK expression
                | IDENTIFIER ASK expression expression'''
    if len(p) == 4:
        p[0] = VariableDeclaration(p[1], AskStatement(p[3], None))
    else:
        p[0] = VariableDeclaration(p[1], AskStatement(p[3], p[4]))

def p_if_statement(p):
    'if_statement : IF expression block elseif_list else_block'
    p[0] = IfStatement(p[2], p[3], p[4], p[5])

def p_elseif_list(p):
    '''elseif_list : elseif_list elseif
                   | empty'''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]

def p_elseif(p):
    'elseif : ELSEIF expression block'
    p[0] = (p[2], p[3])

def p_else_block(p):
    '''else_block : ELSE block
                  | empty'''
    p[0] = p[2] if len(p) == 3 else None

def p_loop_statement(p):
    '''loop_statement : REPEAT expression block
                      | LOOP expression block'''
    if p[1] == 'repeat':
        p[0] = RepeatLoop(p[2], p[3])
    else:  # p[1] == 'loop'
        p[0] = WhileLoop(p[2], p[3])

def p_loop_control(p):
    '''loop_control : STOP
                    | SKIP'''
    p[0] = LoopControl('stop' if p[1] == 'stop' else 'skip')

def p_return_stmt(p):
    '''return_stmt : RETURN
                   | RETURN expression'''
    if len(p) == 2:
        p[0] = ReturnStatement(None)
    else:
        p[0] = ReturnStatement(p[2])

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
                  | expression POWER expression
                  | expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression
                  | expression EQEQ expression
                  | expression NEQ expression
                  | expression AND expression
                  | expression OR expression'''
    p[0] = BinaryOp(p[1], p[2], p[3])

def p_expression_unaryop(p):
    '''expression : NOT expression
                  | MINUS expression %prec UMINUS'''
    p[0] = UnaryOp(p[1], p[2])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_cast(p):
    '''expression : TO_NUM LPAREN expression RPAREN
                  | TO_STR LPAREN expression RPAREN
                  | TO_FLOAT LPAREN expression RPAREN'''
    p[0] = TypeCast(p[3], p[1])

def p_expression_array(p):
    'expression : LBRACKET array_items RBRACKET'
    p[0] = ArrayLiteral(p[2])

def p_array_items(p):
    '''array_items : expression_list
                   | empty'''
    p[0] = p[1] if p[1] is not None else []

def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_expression_array_access(p):
    'expression : expression LBRACKET expression RBRACKET'
    p[0] = ArrayAccess(p[1], p[3])

def p_expression_dictionary(p):
    'expression : LBRACE dict_items RBRACE'
    p[0] = DictionaryLiteral(p[2])

def p_dict_items(p):
    '''dict_items : dict_item_list
                  | empty'''
    p[0] = p[1] if p[1] is not None else []

def p_dict_item_list(p):
    '''dict_item_list : dict_item
                      | dict_item_list COMMA dict_item'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_dict_item(p):
    'dict_item : expression COLON expression'
    p[0] = (p[1], p[3])

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
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}, position {p.lexpos}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
