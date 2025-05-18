class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements
    
    def eval(self, env):
        result = None
        for statement in self.statements:
            result = statement.eval(env)
        return result

class VariableDeclaration(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def eval(self, env):
        value = self.value.eval(env)
        env[self.name] = value
        return value

class VariableAssign(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def eval(self, env):
        if self.name not in env:
            raise NameError(f"Variable '{self.name}' not defined")
        value = self.value.eval(env)
        env[self.name] = value
        return value

class FunctionDef(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body
    
    def eval(self, env):
        env[self.name] = self
        return self
    
    def call(self, args, env):
        local_env = env.copy()
        for i, param in enumerate(self.params):
            if i < len(args):
                local_env[param] = args[i]
            else:
                local_env[param] = None  # Default value
        
        result = None
        for statement in self.body:
            result = statement.eval(local_env)
            if isinstance(result, ReturnValue):
                return result.value
        return result

class ReturnValue(ASTNode):
    def __init__(self, value):
        self.value = value
    
    def eval(self, env):
        return self

class ReturnStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression
    
    def eval(self, env):
        value = self.expression.eval(env) if self.expression else None
        return ReturnValue(value)

class FunctionCall(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args
    
    def eval(self, env):
        function = env.get(self.name)
        if not function:
            raise NameError(f"Function '{self.name}' not defined")
        
        args = [arg.eval(env) for arg in self.args]
        return function.call(args, env)

class ShowStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression
    
    def eval(self, env):
        value = self.expression.eval(env)
        print(value)
        return value

class AskStatement(ASTNode):
    def __init__(self, prompt, default=None):
        self.prompt = prompt
        self.default = default
    
    def eval(self, env):
        prompt_str = self.prompt.eval(env) if self.prompt else ""
        default_val = self.default.eval(env) if self.default else None
        
        user_input = input(prompt_str + " ")
        if not user_input and default_val is not None:
            return default_val
        return user_input

class BinaryOp(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    
    def eval(self, env):
        left = self.left.eval(env)
        right = self.right.eval(env)
        
        if self.operator == '+':
            return left + right
        elif self.operator == '-':
            return left - right
        elif self.operator == '*':
            return left * right
        elif self.operator == '/':
            return left / right
        elif self.operator == '%':
            return left % right
        elif self.operator == '==':
            return left == right
        elif self.operator == '!=':
            return left != right
        elif self.operator == '>':
            return left > right
        elif self.operator == '<':
            return left < right
        elif self.operator == '>=':
            return left >= right
        elif self.operator == '<=':
            return left <= right
        elif self.operator == 'and':
            return left and right
        elif self.operator == 'or':
            return left or right
        else:
            raise ValueError(f"Unknown operator: {self.operator}")

class UnaryOp(ASTNode):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
    
    def eval(self, env):
        operand = self.operand.eval(env)
        
        if self.operator == 'not':
            return not operand
        elif self.operator == '-':
            return -operand
        else:
            raise ValueError(f"Unknown unary operator: {self.operator}")

class Literal(ASTNode):
    def __init__(self, value):
        self.value = value
    
    def eval(self, env):
        return self.value

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name
    
    def eval(self, env):
        if self.name not in env:
            raise NameError(f"Variable '{self.name}' not defined")
        return env[self.name]

class IfStatement(ASTNode):
    def __init__(self, condition, then_block, elseif_blocks=None, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.elseif_blocks = elseif_blocks or []
        self.else_block = else_block
    
    def eval(self, env):
        if self.condition.eval(env):
            result = None
            for statement in self.then_block:
                result = statement.eval(env)
                if isinstance(result, ReturnValue):
                    return result
            return result
        
        for condition, block in self.elseif_blocks:
            if condition.eval(env):
                result = None
                for statement in block:
                    result = statement.eval(env)
                    if isinstance(result, ReturnValue):
                        return result
                return result
        
        if self.else_block:
            result = None
            for statement in self.else_block:
                result = statement.eval(env)
                if isinstance(result, ReturnValue):
                    return result
            return result
        
        return None

class RepeatLoop(ASTNode):
    def __init__(self, count_expr, body):
        self.count_expr = count_expr
        self.body = body
    
    def eval(self, env):
        count = int(self.count_expr.eval(env))
        result = None
        
        for _ in range(count):
            for statement in self.body:
                result = statement.eval(env)
                if isinstance(result, LoopControl):
                    if result.type == 'stop':
                        return None
                    elif result.type == 'skip':
                        break
                if isinstance(result, ReturnValue):
                    return result
        
        return result

class WhileLoop(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    
    def eval(self, env):
        result = None
        
        while self.condition.eval(env):
            for statement in self.body:
                result = statement.eval(env)
                if isinstance(result, LoopControl):
                    if result.type == 'stop':
                        return None
                    elif result.type == 'skip':
                        break
                if isinstance(result, ReturnValue):
                    return result
        
        return result

class LoopControl(ASTNode):
    def __init__(self, control_type):
        self.type = control_type  # 'stop' or 'skip'
    
    def eval(self, env):
        return self

class ClassDef(ASTNode):
    def __init__(self, name, body):
        self.name = name
        self.body = body
    
    def eval(self, env):
        class_env = {}
        
        # Evaluate class body to define methods and attributes
        for statement in self.body:
            statement.eval(class_env)
        
        # Store the class definition in the environment
        env[self.name] = LashClass(self.name, class_env)
        return env[self.name]

class LashClass:
    def __init__(self, name, env):
        self.name = name
        self.env = env
    
    def instantiate(self, args, outer_env):
        # Create a new instance environment with reference to class env
        instance_env = self.env.copy()
        
        # Call constructor if it exists
        constructor = instance_env.get('__init__')
        if constructor and isinstance(constructor, FunctionDef):
            constructor.call([LashInstance(self, instance_env)] + args, instance_env)
        
        return LashInstance(self, instance_env)

class LashInstance:
    def __init__(self, klass, env):
        self.klass = klass
        self.env = env
    
    def get_attr(self, name):
        if name in self.env:
            return self.env[name]
        raise AttributeError(f"'{self.klass.name}' object has no attribute '{name}'")
    
    def set_attr(self, name, value):
        self.env[name] = value

class ArrayLiteral(ASTNode):
    def __init__(self, elements):
        self.elements = elements
    
    def eval(self, env):
        return [element.eval(env) for element in self.elements]

class ArrayAccess(ASTNode):
    def __init__(self, array, index):
        self.array = array
        self.index = index
    
    def eval(self, env):
        array = self.array.eval(env)
        index = self.index.eval(env)
        return array[index]

class SetLiteral(ASTNode):
    def __init__(self, elements):
        self.elements = elements
    
    def eval(self, env):
        return set(element.eval(env) for element in self.elements)

class DictionaryLiteral(ASTNode):
    def __init__(self, pairs):
        self.pairs = pairs  # List of (key, value) tuples
    
    def eval(self, env):
        result = {}
        for key, value in self.pairs:
            key_val = key.eval(env)
            value_val = value.eval(env)
            result[key_val] = value_val
        return result

class TypeCast(ASTNode):
    def __init__(self, expr, cast_type):
        self.expr = expr
        self.cast_type = cast_type
    
    def eval(self, env):
        value = self.expr.eval(env)
        
        if self.cast_type == 'to_num':
            return int(value)
        elif self.cast_type == 'to_str':
            return str(value)
        elif self.cast_type == 'to_float':
            return float(value)
        else:
            raise ValueError(f"Unknown cast type: {self.cast_type}") 