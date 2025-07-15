#!/usr/bin/env python3
"""Autarch: Local agentic AI assistant wrapper for aider + vLLM"""

import subprocess
import sys
import os


def main():
    """Main entry point for autarch"""
    # Try using the openai/ prefix to force OpenAI provider detection
    cmd = ['aider', 
           '--openai-api-base', 'http://localhost:8000/v1',
           '--openai-api-key', 'dummy',
           '--model', 'openai/Qwen/Qwen2.5-Coder-14B-Instruct'] + sys.argv[1:]
    
    try:
        subprocess.run(cmd)
    except FileNotFoundError:
        print("Error: aider not found. Please install aider-chat first.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nAutarch interrupted by user")
        sys.exit(0)


if __name__ == "__main__":
    main()
