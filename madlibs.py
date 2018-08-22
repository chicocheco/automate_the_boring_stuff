#! python3

def mad_libs():
    """
    Reads text files and lets the user add their own text anywhere
    the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

    Bug to fix: It replaces 'VERB.' for a verb with the dot missing...
    """
    filler = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
    answer = []

    file = open('madlibs.txt', 'r')  # Open the text file from the CWD in reading mode.
    content = file.read().split()  # Make a list of words_capital (in text separated by whitespaces).

    for word in content:
        if word.strip('.!?,') in filler:
            # Return a copy of the string with the leading and trailing characters removed. 'NOUN.' -> 'NOUN'
            answer.append(input(f'Enter a {word}: '))
            # The user inputs a word to replace and the loop continues. {0} is part of the .format() method.
        else:
            answer.append(word)
            # If there is not a string ADJECTIVE, NOUN, ADVERB or VERB then simply append the word to the list 'answer'.

    file = open('madlibs_new.txt', 'w')
    file.write(' '.join(answer))
    file.close()


mad_libs()
