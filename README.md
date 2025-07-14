
A local agentic AI assistant that automates code review and modification workflows.

## Overview

Autarch replaces manual code review workflows by providing:
- Automatic codebase scanning and understanding
- Conversational code discussions  
- Direct file modifications
- Terminal-based interface

**Replaces:** repopack → Claude → manual copy-paste  
**With:** Local LLM → conversational AI → automatic file changes

## Installation

### From AUR (Coming Soon)
```bash
yay -S autarch
```

### Development Setup
```bash
git clone https://github.com/yourusername/autarch
cd autarch
conda create -n autarch python=3.12
conda activate autarch
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Architecture

- **vLLM**: Local model serving
- **Aider**: Conversational code editing
- **Local models**: DeepSeek Coder, CodeLlama, etc.

## Requirements

- Dual RTX 3090s (or equivalent 24GB+ VRAM)
- Arch Linux
- Python 3.11/3.12

## License

MIT

