# find the longest word using a for loop
words = ['orange','umbrella','apple','trailer']

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)


