import os

def search_word_in_files(word, folder):
    books_with_word = {}
    for file in os.listdir(folder):
        if file.endswith('.txt'):
            file_path = os.path.join(folder, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                occurrences = content.lower().count(word.lower())
                if occurrences > 0:
                    books_with_word[file] = occurrences
    return books_with_word

def main():
    word_to_search = input("Enter the word you want to search for: ")
    data_folder = "Data"
    results = search_word_in_files(word_to_search, data_folder)
    if results:
        print(f"The word '{word_to_search}' is found in the following books:")
        for book, occurrences in results.items():
            print(f"- {book}: {occurrences} times")
    else:
        print(f"The word '{word_to_search}' was not found in any of the books.")

if __name__ == "__main__":
    main()