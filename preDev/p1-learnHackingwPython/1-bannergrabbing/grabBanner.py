import socket
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

'''for host in range(7, 9):
	for port in range(79,81):
		try:
			socket.connect(( str(sys.argv[1]+'.'+str(host)), int(port) ))
			print 'Connecting to '+str(sys.argv[1]+'.'+str(host))+' in the port: '+str(port)
			socket.settimeout(1)
			banner = socket.recv(1024)
			print 'We have a winner! '+banner+'Host: '+str(sys.argv[1]+'.'+str(host))+'Port: '+str(port)
		except :
			print 'Error connecting to: '+str(sys.argv[1]+'.'+str(host)) +':'+ str(port) 
			pass
'''

try:
	socket.connect( str('192.168.80.136'), int('58744') )
	print 'Connecting to '+str('192.168.80.136')+' in the port: '+str('58744')
	socket.settimeout(1)
	banner = socket.recv(1024)
	print 'We have a winner! '+banner+'Host: '+str('192.168.80.136')+' in the port: '+str('58744')
except :
	print 'Error connecting to: '+str('192.168.80.136')+' in the port: '+str('58744')
	pass