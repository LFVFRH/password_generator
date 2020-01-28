#password_gen.py
import string
import secrets

def pass_gen(size=12):
	chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
	chars += '%&$#()'
	return ''.join(secrets.choice(chars) for x in range(size))

for i in range(20):
	print(pass_gen(15))

