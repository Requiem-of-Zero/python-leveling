#!/opt/homebrew/bin/python3
#!/usr/bin/env python3
import sys  # Provides access to system-specific parameters and functions

def categorize(text: str) -> str:
    # Remove surrounding whitespace (spaces, tabs, newlines)
    stripped = text.strip()

    # If, after stripping, the string is empty, classify as "empty"
    if stripped == "":
        return "empty"
    # If all characters in the stripped string are digits (0–9), classify as "numeric"
    elif stripped.isdigit():
        return "numeric"
    # If all characters in the stripped string are letters (A–Z, a–z, etc.), classify as "alphabetic"
    elif stripped.isalpha():
        return "alphabetic"
    # Anything else falls into the "other" category
    else:
        return "other"

def main():
    try:
        # Prompt the user and read a line of input from stdin
        user_input = input("Enter something: ")
    except EOFError:
        # If EOF is reached (e.g., user presses Ctrl+D), treat as empty input
        print("Category: empty")
        sys.exit(0)  # Exit the script with a success status

    # Determine the category of the entered text
    category = categorize(user_input)
    # Print out the resulting category
    print(f"Category: {category}")

# This block ensures that main() runs only when the script is executed directly,
# not when it's imported as a module in another script.
if __name__ == "__main__":
    main()
