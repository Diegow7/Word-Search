import os
import tkinter as tk
from tkinter import messagebox

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

def search_word():
    word_to_search = entry_word.get()
    results = search_word_in_files(word_to_search, "Data")
    if results:
        result_str = f"The word '{word_to_search}' is found in the following books:\n"
        for book, occurrences in results.items():
            result_str += f"- {book}: {occurrences} times\n"
        messagebox.showinfo("Search Results", result_str)
    else:
        messagebox.showinfo("Search Results", f"The word '{word_to_search}' was not found in any of the books.")

# Create GUI
root = tk.Tk()
root.title("Word Search")

bg_color = "#f0f0f0"
fg_color = "#333333"
font_style = ("Helvetica", 12)

root.configure(bg=bg_color)

label_word = tk.Label(root, text="Enter the word you want to search for:", bg=bg_color, fg=fg_color, font=font_style)
label_word.pack()

entry_word = tk.Entry(root, font=font_style)
entry_word.pack()

button_search = tk.Button(root, text="Search", command=search_word, bg="#4CAF50", fg="white", font=font_style)
button_search.pack(pady=10)

root.mainloop()