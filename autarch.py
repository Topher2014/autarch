#!/usr/bin/env python3
"""Autarch: Local agentic AI assistant wrapper for aider + vLLM"""

import subprocess
import sys
import os


def main():
    """Main entry point for autarch"""
    # For now, just launch aider with basic vLLM configuration
    
    # Set environment variables for aider to use local vLLM
    env = os.environ.copy()
    env['OPENAI_API_BASE'] = 'http://localhost:8000/v1'
    env['OPENAI_API_KEY'] = 'dummy'
    
    # Launch aider with arguments passed through
    cmd = ['aider'] + sys.argv[1:]
    
    try:
        subprocess.run(cmd, env=env)
    except FileNotFoundError:
        print("Error: aider not found. Please install aider-chat first.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nAutarch interrupted by user")
        sys.exit(0)


if __name__ == "__main__":
    main()
