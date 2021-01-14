# Count Vowels
# Enter a string - count the vowels.
# Extra: Have it report a sum of each vowel found.

vowel = {
    'A': 0,
    'E': 0,
    'I': 0,
    'O': 0,
    'U': 0}

example = input("Give me a word or sentence: ")

if ' ' in example:
    new_example = example.split()
    for word in new_example:
        for x in range(len(word)):
            if word[x].upper() in vowel:
                vowel[word[x].upper()] += 1
else:
    for x in range(len(example)):
        if example[x].upper() in vowel:
            vowel[example[x].upper()] += 1


print('Number of vowels in phrase: {}'.format(example))
[print(key, value) for key, value in vowel.items()]
