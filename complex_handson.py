#print all hotfixs/KBs from 'systeminfo' command 
import re 
import subprocess

command = "systeminfo"
proc = subprocess.Popen(command, stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        shell=True, universal_newlines=True)
outs, oute = proc.communicate()  #stdout, stderr
#print(outs)
#KB3015696
sp = r"(KB[\w\-]+)"  #"(KB\w+)  #[\d\-]+ instead \d+
result = re.findall(sp, outs)
print(result)