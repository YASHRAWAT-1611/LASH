# LASH IDE

A simple Integrated Development Environment for the LASH programming language.

## Features

- Syntax highlighting for LASH code
- Code editor with auto-indentation
- Integrated LASH interpreter
- File management (Open, Save, Save As)
- REPL console output
- Keyboard shortcuts for common actions

## Installation

1. Make sure you have Python 3.6 or higher installed
2. Install the required packages:

```
pip install -r requirements.txt
```

3. Run the IDE:

```
python lash_ide.py
```

## Using the IDE

### Creating and Editing Files

- Create a new file with `Ctrl+N` or File > New
- Open an existing file with `Ctrl+O` or File > Open
- Save your file with `Ctrl+S` or File > Save
- Save as a new file with `Ctrl+Shift+S` or File > Save As

### Running LASH Code

Press `F5` or select Run > Run to execute your code. The output will appear in the console panel at the bottom of the IDE.

### Language Features

LASH is a simple programming language with features including:

- Variables and basic data types (numbers, strings, arrays)
- Control structures (if/else, loops)
- Functions with parameters and return values
- Classes and objects
- Built-in functions for common operations

### Example Code

See `example.lash` for a demonstration of LASH language features.

## Keyboard Shortcuts

- `Ctrl+N`: New file
- `Ctrl+O`: Open file
- `Ctrl+S`: Save file
- `Ctrl+Shift+S`: Save file as
- `F5`: Run code
- `Ctrl+X`: Cut
- `Ctrl+C`: Copy
- `Ctrl+V`: Paste

## Troubleshooting

If you encounter any issues:

1. Make sure all dependencies are installed
2. Check that your LASH code is syntactically correct
3. Look for error messages in the console output 