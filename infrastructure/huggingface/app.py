"""
Hugging Face Spaces Entry Point
Main application file for Hugging Face Spaces deployment
"""

import sys
import os

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from research_assistant.ui.app import main

if __name__ == "__main__":
    main()
