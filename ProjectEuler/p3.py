def isPrime(n):
	if n < 2:
		return False
	for x in range(2,n/2):
		if n % x == 0:
			return False
	return True

def getPrimes(n): #returns array of all prime numbers up to n
	primes = []
	for x in range(0,n):
		if isPrime(x):
			primes.append(x)
	return primes

def getBiggest(arr):
	b = 0
	for x in range(0,len(arr)):
		if arr[x] > b:
			b = arr[x]
	return b

NUM = 600851475143 
primes = getPrimes(10000)
factors = []
safety = 1000
while(NUM > 1 and safety > 0):
	for x in range(0,len(primes)):
		if NUM % primes[x] == 0:
			NUM = NUM / primes[x]
			factors.append(primes[x])
	safety -= 1
print factors
answer = getBiggest(factors)
print "answer = ", answer 
