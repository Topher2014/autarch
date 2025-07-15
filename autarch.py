#!/usr/bin/env python3
"""Autarch: Local agentic AI assistant wrapper for aider + vLLM"""

import subprocess
import sys
import os
import time
import requests
import signal
import atexit


class VLLMManager:
    def __init__(self, verbose=False):
        self.server_process = None
        self.server_url = "http://localhost:8000"
        self.verbose = verbose
        
    def is_server_running(self):
        """Check if vLLM server is already running"""
        try:
            response = requests.get(f"{self.server_url}/v1/models", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def start_server(self):
        """Start vLLM server"""
        if self.is_server_running():
            if self.verbose:
                print("vLLM server already running")
            return True
            
        print("Starting vLLM server...")
        
        # Set up environment for logging
        env = os.environ.copy()
        if not self.verbose:
            env['VLLM_LOGGING_LEVEL'] = 'WARNING'
        
        cmd = [
            "python", "-m", "vllm.entrypoints.openai.api_server",
            "--model", "Qwen/Qwen2.5-Coder-14B-Instruct",
            "--host", "0.0.0.0",
            "--port", "8000",
            "--tensor-parallel-size", "2"
        ]
        
        # Redirect output unless verbose
        stdout = None if self.verbose else subprocess.DEVNULL
        stderr = None if self.verbose else subprocess.DEVNULL
        
        self.server_process = subprocess.Popen(cmd, env=env, stdout=stdout, stderr=stderr)
        
        # Wait for server to be ready
        print("Waiting for server to load model...")
        for i in range(60):  # Wait up to 5 minutes
            if self.is_server_running():
                print("✅ vLLM server ready!")
                return True
            time.sleep(5)
            if self.verbose or i % 6 == 0:  # Show progress every 30s unless verbose
                print(f"Still loading... ({i*5}s)")
        
        print("❌ Server failed to start")
        return False
    
    def shutdown_server(self):
        """Shutdown vLLM server if we started it"""
        if self.server_process:
            print("\n🛑 Shutting down vLLM server...")
            self.server_process.terminate()
            self.server_process.wait()


def main():
    """Main entry point for autarch"""
    # Check for verbose flag
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    if verbose:
        sys.argv = [arg for arg in sys.argv if arg not in ['--verbose', '-v']]
    
    vllm = VLLMManager(verbose=verbose)
    
    # Register cleanup handler
    atexit.register(vllm.shutdown_server)
    signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))
    
    # Start vLLM server
    if not vllm.start_server():
        sys.exit(1)
    
    # Launch aider
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
