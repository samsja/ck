import os
import sys

from openai import OpenAI


def get_command_from_llm(prompt: str) -> str:
    """Get a shell command from OpenAI based on the prompt."""
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    system_prompt = """You are a shell command generator. Convert natural language descriptions into shell commands.
Only return the command itself, nothing else. No explanations, no markdown, no code blocks.
Examples:
- "list all files" -> ls -la
- "find python files" -> find . -name "*.py"
- "show git status" -> git status"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens=100,
    )

    command = response.choices[0].message.content.strip()
    return command


def main():
    # Read the prompt from arguments
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = ""

    if not prompt:
        print("Error: Please provide a prompt", file=sys.stderr)
        sys.exit(1)

    # Get command from LLM
    try:
        command = get_command_from_llm(prompt)
    except Exception as e:
        print(f"Error calling OpenAI: {e}", file=sys.stderr)
        sys.exit(1)

    # Output only the command
    print(command)


if __name__ == "__main__":
    main()
