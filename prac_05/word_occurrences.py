"""
Word Occurrences
Estimate: 15 minutes
Actual: 22 minutes
"""

string = input("Text: ")
word_to_count = {}
for word in list(sorted(string.split())):
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = word_to_count.get(word, 0) + 1
max_length = max(len(word) for word in list(word_to_count.keys()))
for word, count in word_to_count.items():
    print(f"{word:{max_length}} : {count}")