import os
import re
from collections import defaultdict

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def create_inverted_index(directory):
    inverted_index = defaultdict(list)
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                tokens = tokenize(text)
                for pos, token in enumerate(tokens):
                    inverted_index[token].append((filename, pos))
    return inverted_index

def search_inverted_index(query, inverted_index):
    query_tokens = tokenize(query)
    results = defaultdict(list)
    for token in query_tokens:
        if token in inverted_index:
            for filename, pos in inverted_index[token]:
                results[filename].append(pos)
    return results

def main():
    directory = 'text_files'
    inverted_index = create_inverted_index(directory)
    
    while True:
        query = input("Enter search query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        search_results = search_inverted_index(query, inverted_index)
        for filename, positions in search_results.items():
            print(f"Found in {filename} at positions {positions}")
        if not search_results:
            print("No results found")

if __name__ == "__main__":
    main()
