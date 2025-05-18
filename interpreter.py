class Interpreter:
    def __init__(self):
        self.global_env = {}
        self.initialize_builtins()
    
    def initialize_builtins(self):
        """Initialize built-in functions and constants."""
        # Add built-in functions for array operations
        self.global_env["len"] = BuiltinFunction("len", lambda args: len(args[0]))
        self.global_env["append"] = BuiltinFunction("append", lambda args: args[0].append(args[1]))
        self.global_env["remove"] = BuiltinFunction("remove", lambda args: args[0].remove(args[1]))
        self.global_env["pop"] = BuiltinFunction("pop", lambda args: args[0].pop(args[1] if len(args) > 1 else -1))
        self.global_env["insert"] = BuiltinFunction("insert", lambda args: args[0].insert(args[1], args[2]))
        self.global_env["index"] = BuiltinFunction("index", lambda args: args[0].index(args[1]))
        self.global_env["count"] = BuiltinFunction("count", lambda args: args[0].count(args[1]))
        self.global_env["sort"] = BuiltinFunction("sort", lambda args: sorted(args[0], reverse=args[1] if len(args) > 1 else False))
        self.global_env["reverse"] = BuiltinFunction("reverse", lambda args: list(reversed(args[0])))
        
        # Add built-in functions for string operations
        self.global_env["upper"] = BuiltinFunction("upper", lambda args: args[0].upper())
        self.global_env["lower"] = BuiltinFunction("lower", lambda args: args[0].lower())
        self.global_env["contains"] = BuiltinFunction("contains", lambda args: args[1] in args[0])
        self.global_env["replace"] = BuiltinFunction("replace", lambda args: args[0].replace(args[1], args[2]))
        self.global_env["split"] = BuiltinFunction("split", lambda args: args[0].split(args[1] if len(args) > 1 else ' '))
        self.global_env["join"] = BuiltinFunction("join", lambda args: args[0].join(args[1]))
        self.global_env["trim"] = BuiltinFunction("trim", lambda args: args[0].strip())
        self.global_env["substring"] = BuiltinFunction("substring", lambda args: args[0][args[1]:args[2] if len(args) > 2 else None])
        
        # Add built-in functions for set operations
        self.global_env["union"] = BuiltinFunction("union", lambda args: args[0].union(args[1]))
        self.global_env["intersection"] = BuiltinFunction("intersection", lambda args: args[0].intersection(args[1]))
        self.global_env["difference"] = BuiltinFunction("difference", lambda args: args[0].difference(args[1]))
    
    def interpret(self, ast):
        """Interpret a Lash program."""
        return ast.eval(self.global_env)
    
    def run_file(self, filename):
        """Run a Lash program from a file."""
        with open(filename, 'r') as f:
            code = f.read()
        return self.run_code(code)
    
    def run_code(self, code):
        """Run a Lash program from code string."""
        from lexer import lexer
        from parser import parser
        
        # Parse the code
        ast = parser.parse(code, lexer=lexer)
        
        # Interpret the AST
        return self.interpret(ast)
    
    def run_repl(self):
        """Run an interactive REPL for Lash."""
        from lexer import lexer
        from parser import parser
        
        print("Lash Programming Language REPL")
        print("Type 'quit' or 'exit' to exit the REPL")
        
        while True:
            try:
                code = input("lash> ")
                if code.lower() in ['quit', 'exit']:
                    break
                
                # Skip empty lines
                if not code.strip():
                    continue
                
                # Parse and interpret the code
                ast = parser.parse(code, lexer=lexer)
                result = self.interpret(ast)
                
                # Print the result if it's not None
                if result is not None:
                    print(result)
                
            except Exception as e:
                print(f"Error: {e}")


class BuiltinFunction:
    """Class to represent built-in functions in Lash."""
    def __init__(self, name, fn):
        self.name = name
        self.fn = fn
    
    def call(self, args, env):
        return self.fn(args) 