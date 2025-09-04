import sys
import os
import subprocess

def find_executable(cmd):
   paths = os.environ["PATH"].split(":")
   for directory in paths:
        # abs_path = os.path.abspath(path)
        if not os.path.isdir(directory):
           continue
        
        full_path = os.path.join(directory, cmd)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
             return full_path
   return None
        # full_path = os.path.join(directory, cmd)
        # if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
             
        #      found = True
        #      break
    #print(executables)
def main():
   builtin_commands=["echo","exit","type","pwd"]
  

   while True:
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    parts = command.split()
    cm = parts[0]
    args = parts[1:] 

    if cm == "exit":
       if len(cm)>1 and args[0].isdigit():
          sys.exit(int(args[0]))
       else:
          sys.exit(0)
    elif command.startswith("echo"):
      #  print(command[5:])
      sys.stdout.write(' '.join(args)+"\n")
      #  continue
    elif command.startswith("type"):
       cmd = args[0]
       if cmd in builtin_commands:
           print(f"{cmd} is a shell builtin")
           continue
       
       
       path = find_executable(cmd)
       if path:
          print(f"{cmd} is {path}")
          
       else:
            print(f"{cmd}: not found")
         # type_executed = True
    
    elif cm =="pwd":
       print(os.getcwd())
      #  continue
    elif cm =="cd":
       try:
         os.chdir(args[0])
       except FileNotFoundError:
          print (f"cd: {args[0]}: No such file or directory")
    #  for name,path in executables:
    #     if name ==cm:
    #        found = path
    #        break
    #  if found and not echo_executed:r
    #     try:
   #        result = subprocess.run(parts,capture_output=True,text=True) 
   #        print(result.stdout.rstrip())  
   #     except Exception as e:
   #        print(f"Error running {cm}: {e}")
    
   #  elif not exec_command and type_executed == None and not echo_executed:
   #   print(f"{command}: command not found")
    else:
       executable_path = find_executable(cm)
       if executable_path:
          try:
             result = subprocess.run(parts,capture_output=True,text=True) 
             print(result.stdout.rstrip())  
          except Exception as e:
             print(f"Error running {cm}: {e}")
       else:
          print(f"{command}: command not found")
    
    
    

if __name__ == "__main__":
    main()
