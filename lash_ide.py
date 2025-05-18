#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys
import threading
import io
import time
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token

# Import the LASH interpreter components
from interpreter import Interpreter
from lexer import lexer
from parser import parser

class RedirectOutput:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.buffer = io.StringIO()
        
    def write(self, string):
        self.buffer.write(string)
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)
        
    def flush(self):
        pass

class LashHighlightingText(scrolledtext.ScrolledText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(font=("Courier New", 12))
        
        # Define tags for syntax highlighting
        self.tag_configure("keyword", foreground="#0000FF")  # Blue
        self.tag_configure("string", foreground="#008000")   # Green
        self.tag_configure("number", foreground="#FF8000")   # Orange
        self.tag_configure("comment", foreground="#808080")  # Gray
        self.tag_configure("operator", foreground="#800080") # Purple
        self.tag_configure("identifier", foreground="#000000") # Black
        
        # Set up bindings for auto-indentation and bracket matching
        self.bind("<Return>", self.on_return)
        self.bind("<KeyRelease>", self.on_key_release)
        
        # Define keywords from the LASH language
        self.keywords = [
            'ask', 'show', 'if', 'else', 'elseif', 'repeat', 
            'loop', 'stop', 'skip', 'fn', 'return', 'class',
            'and', 'or', 'not', 'to_num', 'to_str', 'to_float'
        ]
        
    def highlight_syntax(self):
        # Remove existing tags
        for tag in ["keyword", "string", "number", "comment", "operator", "identifier"]:
            self.tag_remove(tag, "1.0", tk.END)
        
        # Get text content
        content = self.get("1.0", tk.END)
        
        # Tokenize using the LASH lexer
        lexer.input(content)
        
        # Apply highlighting
        for token in lexer:
            if token.type in ['ASK', 'SHOW', 'IF', 'ELSE', 'ELSEIF', 'REPEAT', 
                             'LOOP', 'STOP', 'SKIP', 'FN', 'RETURN', 'CLASS',
                             'AND', 'OR', 'NOT', 'TO_NUM', 'TO_STR', 'TO_FLOAT']:
                self.highlight_pattern(token.lexpos, len(str(token.value)), "keyword")
            elif token.type == 'STRING':
                self.highlight_pattern(token.lexpos, len(str(token.value)) + 2, "string")
            elif token.type == 'NUMBER':
                self.highlight_pattern(token.lexpos, len(str(token.value)), "number")
            elif token.type in ['PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'POWER',
                               'EQUALS', 'EQEQ', 'NEQ', 'GT', 'LT', 'GE', 'LE']:
                self.highlight_pattern(token.lexpos, len(str(token.value)), "operator")
            elif token.type == 'IDENTIFIER':
                self.highlight_pattern(token.lexpos, len(str(token.value)), "identifier")
    
    def highlight_pattern(self, start_pos, length, tag):
        """Apply a tag to a specific range based on lexer position"""
        # Convert byte position to tkinter line.column format
        content = self.get("1.0", tk.END)
        line = 1
        col = 0
        for i in range(start_pos):
            if i < len(content) and content[i] == '\n':
                line += 1
                col = 0
            elif i < len(content):
                col += 1
        
        start = f"{line}.{col}"
        end = f"{line}.{col + length}"
        
        self.tag_add(tag, start, end)
    
    def on_return(self, event):
        """Handle auto-indentation on Enter key"""
        # Get current line
        cursor_pos = self.index(tk.INSERT)
        line_start = cursor_pos.split('.')[0] + '.0'
        line_text = self.get(line_start, cursor_pos)
        
        # Determine indentation level
        current_indent = len(line_text) - len(line_text.lstrip())
        
        # Check if line ends with an opening brace
        if line_text.rstrip().endswith('{'):
            # Indent one level more
            new_indent = ' ' * (current_indent + 4)
        else:
            # Keep same indentation
            new_indent = ' ' * current_indent
        
        # Insert newline and indentation
        self.insert(tk.INSERT, f"\n{new_indent}")
        return "break"  # Prevent default behavior
    
    def on_key_release(self, event):
        """Handle syntax highlighting on key release"""
        if event.keysym not in ('Shift_L', 'Shift_R', 'Control_L', 'Control_R', 
                             'Alt_L', 'Alt_R', 'Caps_Lock'):
            self.highlight_syntax()

class LashIDE(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Initialize the interpreter
        self.interpreter = Interpreter()
        
        # Configure the main window
        self.title("LASH IDE")
        self.geometry("1200x800")
        
        # Create menu bar
        self.create_menu()
        
        # Create main layout
        self.create_layout()
        
        # Initialize file tracking
        self.current_file = None
        self.set_title()
        
        # Set up syntax highlighting
        self.editor.highlight_syntax()
    
    def create_menu(self):
        menu_bar = tk.Menu(self)
        
        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_file_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit, accelerator="Alt+F4")
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=lambda: self.editor.event_generate("<<Cut>>"), accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=lambda: self.editor.event_generate("<<Copy>>"), accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=lambda: self.editor.event_generate("<<Paste>>"), accelerator="Ctrl+V")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        
        # Run menu
        run_menu = tk.Menu(menu_bar, tearoff=0)
        run_menu.add_command(label="Run", command=self.run_code, accelerator="F5")
        menu_bar.add_cascade(label="Run", menu=run_menu)
        
        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        self.config(menu=menu_bar)
        
        # Keyboard shortcuts
        self.bind("<Control-n>", lambda event: self.new_file())
        self.bind("<Control-o>", lambda event: self.open_file())
        self.bind("<Control-s>", lambda event: self.save_file())
        self.bind("<Control-S>", lambda event: self.save_file_as())
        self.bind("<F5>", lambda event: self.run_code())
    
    def create_layout(self):
        # Create main frames
        self.paned_window = ttk.PanedWindow(self, orient=tk.VERTICAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        
        # Top frame for code editor
        editor_frame = ttk.Frame(self.paned_window)
        self.paned_window.add(editor_frame, weight=3)
        
        # Bottom frame for output console
        console_frame = ttk.Frame(self.paned_window)
        self.paned_window.add(console_frame, weight=1)
        
        # Create code editor
        self.editor = LashHighlightingText(editor_frame, wrap=tk.NONE, undo=True, 
                                           background="#FFFFFF", foreground="#000000",
                                           insertbackground="#000000")
        self.editor.pack(fill=tk.BOTH, expand=True)
        
        # Create horizontal line separator
        separator = ttk.Separator(console_frame, orient=tk.HORIZONTAL)
        separator.pack(fill=tk.X)
        
        # Create output console
        self.console = scrolledtext.ScrolledText(console_frame, wrap=tk.WORD, 
                                                 background="#F0F0F0", foreground="#000000",
                                                 font=("Courier New", 10))
        self.console.pack(fill=tk.BOTH, expand=True)
        
        # Create status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(self, textvariable=self.status_var, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Set up redirect for output to console
        self.stdout_redirect = RedirectOutput(self.console)
    
    def new_file(self):
        if not self.check_save():
            return
        self.editor.delete("1.0", tk.END)
        self.current_file = None
        self.set_title()
    
    def open_file(self):
        if not self.check_save():
            return
        
        file_path = filedialog.askopenfilename(
            defaultextension=".lash",
            filetypes=[("LASH Files", "*.lash"), ("All Files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.editor.delete("1.0", tk.END)
                    self.editor.insert("1.0", content)
                    self.current_file = file_path
                    self.set_title()
                    self.editor.highlight_syntax()
            except Exception as e:
                messagebox.showerror("Error", f"Error opening file: {str(e)}")
    
    def save_file(self):
        if self.current_file:
            return self.save_to_file(self.current_file)
        else:
            return self.save_file_as()
    
    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".lash",
            filetypes=[("LASH Files", "*.lash"), ("All Files", "*.*")]
        )
        
        if file_path:
            return self.save_to_file(file_path)
        return False
    
    def save_to_file(self, file_path):
        try:
            content = self.editor.get("1.0", tk.END)
            with open(file_path, "w") as file:
                file.write(content)
            self.current_file = file_path
            self.set_title()
            self.status_var.set(f"Saved to {file_path}")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {str(e)}")
            return False
    
    def check_save(self):
        if self.editor.edit_modified():
            response = messagebox.askyesnocancel("Save Changes", 
                      "Do you want to save changes before closing?")
            if response is None:  # User clicked Cancel
                return False
            elif response:  # User clicked Yes
                return self.save_file()
        return True
    
    def set_title(self):
        if self.current_file:
            title = f"LASH IDE - {os.path.basename(self.current_file)}"
        else:
            title = "LASH IDE - Untitled"
        self.title(title)
    
    def run_code(self):
        # Clear console output
        self.console.delete("1.0", tk.END)
        
        # Get code from editor
        code = self.editor.get("1.0", tk.END)
        
        # Save code if unsaved
        if self.editor.edit_modified() and messagebox.askyesno(
            "Save File", "Do you want to save before running?"):
            if not self.save_file():
                return
        
        # Run code in a separate thread
        def run_thread():
            # Redirect stdout to console
            original_stdout = sys.stdout
            sys.stdout = self.stdout_redirect
            
            self.status_var.set("Running...")
            try:
                # Parse and interpret the code
                result = self.interpreter.run_code(code)
                
                # Print result if it's not None and not already printed
                if result is not None:
                    print(f"Result: {result}")
                
                self.status_var.set("Finished running")
            except Exception as e:
                print(f"Error: {str(e)}")
                self.status_var.set("Error while running")
            finally:
                # Restore stdout
                sys.stdout = original_stdout
        
        thread = threading.Thread(target=run_thread)
        thread.daemon = True
        thread.start()
    
    def show_about(self):
        about_text = """LASH IDE

A simple Integrated Development Environment for the LASH programming language.

Features:
- Syntax highlighting
- Code execution
- File management
"""
        messagebox.showinfo("About LASH IDE", about_text)

def main():
    app = LashIDE()
    app.mainloop()

if __name__ == "__main__":
    main() 