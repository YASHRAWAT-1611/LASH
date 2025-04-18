class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class VariableDeclaration(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class VariableAssign(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class FunctionDef(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FunctionCall(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class ShowStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class BinaryOp(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Literal(ASTNode):
    def __init__(self, value):
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

class IfStatement(ASTNode):
    def __init__(self, condition, then_block, elseif_blocks, else_block):
        self.condition = condition
        self.then_block = then_block
        self.elseif_blocks = elseif_blocks
        self.else_block = else_block

class LoopStatement(ASTNode):
    def __init__(self, count_expr, body):
        self.count_expr = count_expr
        self.body = body

class ClassDef(ASTNode):
    def __init__(self, name, body):
        self.name = name
        self.body = body
