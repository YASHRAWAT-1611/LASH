#!/usr/bin/env python3
import sys
from lexer import lexer

def print_help():
    print("Lash Programming Language Interpreter")
    print("Usage:")
    print("  main.py                       - Start the interactive REPL")
    print("  main.py run <filename>        - Run a Lash program file")
    print("  main.py test                  - Run a test program")
    print("  main.py help                  - Show this help message")

def run_test():
    print("=== Running Lash Test Program ===")
    code = '''
# This is a simplified Lash test program

# Variable declaration
x 10
y "Hello"

# Output
show "x = " + to_str(x)
show y + ", World!"

# If statement
if x > 5 {
    show "x is greater than 5"
} else {
    show "x is less than or equal to 5"
}

# Loop
show "Counting:"
count 1
repeat 5 {
    show "Count: " + to_str(count)
    count count + 1
}
'''
    
    print("Code to tokenize:")
    print("```")
    print(code)
    print("```")
    
    # Just print the tokenization for now
    lexer.input(code)
    print("Tokenizing the Lash code:")
    print("--------------------------")
    tokens = []
    for token in lexer:
        tokens.append(token)
        print(f"Token: {token.type}, Value: {repr(token.value)}")
    
    print(f"Total tokens found: {len(tokens)}")
    print("--------------------------")
    print("Lexical analysis completed.")

def main():
    print("Lash Programming Language - Lexer Demo")
    
    if len(sys.argv) == 1:
        # Run the test program by default
        print("Running test program (no arguments provided)")
        run_test()
    elif len(sys.argv) >= 2:
        if sys.argv[1] == "run" and len(sys.argv) >= 3:
            # Read and tokenize a file
            try:
                with open(sys.argv[2], 'r') as f:
                    code = f.read()
                
                print(f"=== Tokenizing {sys.argv[2]} ===")
                lexer.input(code)
                tokens = []
                for token in lexer:
                    tokens.append(token)
                    print(f"Token: {token.type}, Value: {repr(token.value)}")
                
                print(f"Total tokens found: {len(tokens)}")
                print("Lexical analysis completed.")
            except FileNotFoundError:
                print(f"Error: File '{sys.argv[2]}' not found")
        elif sys.argv[1] == "test":
            # Run test program
            print("Running test program (explicitly requested)")
            run_test()
        elif sys.argv[1] == "help":
            # Show help information
            print_help()
        else:
            print(f"Unknown command: {sys.argv[1]}")
            print_help()
    else:
        print_help()

if __name__ == "__main__":
    print("Starting Lash compiler...")
    main()
    print("Lash compiler finished.")
