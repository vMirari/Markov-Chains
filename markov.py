"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_text = open(file_path).read()
    return file_text.replace("\n"," ") #contents of your file as one long string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

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
    count = 0 
    words = text_string.split()
   
 

    for count in range(len(words)-2): 
        key = (words[count], words[count + 1])
        value = words[count + 2]
        
        
        if key in chains:
            chains[key].append(value)
        else:
            chains[key]=[value]

    #hardcoding  the last two items of the list do we are not out of range in out for loop 
    chains[( words[-2], words[-1] )] = [None]
   


        

    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    
    current_key = choice(chains.keys()) #this finds a random key, our tuple in our our chains dictionary 
   # print starting_key[0], starting_key[1] # this finds a tuple in that random key that we chose 
    chosen_word = choice(chains[current_key])

    words.extend(current_key)
   
    while chosen_word is not None:
        words.append(chosen_word)
        current_key = (words[-2],words[-1])
        chosen_word = choice(chains[current_key])
        #words.extend(current_key)
       

 



    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
