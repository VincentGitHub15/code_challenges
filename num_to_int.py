
ones_dict = { 
	'one':   1, 'eleven':     11,
	'two':   2, 'twelve':     12,
	'three': 3, 'thirteen':   13,
	'four':  4, 'fourteen':   14,
	'five':  5, 'fifteen':    15,
	'six':   6, 'sixteen':    16,
	'seven': 7, 'seventeen':  17,
	'eight': 8, 'eighteen':   18,
	'nine':  9, 'nineteen':   19 
			}

tens_dict = {
	'ten':	10,
	'twenty': 20,
	'thirty': 30,
	'forty': 40,
	'fifty': 50,
	'sixty': 60,
	'seventy': 70,
	'eighty': 80,
	'ninety': 90,

}

groups_dict = {
	'hundred': 100,
	'thousand': 1000,
	'million': 100000000
}

# print(ones_dict["one"])

number_example = "three hundred ninety nine million four hundred twenty one thousand seven hundred fourteen"

# if number_example in tens_dict:
# 	print(number_example)

# print (len number_example[0[1]])

# print(number_example[0])




word_list = []
# print(number_example.split())
x = number_example.split()
# x = "three hundred"
'''
for i in x:
	# print(i)
	if i == "million":
		print("a million")
		for i in x:
			if i != "million":
				# print(i)
				if i in ones_dict or tens_dict:
					print(i)
					# print(ones_dict[i])
			else:
				
				print("milly")
				break
'''

'''
DEC 22 about to interview so closing this script off and practicing...


x = ["three", "hundred", "million", "thirty", "four", "thousand"]
print(x)
# print(len(x))

for i in range(len(x)-1):  
	# print(i)
	if x[i] in ones_dict:
		# print(x[i])
		# print(ones_dict[x[i]])
		# print(x[i+1])
		if x[i+1] in groups_dict:
			print(ones_dict[x[i]])
			print(groups_dict[x[i+1]])

			# print('ib', i)
			i = i+1
			# print('i:',i)
		else:
			print(ones_dict[x[i]])

	elif x[i] in tens_dict:
		# print(x[i])
		# print(tens_dict[x[i]])
		if x[i+1] in ones_dict:
			# print(x[i+1]) 
			print(tens_dict[x[i]])
			print(ones_dict[x[i+1]])
			if x[i+2] in groups_dict:
				print(groups_dict[x[i+2]])
			# print('ib', i)
			i = i+1
			# print('i:',i)
		else:
			print(tens_dict[x[i]])
	# elif x[i] == "million":
	# 	print("million")

	# elif x[i] == "thousand":
	# 	print("thousand")
	else:
		print("bye")
'''



# for i in x:
# 	# print(i)
# 	if i in ones_dict:
# 		print(i)
		
	# if i in ones_dict or tens_dict:
	# 	print(i)
	# if i == "thousand":
	# 	print("some thousands")


	# if i in ones_dict:
	# 	print(ones_dict[i])

	# print(number_example.split())
	# word_list.append(i)
	# if i == ' ':
	# 	print("there is a space")
	# 	print(word_list)
		# word_list = word_list[0]
		# if word_list in ones_dict:
		# 	print(ones_dict[word_list])


	# print(type(i))
	# print(number_example[0])


		# for i in number_example:
		# 	if i in ones_dict:
		# 		print(ones_dict[i])




	# if i == ' ':
	# 	print("there is a space")
	# print(i)




x = ["three", "hundred", "million", "thirty", "four", "thousand"]
total = 0
for i in range(len(x)-1):  
	print(i)
	if x[i+1] == "million":
		total = x[i]*1000 + total
		print(total)
	# elif:











