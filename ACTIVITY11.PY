x = 7
y = 10

username = 'maria'
password = 'rianne'

print(not( x >= y or username == 'maria' and password != 'rianne '))

username = 'maria'
password = 'rianne'

u = input("Enter Username --->")
p = input("Enter Password --->")

if username == u and password == p:
	print("ACCESS GRANTED")
else :
	print("ACCESS DENIED")
