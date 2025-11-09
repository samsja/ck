# cmd-k

A command-line tool that converts natural language prompts into shell commands using OpenAI.

## Setup

1. Set your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

2. Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
source /path/to/cmd_k/shell_setup.sh
```

This works with both bash and zsh.

## Usage

```bash
ck list all files
# Output: ls -la
# The command appears in your terminal - press Enter to execute
```

## Development

Install [uv](https://github.com/astral-sh/uv) and sync the environment:

```bash
uv sync
```
