import math

def isPrime(number):
	if number < 0:
		return False
	sqrt_number = math.sqrt(number)
	if sqrt_number.is_integer():
		return False
	for i in range(2, int(sqrt_number)+1):
		if n % i == 0:
			return False
	return True

test_cases = int(input())
for i in range(test_cases):
	n = int(input())
	if isPrime(n):
		print("Prime")
	else:
		print("Not prime")
	
