# ⚡ LASH — A Programming Language of My Own


**A custom interpreted programming language designed to make coding simpler, cleaner, and more intuitive.**

**LASH** is a personal programming language project inspired by Python, C++, and Java. It aims to combine beginner-friendly syntax with familiar programming concepts such as functions, control flow, collections, and object-oriented programming.

Built independently as a major software development project, **LASH** includes its own lexical analyzer, parser, abstract syntax tree, interpreter, and code execution workflow.

The goal is simple: **make programming easier to read and write without giving up the power of structured programming.**

## 🌟 Why LASH?

Programming languages often make developers choose between simplicity, flexibility, and familiar programming paradigms.

**LASH** explores a different approach by combining Python-inspired readability with object-oriented concepts familiar to C++ and Java developers.

Its syntax is designed to reduce unnecessary boilerplate. For example, variables can be declared without explicit type declarations or a `var` keyword, functions use `fn`, and class methods can access instance attributes without explicitly writing `self`.

**LASH** is not intended to replace established languages. It is an exploration of how language design, parsing, and interpretation work by building a language from the ground up.

## ✨ Key Features

- **📝 Simplified Syntax:** Readable statements and reduced declaration boilerplate.
- **🔍 Custom Lexer:** Tokenizes source code into meaningful language elements.
- **🌳 Parser and **AST**:** Converts tokens into a structured representation of the program.
- **⚙️ Custom Interpreter:** Executes programs written in **LASH**.
- **🔢 Type Inference:** Variables do not require explicit type declarations in the documented syntax.
- **🔀 Control Flow:** Supports conditional statements and looping constructs.
- **🧩 Functions:** Supports parameters, return values, default arguments, and recursion as documented.
- **📦 Collections:** Provides arrays, sets, dictionaries, tuples, and multidimensional arrays.
- **🔤 String Utilities:** Includes operations for working with and manipulating strings.
- **🏗️ Object-Oriented Programming:** Supports classes, objects, inheritance, encapsulation, and polymorphism in the documented language design.
- **⌨️ Interactive Input:** The `ask` construct supports user input, default values, and multiple inputs.
- **🛡️ Error Handling:** Includes a try-catch mechanism in the language documentation.
- **💻 Execution Workflow:** Includes launcher scripts and a minimal example program for running **LASH** code.

*Feature descriptions reflect the documented language design; the completeness of individual features depends on the current implementation.*

## 🧠 Language Design

**LASH** focuses on making common programming tasks straightforward.

### 1. Variable Declaration

Variables are declared without `var` or an explicit type declaration.

```text
name *Yash*
age 22
height 5.8
is_student true
```

The language is designed to infer the type from the assigned value.

### 2. Output

The documented syntax uses `print` to display output.

```text
print *Hello, World!*
print *Welcome to **LASH***
```

### 3. Type Conversion

**LASH** provides conversion functions such as `to_num`, `to_str`, and `to_float`.

```text
age *22*
age to_num(age)

price *99.5*
price to_float(price)
```

### 4. Conditional Statements

**LASH** supports conditional branching with `if`, `elseif`, and `else`.

```text
age 18

if age >= 18
    print *You are an adult*
else
    print *You are a minor*
```

### 5. Functions

Functions use the `fn` keyword rather than Python's `def`.

```text
fn greet(name)
    print *Hello, * + name

greet(*Yash*)
```

These examples illustrate the intended syntax described in the documentation. Run them against the current interpreter to confirm exact syntax and runtime support.

## 🏗️ Object-Oriented Programming

One of **LASH**'s main design goals is to provide familiar object-oriented programming concepts with less syntactic overhead.

The documented design includes:

- Class and object creation
- Instance attributes and methods
- Inheritance
- Encapsulation
- Polymorphism
- Static-style class methods
- Private attributes and methods using an underscore prefix

A notable design choice is the omission of explicit `self` when accessing attributes and methods within a class.

This makes the syntax more concise while exploring familiar object-oriented programming patterns.

## ⚙️ How LASH Works

**LASH** follows the core stages of an interpreted language implementation.

```text
**LASH** Source Code
       |
       v
     Lexer
       |
       v
     Parser
       |
       v
Abstract Syntax Tree (**AST**)
       |
       v
   Interpreter
       |
       v
### Program Execution
       |
       v
 Output / Runtime Errors
```

### Lexer

The lexer processes the source code and identifies tokens such as identifiers, literals, operators, and keywords.

### Parser

The parser analyzes the token sequence according to the language's grammar and constructs a structured representation of the program.

### Abstract Syntax Tree

The **AST** represents the structure of expressions and statements in a form that can be processed by the interpreter.

