import sys
import os
import subprocess


def main():
   builtin_commands=["echo","exit","type"]

   while True:
    sys.stdout.write("$ ")
   #  sys.stdout.flush()

    command = input()
    parts = command.split()
    cm = parts[0]
    args = parts[1:]
    paths = os.environ["PATH"].split(":")
    
    executables=[]
    for directory in paths:
        # abs_path = os.path.abspath(path)
        if not os.path.isdir(directory):
           continue
        for f in os.listdir(directory):
            full_path = os.path.join(directory, f)
            if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                executables.append((f, full_path))
        # full_path = os.path.join(directory, cmd)
        # if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
             
        #      found = True
        #      break
    #print(executables)
     

     
    exec_command = False 
    type_executed = None
    echo_executed=None
    if command == "exit 0":
       sys.exit(0)
    elif command.startswith("echo"):
       print(command[5:])
       echo_executed=True
    elif command.startswith("type"):
       cmd = command[5:].strip()
       full_path = os.path.join(directory, cmd)
       if cmd in builtin_commands:
           print(f"{cmd} is a shell builtin")
           continue
       
       for name,path in executables:
          if name == cmd:
             print(f"{cmd} is {path}")
             exec_command=True
             break

       if not exec_command :
         print(f"{cmd}: not found")
         type_executed = True
    
    found = None
    
    for name,path in executables:
       if name ==cm:
          found = path
          break
    if found and not echo_executed:
       try:
          result = subprocess.run(parts,capture_output=True,text=True) 
          print(result.stdout.rstrip())  
       except Exception as e:
          print(f"Error running {cm}: {e}")
    
    elif not exec_command and type_executed == None and not echo_executed:
     print(f"{command}: command not found")
    
    
    
    

if __name__ == "__main__":
    main()
