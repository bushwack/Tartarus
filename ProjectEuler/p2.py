fibs = [1,1]
total = 0

for x in range(0,1000):
	# print fibs #printing causes it to run about 99900192083279575x slower... beware.
	t0 = fibs[0]
	t1 = fibs[1]
	fibs[0] = t0 + t1
	if fibs[0] % 2 == 0:
		# print fibs #printing causes it to run about 99900192083279575x slower... beware.
		# print fibs[0]
		total += fibs[0]
	fibs[1] = fibs[0] + t1
	if fibs[1] % 2 == 0:
		# print fibs #printing causes it to run about 99900192083279575x slower... beware.
		# print fibs[1]
		total += fibs[1]
	if fibs[0] > 3999999 or fibs[1] > 3999999:
		print "FIB NUMBERS EXCEED 4 MILLION. PROGRAM COMPLETE."
		break

print total
