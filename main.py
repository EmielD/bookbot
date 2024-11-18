def sort_on(dict):
	return dict["num"]

def generate_report(input_text, book_path):
	print(f"--- Begin report of {book_path} ---")
	print(f"{count_words(input_text)} words found in the document")
	print("\n")

	count_characters_list = count_characters(input_text)
	count_characters_list.sort(reverse=True, key=sort_on)

	for character in count_characters_list:
		print(f"The '{character['char']}' character was found {character['num']} times")

	print("\n")
	print("--- End report ---")

def count_characters(input_text):
	characters_dictionary = {}

	for character in input_text:
		if character.isalpha():
			if character not in characters_dictionary:
				characters_dictionary[character] = 1
			else:
				characters_dictionary[character] += 1

	characters_list = [{"char": character, "num": count} for character, count in characters_dictionary.items()]

	return characters_list

def count_words(input_text):
	words_amount = len(input_text.split())
	return words_amount

def main():
	book_path = "books/frankenstein.txt"
	with open(book_path) as f:
		file_contents = f.read().lower()
		generate_report(file_contents, book_path)

main()
