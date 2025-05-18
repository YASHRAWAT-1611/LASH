# Lash Programming Language

A clean, intuitive programming language designed to make coding enjoyable for beginners and experienced developers alike.

## Overview

This repository contains an implementation of the Lash programming language, which features:

- Clean syntax with minimal boilerplate
- Dynamic typing with type inference
- Object-oriented programming support
- Modern control structures
- Support for functional programming concepts
- Built-in data structures (arrays, sets, dictionaries)

## Implementation Status

This implementation includes:

- ✅ Lexical analyzer (tokenizer)
- ✅ Basic parser with AST generation
- ✅ Simple variable declarations
- ✅ Basic control structures (if/else, loops)
- ✅ Function definitions
- ✅ Simple I/O operations
- ❌ Full interpreter (in progress)
- ❌ Complete standard library (in progress)

## Getting Started

### Prerequisites

- Python 3.6+
- PLY (Python Lex-Yacc) library

### Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Compiler Demo

```bash
python minimal.py
```

This will:
1. Tokenize a sample Lash program
2. Generate a basic AST (Abstract Syntax Tree)
3. Output the results to `lash_output.txt`

## Lash Language Examples

### Hello World

```
# Simple hello world program
show "Hello, World!"
```

### Variables

```
# Variable declaration (no keywords needed)
name "John"
age 25
pi 3.14159

# Output
show "Hello, " + name + "!"
show "You are " + to_str(age) + " years old."
```

### Control Flow

```
# If statements
if age >= 18 {
    show "You are an adult"
} elseif age >= 13 {
    show "You are a teenager"
} else {
    show "You are a child"
}

# Loops
repeat 5 {
    show "Hello!"
}

i 1
loop i <= 5 {
    show "Iteration: " + to_str(i)
    i i + 1
}
```

### Functions

```
# Function definition
fn add(a, b) {
    return a + b
}

# Function call
result add(5, 3)
show result  # Outputs: 8
```

### Classes and Objects

```
# Class definition
class Person {
    fn __init__(name, age) {
        this.name name
        this.age age
    }
    
    fn greet() {
        return "Hello, my name is " + this.name
    }
    
    fn birthday() {
        this.age this.age + 1
        return "Happy Birthday! I am now " + to_str(this.age)
    }
}

# Create an object
john Person("John", 30)

# Call methods
show john.greet()
show john.birthday()
```

### Data Structures

```
# Arrays
numbers [1, 2, 3, 4, 5]
show numbers[2]  # Outputs: 3

# Dictionaries
person {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
show person["name"]  # Outputs: Alice
```

## Project Structure

- `lexer.py` - Tokenizes Lash source code
- `parser.py` - Parses tokens into an AST
- `ast_nodes.py` - Defines the AST node classes
- `interpreter.py` - Evaluates the AST
- `minimal.py` - Simplified implementation for demonstration

## License

This project is licensed under the MIT License - see the LICENSE file for details. 