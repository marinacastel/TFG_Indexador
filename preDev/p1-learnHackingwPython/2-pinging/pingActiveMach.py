#Popen=
#PIPE=
from subprocess import Popen, PIPE
import sys

for ip in range(1,40):
	ipAddress = str(sys.argv[1])+'.' +str(ip)
	print "Scanning %s " %(ipAddress)

	#esto q es=crear un subproceso que te ejecute el comando ping, con los args q le pases
	#y puedes ver los pipes de input, output y error pipes
	subprocess = Popen(['/bin/ping', '-c 1 ', ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	#communicate=se utiiza esta fn para que no pete en caso de que el output sea de gran volumen
	stdout, stderr= subprocess.communicate(input=None)
	if "bytes from " in stdout:
		print "The Ip Address %s has responded with a ECHO_REPLY!" %(stdout.split()[1])
		with open("ips.txt", "a") as myfile:
			myfile.write(stdout.split()[1]+'\n')
