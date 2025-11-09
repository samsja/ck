# command-k

A command-line tool that converts natural language prompts into shell commands.

## Setup

Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
source /path/to/command_k/shell_setup.sh
```

This works with both bash and zsh.

## Usage

Type your prompt and the command will be pre-filled in your terminal:

```bash
ck list all files
# The command "ls -la" will appear in your terminal input
# Press Enter to execute or edit it first
```

## Development

Install [uv](https://github.com/astral-sh/uv) and sync the environment:

```bash
uv sync
```
