path = "books/frankenstein.txt"

# print contents of file at path

def main (path):
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)

main(path)
