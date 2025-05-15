def get_word_count(book_contents):
		word_list = book_contents.split()
		word_count = 0
		for words in word_list:
			word_count += 1
		print(f"{word_count} words found in the document")