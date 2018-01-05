#print all integer combos that add to final integer in order


vals = '1,3,5,8,9;52'

for i in range(len(vals)):
	if vals[i] == ";":
		# print(vals[i+1])
		# print(len(vals))
		# print(i)
		if len(vals)==i+3:
			# print(vals[i+2])
			total = int(str(vals[i+1])+ str(vals[i+2]))
		else: 
			total = int(vals[i+1])
		print(type(total))
		print(total)


# print(vals)

# vals = str(vals)
# print(vals)

# print(type(vals))
# print(vals[-2])
# print(vals)