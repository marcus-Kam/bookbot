def word_count(filetext):
        split_filetext = []
        split_filetext = filetext.split()
        return len(split_filetext)
def count_characters(filetext):
	lowercase_filetext = filetext.lower()
	character_count = {}
	for char in lowercase_filetext:
		if char in character_count:
			character_count[char] += 1
		else:
			character_count[char] = 1
	return character_count
def get_num(dict):
	return dict["num"]
def sort_dictionary(dictionary):
	new_list = []
	for character in dictionary:
		if character.isalpha() == True:
			new_list.append({"char": character,"num": dictionary[character]})
	new_list.sort(reverse=True, key=get_num)
	return new_list
		
