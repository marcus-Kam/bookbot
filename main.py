from stats import word_count, count_characters, sort_dictionary
import sys
def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents
def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	bookpath = sys.argv[1]
	try:
		text = get_book_text(bookpath)
	except:
		print("No file was found")
		sys.exit(1)
	num_words = word_count(text)
	characters = count_characters(text)
	sorted_characters = sort_dictionary(characters)
	print(f"Found {num_words} total words")
	for dict in sorted_characters:
		print(f"{dict["char"]}: {dict["num"]}") 
main()
