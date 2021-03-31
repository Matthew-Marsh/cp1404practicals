"""
Program will request a sentence from the user and count the number of occurrences of each word
before printing a sorted dictionary
"""

sentence = input("Text: ").lower()
words = sentence.split()

word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

maximum_word_length = max([len(word) for word in words])
for word in sorted(word_to_count):
    print("{:{}} : {}".format(word, maximum_word_length, word_to_count[word]))
