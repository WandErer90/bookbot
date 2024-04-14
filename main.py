path = "books/frankenstein.txt"

# read file from path

def main (path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

# return word count from file

def word_count(file_contents):
    word_count = 0
    words = main(file_contents).split()
    for i in range(0,len(words) + 1):
        word_count = i
    print(word_count)

word_count(path)
