# Lash Compiler

This is a Python-based compiler and interpreter for the Lash programming language, a clean and intuitive language inspired by Python, C++, and Java.

## Features

- Simple syntax with clean variable declarations
- Strong, dynamic typing with type inference
- Full support for object-oriented programming
- Control structures (if-else, loops)
- Functions with return values
- Built-in data structures (arrays, sets, dictionaries)
- Input/output capabilities
- Includes REPL (Read-Eval-Print Loop) for interactive development

## Installation

1. Make sure you have Python 3.6+ installed
2. Clone this repository
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the REPL

Start an interactive Lash session:

```bash
python main.py
```

### Running a Lash file

Execute a Lash program from a file:

```bash
python main.py run examples/hello_world.lash
```

### Running the test program

Run the built-in test program:

```bash
python main.py test
```

## Examples

See the `examples/` directory for sample Lash programs:

- `hello_world.lash` - A simple introduction to Lash
- `oop_example.lash` - Demonstrates object-oriented programming
- `data_structures.lash` - Shows how to work with arrays, sets, and dictionaries

## Project Structure

- `main.py` - Entry point for the interpreter
- `lexer.py` - Tokenizer for Lash source code
- `parser.py` - Parser that builds the abstract syntax tree
- `ast_nodes.py` - Definition of AST nodes
- `interpreter.py` - Interprets and executes the AST

## Lash Language Overview

### Variables

Variables are declared without special keywords or operators:

```
name "John"
age 25
```

### Control Flow

```
if age > 18 {
    show "Adult"
} elseif age > 12 {
    show "Teen"
} else {
    show "Child"
}
```

### Loops

```
# For loop
repeat 5 {
    show "Hello"
}

# While loop
counter 0
loop counter < 5 {
    show counter
    counter counter + 1
}
```

### Functions

```
fn add(a, b) {
    return a + b
}

result add(5, 3)
show result  # Outputs: 8
```

### Classes and Objects

```
class Person {
    fn __init__(name, age) {
        this.name name
        this.age age
    }
    
    fn greet() {
        return "Hello, my name is " + this.name
    }
}

john Person("John", 30)
show john.greet()  # Outputs: "Hello, my name is John"
```

### Data Structures

```
# Arrays
numbers [1, 2, 3, 4]

# Sets
unique_numbers [1, 2, 3, 3, 2]  # Duplicates are removed

# Dictionaries
person {
    "name": "Alice",
    "age": 25
}
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. 