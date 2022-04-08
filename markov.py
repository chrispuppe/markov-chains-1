"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # your code goes here
    file_contents = open(file_path).read()

    return file_contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    individual_words = text_string.split()

    individual_words.append(None)

    for i in range(len(individual_words) - 2):
        key = (individual_words[i], individual_words[i+1])
        value = individual_words[i+2]
        
        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    random_word = choice(chains[key])

    while random_word is not None:
        key = (key[1], random_word)
        words.append(random_word)
        random_word = choice(chains[key])

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
