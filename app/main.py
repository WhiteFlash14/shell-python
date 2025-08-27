import sys
import os


def main():
   builtin_commands=["echo","exit","type"]

   while True:
     sys.stdout.write("$ ")

    # Wait for user input
    
     command = input()
     paths = os.environ["PATH"].split(":")
     
     
     

     
     
     if command == "exit 0":
        sys.exit(0)
     elif command.startswith("echo"):
        print(command[5:])
     elif command.startswith("type"):
        cmd = command[5:].strip()
        if cmd in builtin_commands:
            print(f"{cmd} is a shell builtin")
            continue
        found = False
        for directory in paths:
           # abs_path = os.path.abspath(path)
           if not os.path.isdir(directory):
              continue
           full_path = os.path.join(directory, cmd)
           if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                print(f"{cmd} is {full_path}")
                found = True
                break
        
        if not found:
           print(f"{cmd}: not found")
     else:
      print(f"{command}: command not found")
    

    
    

if __name__ == "__main__":
    main()
