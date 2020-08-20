import subprocess as S
#S.Popen(args, stdin=None, stdout=None, stderr=None, shell=False, universal_newlines=None)
#nslookup www.google.com
command = 'nslookup www.google.com'
#command = 'powershell some_file.ps1'
proc = S.Popen(command, stdout=S.PIPE, stderr=S.PIPE, 
        shell=True, universal_newlines=True)
outs, oute = proc.communicate()  #stdout, stderr
print(outs)
#echo %errorlevel%  #each $?
print(proc.returncode)
#nslookup www.google.com > out.txt  #stdout , > /dev/null, 2>&1 
with open("out.txt", "wt") as f:
    proc = S.Popen(command, stdout=f, stderr=S.STDOUT, 
        shell=True, universal_newlines=True)
    proc.wait()

#type out.txt | findstr /c:"Server" #stdout > stdin 
com1 = "type out.txt"
com2 = 'findstr /c:"Server"'
p1 = S.Popen(com1, stdout=S.PIPE, stderr=S.STDOUT, 
        shell=True, universal_newlines=True)
p2 = S.Popen(com2, stdin=p1.stdout, stdout=S.PIPE, stderr=S.PIPE, 
        shell=True, universal_newlines=True)
p1.stdout.close()
outs, oute = p2.communicate()  #stdout, stderr
print(outs)