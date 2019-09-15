import re

dicts = []
file = open('dict.txt', 'r', encoding='utf-8')
for line in file:
	dicts.append(line.split("\n")[0])

def get_letter(search, exclude):
	search_list = [x for x in search + exclude]
	if "*" not in search_list:
		return "Word mask must contain \"*\""

	exc = "."
	used = (search + exclude).lower().replace('*', '')	
	if used: exc = f"[^{used}]"

	stat = dict()
	patt = f"^{search.replace('*', exc)}$"

	for word in dicts:
		result = re.search(patt, word)
		if result is None:
			continue

		letters_in_word = []
		for letter in word:
			if letter not in letters_in_word and letter not in search_list:
				if letter not in stat: stat[letter] = 0
				stat[letter] += 1
				letters_in_word.append(letter)

	stat = list(stat.items())
	stat.sort(key=lambda i: i[1], reverse=True)
	if not stat:
		return "Cant find similar word in base!"
	return stat[0][0]

print(get_letter("ап*ль**н", "кр")) # апельсин