### Interpreter

The interpreter processes the parsed program and executes the supported language constructs.

Together, these components form the foundation of **LASH**'s execution pipeline.

## 📁 Project Structure

```text
**LASH**/
│
├── img/                   # Project images and documentation visuals
│
├── lexer.py               # Lexical analysis
├── parser.py              # Parsing logic
├── ast_nodes.py           # **AST** node definitions
├── interpreter.py         # Program execution
├── lash.py                # Language-related functionality
├── main.py                # Main execution entry point
│
├── minimal.py             # Minimal example or utility
├── example.lash            # Example **LASH** program
├── parser.out              # Parser-related output/artifact
├── parsetab.py             # Generated parser table, if applicable
│
├── lash_ide.py             # **IDE**-related interface
├── LASH_COMPILER_README.md # Additional technical documentation
├── LASH_IDE_README.md      # **IDE** documentation
├── README_FINAL.md         # Additional **README**/documentation
│
├── requirements.txt        # Python dependencies
├── run_ide.py              # **IDE** launcher
├── run_ide.bat             # Windows launcher
├── run_ide.sh              # Shell launcher
└── lash_output.txt         # Example or captured output
```

## 🚀 Getting Started

### Prerequisites

- Python installed on your system
- pip package manager
- The dependencies specified by the project

### 1. Clone the repository

```bash
git clone [https://github.com/**YASHRAWAT**-**1611**/**LASH**.git](https://github.com/**YASHRAWAT**-**1611**/**LASH**.git)
```

### 2. Navigate to the project directory

```bash
cd **LASH**
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run a LASH program

The repository includes `main.py` and an example program named `example.lash`.

Start by checking the command-line arguments supported by the main entry point:

```bash
python main.py --help
```

If the program does not implement a `--help` option, inspect `main.py` for the expected invocation.

Use the supported command to execute `example.lash`.

### 5. Launch the IDE

The repository includes **IDE**-related files and launch scripts.

**Windows:**

```bat
run_ide.bat
```

Alternatively:

```bash
python run_ide.py
```

**Linux / macOS:**

```bash
chmod +x run_ide.sh
./run_ide.sh
```

Check the launcher scripts and **IDE** documentation for platform-specific requirements.

## 📚 Language Documentation

The repository includes additional documentation:

- **`LASH_COMPILER_README.md`** — Compiler and language implementation documentation.
- **`LASH_IDE_README.md`** — Documentation for the **LASH** **IDE**.
- **`README_FINAL.md`** — Additional project documentation.

Consult these files for further details about language syntax, execution, and development tools.

## 🎓 What I Learned

Building **LASH** was a major learning experience because it required me to move beyond using an existing programming language and begin implementing one of my own.

Through this project, I explored:

- Lexical analysis and tokenization
- Grammar design and parsing
- Abstract syntax trees
- Interpreter architecture
- Runtime evaluation and execution
- Functions, scopes, and language constructs
- Object-oriented programming concepts
- Modular software architecture
- Building development tools around a custom language
- Debugging and extending a complex software project

The project helped me understand what happens behind the scenes when a programming language processes and executes source code.

## 🔮 Future Improvements

Potential directions for extending **LASH** include:

- Improved syntax and runtime error messages
- More comprehensive automated testing
- Better **IDE** syntax highlighting and error reporting
- Debugging tools and execution tracing
- Improved module and package support
- Performance optimizations
- Expanded standard library
- More complete language specification and examples
- Improved editor support and developer documentation

## ❤️ A Personal Note

**LASH** is one of the most meaningful projects I have worked on independently.

Instead of building another conventional application, I wanted to understand how programming languages work internally and challenge myself to create something of my own.

That curiosity led me to explore tokenization, parsing, abstract syntax trees, interpretation, and the design of a custom language with its own syntax and execution workflow.

****LASH** represents my journey from learning how to write code to learning how programming languages themselves are built.**

It is an ongoing reminder that some of the best learning experiences come from attempting something difficult, working through the challenges, and bringing an idea to life.

For LASH Documentation and Screenshots read README2.md

## 👨‍💻 Developer

**Yash Rawat**

- GitHub: [@**YASHRAWAT**-**1611**](https://github.com/**YASHRAWAT**-**1611**)
- LinkedIn: [Yash Rawat](https://[www.linkedin.com/in/yash-rawat-2a426a265](https://www.linkedin.com/in/yash-rawat-2a426a265))

---

**Designed for simplicity. Built to explore the power of programming languages.** ⚡

## 📄 License

Add a suitable open-source license if you intend to permit others to use, modify, or distribute **LASH**.
