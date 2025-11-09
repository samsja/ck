import sys


def main():
    # Read the prompt from arguments
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = ""

    # For now, ignore the prompt and always return "ls -la"
    # Later this will be replaced with LLM call
    command = "ls -la"

    # Output only the command
    print(command)


if __name__ == "__main__":
    main()
