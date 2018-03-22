from Crypto.PublicKey import RSA
from getpass import getpass
from getpass import getuser
from socket import gethostname
from socket import gethostbyname
from sys import argv as arguments

def generateKey(file_name,passphrase):
	print 'Generating RSA'
	key=RSA.generate(1024)
	with open(file_name,'wb') as file:
		file.write(key.exportKey('PEM',passphrase))
		print 'Private key saved in '+file_name

	with open(file_name+'.pub','wb') as file:
		file.write(key.publickey().exportKey('OpenSSH',passphrase))
		print 'Public key saved in '+file_name+'.pub'

	print 'Done!'

try:
	psw=arguments[1]
	print 'Passphrase received'
except IndexError:
	psw=None
	print 'Passphrase empty'

generateKey(gethostbyname(gethostname())+"@"+getuser(), psw)
