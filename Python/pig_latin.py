# Martyr2's Mega Project List

# Pig Latin
# Initial Consonant sound is transposed to the endof the word
# an ay is affixed to it. Ex. banana = anana-bay
# There are intricacies that are purely vocal that have not been accounted for.
# Account for null (later)

ay = 'ay'
consonant = {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q',
             'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'}
vowel = {'A', 'E', 'I', 'O', 'U'}


def pig_latin(text):
    first_letter = example[0].upper()

    if first_letter in consonant:
        counter = 0
        while first_letter in consonant:
            counter += 1
            first_letter = example[counter].upper()

        print('The word {} being with these consonants: {}'.format(text, text[:counter]))
        print("Translation: " + example[counter:] + "-" + example[:counter] + ay)
    elif first_letter in vowel:
        print('The word {} beings with this vowel: {}'.format(text, text[0]))
        print('Translation: {}{}'.format(example, '-hay'))
    else:
        print("I couldn't even understand that.")


example = input("What would you like anslated-tray?: ")
pig_latin(example)
