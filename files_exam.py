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
# with open('students.txt', 'r', encoding='utf-8') as file:
# 	arr = file.readlines()
# 	count = 0
# 	for elt in arr:
# 		person = elt.split()[1:]
# 		person = [int(x) for x in person]
# 		if all([x >= 65 for x in person]):
# 			count +=1
# 	print(count)


#4
# with open('students.txt', 'r', encoding='utf-8') as file:
# 	arr = file.read()
# 	len_max = max([len(x) for x in arr.split()])
# 	for elt in arr.split():
# 		if len(elt) == len_max:
# 			print(elt)

#5
# with open('students.txt', 'r', encoding='utf-8') as file:
# 	arr = file.readlines()
# 	start = len(arr) - 10
# 	if len(arr) < 10:
# 		for elt in arr:
# 			print(elt, end='')
# 	else:
# 		for elt in range(start, len(arr)):
# 			print(arr[elt], end='')

#6
with open('forbidden_words.txt') as forbidden_words, open(input()) as to_change:
	pattern, text = forbidden_words.read().split(), to_change.read()
text_lower = text.lower()
for word in pattern:
	text_lower = text_lower.replace(word, '*' * len(word))
result = ''.join((y, x)[x == '*'] for x, y in zip(text_lower, text))
print(result)