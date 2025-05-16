def get_word_count(book_contents):
		word_list = book_contents.split()
		word_count = 0
		for words in word_list:
			word_count += 1
		print(f"{word_count} words found in the document")

def get_character_count(book_contents):
		lower_book_contents = book_contents.lower()
		char_list = list(lower_book_contents)
		character_count = {}
		for char in char_list:
			if char in character_count:
				character_count[char] += 1
			else:
				character_count[char] = 1
		print(character_count)

		