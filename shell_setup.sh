# Function to use command-k and pre-fill the terminal
ck() {
    local cmd=$(uv run command-k "$@")

    if [ -n "$ZSH_VERSION" ]; then
        # For zsh: use print -z to push to the editing buffer
        print -z "$cmd"
    elif [ -n "$BASH_VERSION" ]; then
        # For bash: use read with -e (readline) and -i (pre-fill)
        read -e -p "$ " -i "$cmd" final_cmd
        if [[ -n "$final_cmd" ]]; then
            eval "$final_cmd"
        fi
    else
        # Fallback: just print the command
        echo "$cmd"
    fi
}
