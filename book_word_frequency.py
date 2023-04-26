# There is a coding challenge I use in my own interviews, described below
# I don't write a lot of python, so I figured I would try it out myself here 
# Challenge: You have a book (a block of text, no images) and a target word as an input.
# Write a method to determine the number of times that the target word appears in the input text.
# What if the method was run multiple times for the same book, but different target words?

# Algorithm: Read the input text into a dictionary. Read word by word, and each time a word is encountered, either:
# - Insert a new word to the overall dictionary, with a count of 1
# - Increment the count of an existing word
# When complete, check the dictionary for the target word

# Defining a method to return the (currently) hard coded input book
def getBook(): 
    return "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of light, it was the season of darkness, it was the spring of hope, it was the winter of despair."

def handleWord(inWord): # clean / remove punctuation from an individual word
    noWhitespace = inWord.strip() # strip the specified character (if any is provided as an argument), or remove all whitespace otherwise 
    noComma = noWhitespace.rstrip(",") # rstrip, or right-side strip. Removes the specified character from the end of the string
    strippedWord = noComma.rstrip(".") # removing the . character, if it is there. If not, no change to the input. "winter" -> "winter", but "despair." -> "despair"
    upperWord = strippedWord.upper() # make the word uppercase, to standardize. To python (the language), "Rabbit" != "RABBIT" != "rabbit"
    return upperWord # technically, could just return strippedWord.upper(), but did that for clarity

def splitBookToList(inBook): # split the individual book into individual words
    return inBook.split() # by default, any whitespace like space, tab, or newline character will be caught by the split() method (I had to look that up)

def addWordToDictionary(word, dict):
    if(word in dict):
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1

def processBookIntoIndex(book, wordCountIndex):
    wordList = splitBookToList(book)
    for word in wordList:
        temp = handleWord(word)
        addWordToDictionary(temp, wordCountIndex) 

def printWordIndex(dict):
    print("Dictionary Contents:\n")
    for word in dict:
        print("Word: '" + word + "' Count: " + str(dict[word]) + "\n")

def main():
    # Defining the variables used in this method
    wordCountIndex = {}
    targetWord = "AGE"
    book = getBook()

    processBookIntoIndex(book, wordCountIndex)
    print("Finished processing book into word index")
    printWordIndex(wordCountIndex)
    
    print ("\nTarget word: '" + targetWord + "', count: " + str(wordCountIndex[targetWord]))
    print("End of 1st test, changing target word to 'epoch' \n")
    targetWord = "EPOCH"
    
    print ("\nTarget word: '" + targetWord + "', count: " + str(wordCountIndex[targetWord]))
    print("End of 2nd test, changing target word to 'was' \n")
    targetWord = "WAS"

    print ("\nTarget word: '" + targetWord + "', count: " + str(wordCountIndex[targetWord]))

main()