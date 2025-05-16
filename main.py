from stats import get_word_count
from stats import get_character_count

def get_book_text(book):
	with open(book) as f:
		book_contents = f.read()
	get_word_count(book_contents)
	get_character_count(book_contents)
			
def main():
	book = "books/frankenstein.txt"
	get_book_text(book)



main()	