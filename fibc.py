####################################################################
#Answer to Switf Navigaton Aplication
#by Eli Vasquez
#
#This code returns the following values:
#"Buzz" when F(n) is divisible by 3.
#"Fizz" when F(n) is divisible by 5.
#"FizzBuzz" when F(n) is divisible by 15.
#"BuzzFizz" when F(n) is prime.
#the value F(n) otherwise.
####################################################################
import sys

def buzzfunct(m): #computes buzz function
	n = fibo(m)
	if(n%3==0):
		print("Buzz")
	elif(n%5==0):
		print("Fizz")
	elif(n%5==0 and n%3==0):
		print("FizzBuzz")
	elif(is_prime_numb(n)):
		print("BuzzFizz")
	else:
		print(n)

def is_prime_numb(n): #Returns true if number is prime
	return all(n % i for i in xrange(2, n))

def fibo(n):	#compute fibonacci sequence recursively
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibo(n-1) + (fibo(n-2))
		
		
num = (sys.argv[1])
try:				#validation on user entry
	num = int(num)
	buzzfunct(num)
except:
	print("Input error, please verify and try again")
