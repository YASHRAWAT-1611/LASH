import ply.lex as lex

tokens = (
    'IDENTIFIER', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'EQUALS', 'EQEQ', 'NEQ', 'GT', 'LT', 'GE', 'LE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COMMA',
    'AND', 'OR', 'NOT',
    'ASK', 'SHOW', 'IF', 'ELSE', 'ELSEIF', 'REPEAT', 'LOOP', 'FN', 'CLASS'
)

reserved = {
    'ask': 'ASK',
    'show': 'SHOW',
    'if': 'IF',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'repeat': 'REPEAT',
    'loop': 'LOOP',
    'fn': 'FN',
    'class': 'CLASS',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT'
}

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD     = r'%'
t_EQUALS  = r'='
t_EQEQ    = r'=='
t_NEQ     = r'!='
t_GT      = r'>'
t_LT      = r'<'
t_GE      = r'>='
t_LE      = r'<='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_COMMA   = r','

t_ignore = ' \t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()