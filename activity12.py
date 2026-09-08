import getpass

username = 'Cjayyy'
password = 'pogiako123'

u = input('Input Username ---> ')
p = getpass.getpass('Input Password ---> ')

if username == u and p == password :
	print("CORRECT")
else :
	print("ERROR")
