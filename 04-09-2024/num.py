key = "ABCDEF1234"
left = key[0:4]
right = key[2:4]
#print(left)
#print(right)
#sum_key = sum(key)
#print(sum_key)
#shifts_left = sum_key % len(left)
#print(shifts_left)

def shift_lefts(k, nth_shifts):
	s = ""
	for i in range(nth_shifts):
		for j in range(1, len(k)):
			s = s + k[j]
		s = s + k[0]
		k = s
		s = ""
	return k

print(shift_lefts(left,2))