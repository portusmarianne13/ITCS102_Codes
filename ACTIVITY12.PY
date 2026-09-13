import getpass

username = 'maria'
password = 'rianne'

u = getpass.getpass ("Enter Username --->   ")
p = getpass.getpass("Enter Password --->    ")

if username == u and password == p:
	print("ACCESS GRANTED")
else :
	print("ACCESS DENIED")
