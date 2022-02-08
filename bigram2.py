# Updated Feb 11
#
# Word bigrams are just pairs of words.
# In the sentence "I went to the beach"
# the bigrams are:
#    I went
#    went to
#    to the
#    the beach
#
# Having counts of English bigrams from a very large text corpus
# can be useful for a number of purposes.
#
# for example for spelling correction:
# If I had mistyped the sentence as "I went to beach"
# then I might be able to find the error by seeing that
# the bigram "to beach" has a very low count, and
# "to the", "to a", and "the beach" have much larger counts.
#
# This program counts all word bigrams in a given text file


###############################################################
# ToDO: Extend it for nigram, bigram, trigrams
################################################################

import string
import sys


# count bigrams
def count_bigrams(filecontents):
    bigrams = {}
    words_punct = filecontents.split()
    # strip all punctuation at the beginning and end of words, and
    # convert all words to lowercase.
    # The following is a Python list comprehension. It is a command that transforms a list,
    # here words_punct, into another list.
    words = [ w.strip(string.punctuation).lower() for w in words_punct ]

    # add special START, END tokens
    words = ["START"] + words + ["END"]

    for index, word in enumerate(words):
        if index < len(words) - 1:
            # we only look at indices up to the
            # next-to-last word, as this is
            # the last one at which a bigram starts
            w1 = words[index]
            w2 = words[index + 1]
            # bigram is a tuple,
            # like a list, but fixed.
            # Tuples can be keys in a dictionary
            bigram = (w1, w2)

            if bigram in bigrams:
                bigrams[ bigram ] = bigrams[ bigram ] + 1
            else:
                bigrams[ bigram ] = 1
            # or, more simply, like this:
            # bigrams[bigram] = bigrams.get(bigram, 0) + 1
    return bigrams


# sort bigrams by their counts
def sort_bigrams(bigrams):
    sorted_bigrams = sorted(bigrams.items(), key = lambda pair:pair[1], reverse = True)
    for bigram, count in sorted_bigrams:
        print(bigram, ":", count)


if __name__ == "__main__" :
    input_file_name = input("Please enter the name of a corpus file as a input:")
    # try opening file
    # If the file doesn't exist, catch the error
    try:
        f = open(input_file_name)
    except IOError:
        print("Sorry, I could not find the file", input_file_name)
        print("Please try again.")
        sys.exit()

    # read the contents of the whole file into ''filecontents''
    filecontents = f.read()
    #unigrams = count_unigrams()
    bigrams = count_bigrams(filecontents)
    sort_bigrams(bigrams)
    #TODO
    # Do the same thing for counting unigrams,trigrams
    #trigrams = count_trigrams()
    #find 10 most frequent unigram, bigram, trigrams


