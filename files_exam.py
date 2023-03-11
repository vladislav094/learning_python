#1
# with open(input(), 'r', encoding='utf-8') as file:
#     arr = file.readlines()
#     print(len(arr))


#2
# with open('students.txt', 'r', encoding='utf-8') as file:
# 	arr = file.readlines()
# 	arr = [int(x.replace('$', '')) for x in arr]
# 	print(f"${sum(arr)}")

#3
with open('students.txt', 'r', encoding='utf-8') as file:
	arr = file.readlines()
	count = 0
	for elt in arr:
		person = elt.split()[1:]
		person = [int(x) for x in person]
		if all([x >= 65 for x in person]):
			count +=1
	print(count)