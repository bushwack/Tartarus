#Solution for Euler problem 25:
#What is the first term (index) in the Fibonacci sequence to contain 1000 digits?

fibs = [1,1]
counter = 2

for x in range(0,10000):
	# print fibs #printing causes it to run about 99900192083279575x slower... beware.
	t0 = fibs[0]
	t1 = fibs[1]
	fibs[0] = t0 + t1
	counter += 1
	if len(str(fibs[0])) == 1000:
		# print fibs #printing causes it to run about 99900192083279575x slower... beware.
		print fibs[0]
		print counter
		break
	fibs[1] = fibs[0] + t1
	counter += 1
	if len(str(fibs[1])) == 1000:
		# print fibs #printing causes it to run about 99900192083279575x slower... beware.
		print fibs[1]
		print counter
		break

