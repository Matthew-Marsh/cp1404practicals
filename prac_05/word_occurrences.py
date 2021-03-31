sentence = input("Text: ").lower()
words = sentence.split()

word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

maximum_word_length = max([len(word) for word in words])
words = [word for word in word_to_count]
for word in sorted(words):
    print("{:{}} : {}".format(word, maximum_word_length, word_to_count[word]))

