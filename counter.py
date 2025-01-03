import re
from collections import Counter

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    # Use regular expressions to find words (considering alphanumeric words and ignoring case)
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def main():
    # Replace 'your_file.txt' with the path to your file
    file_path = 'your_file.txt'
    text = read_file(file_path)
    word_counts = count_words(text)

    # Print word counts in descending order of frequency
    print("Word Frequency Count:")
    print("---------------------")
    for word, count in word_counts.most_common():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
