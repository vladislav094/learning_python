def ave_caesar(word: str) -> str:
	new_word = []
	for elt in word.split():
		ss = ''
		x = len([c for c in elt if c.isupper() or c.islower()])
		for j in elt:
			if j.isupper():
				ss += chr((ord(j) + x - 65) % 26 + 65)
			elif j.islower():
				ss += chr((ord(j) + x - 97) % 26 + 97)
			else:
				ss += j
		new_word.append(ss)
	return ' '.join(new_word)
word = input()
print(ave_caesar(word))

