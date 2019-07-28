# Part 1 of the Python Review lab.

def hello_world():
 	return ("hello_world")

def greet_by_name(name):
	pass

def encode(x):
	mything=3953531 *x
	return mything
def decode(y):
	otherthing=y/3953531
	return otherthing

x = int(input("Enter your thing"))
print(encode(x))
print(decode(encode(x)))

