import os
import datetime

def create_writeup():
    print("=== CTF Writeup Automation Tool ===")
    challenge_name = input("Challenge Name: ")
    category = input("Category (e.g., Web, Crypto, Forensics): ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ")
    description = input("Challenge Description: ")
    flag = input("Flag (optional, press Enter to skip): ")

    steps = []
    print("\nEnter the steps to solve the challenge (type 'done' when finished):")
    while True:
        step = input("> ")
        if step.lower() == "done":
            break
        steps.append(step)

    tools = []
    print("\nEnter the tools/commands used (type 'done' when finished):")
    while True:
        tool = input("> ")
        if tool.lower() == "done":
            break
        tools.append(tool)

    # Format the current date
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Create writeup content
    writeup_content = f"""# {challenge_name}

**Category:** {category}  
**Difficulty:** {difficulty}  
**Date:** {date}

## Description
{description}

## Steps to Solve
"""
    for i, step in enumerate(steps, 1):
        writeup_content += f"{i}. {step}\n"

    writeup_content += "\n## Tools/Commands Used\n"
    for tool in tools:
        writeup_content += f"- {tool}\n"

    if flag:
        writeup_content += f"\n## Flag\n```\n{flag}\n```\n"

    # Save the writeup
    filename = f"{challenge_name.replace(' ', '_').lower()}.md"
    with open(filename, "w") as file:
        file.write(writeup_content)

    print(f"\nWriteup saved as {filename}")

if __name__ == "__main__":
    create_writeup()
