#1
# with open(input(), 'r', encoding='utf-8') as file:
#     arr = file.readlines()
#     print(len(arr))


#2
with open('students.txt', 'r', encoding='utf-8') as file:
	arr = file.readlines()
	arr = [int(x.replace('$', '')) for x in arr]
	print(f"${sum(arr)}")