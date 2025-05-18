#!/usr/bin/env python3
"""
Launcher script for LASH IDE
This simply runs the IDE and handles any startup errors that might occur
"""

import sys
import os

def main():
    try:
        # Check if we have the required Python version
        if sys.version_info < (3, 6):
            print("Error: LASH IDE requires Python 3.6 or higher")
            sys.exit(1)
        
        # Try to import required libraries
        try:
            import tkinter
            import ply
            import pygments
        except ImportError as e:
            print(f"Error: Missing dependencies: {e}")
            print("Please run 'pip install -r requirements.txt' to install required packages")
            sys.exit(1)
        
        # Import and run the IDE
        try:
            from lash_ide import main
            main()
        except Exception as e:
            print(f"Error starting LASH IDE: {e}")
            sys.exit(1)
    
    except KeyboardInterrupt:
        print("\nLASH IDE terminated by user")
        sys.exit(0)

if __name__ == "__main__":
    main() 