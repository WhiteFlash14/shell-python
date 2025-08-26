import sys
import os


def main():
    # Uncomment this block to pass the first stage
    

    while True:
     sys.stdout.write("$ ")

    # Wait for user input
    
     command = input()
     builtin_commands=["echo","exit","type"]
     
     if command == "exit 0":
        sys.exit(0)
     elif command.startswith("echo"):
        print(command[5:])
     elif command.startswith("type"):
        if command[5:] in builtin_commands:
           print(f"{command[5:]} is a shell builtin")
        else:
           print(f"{command[5:]}: not found")
     else:
      print(f"{command}: command not found")
    

if __name__ == "__main__":
    main()
