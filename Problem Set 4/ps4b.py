from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0

    # Create a new variable to store the best word seen so far (initially None) 
    best_word = None 

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if canWord(word, hand):
    
            # Find out how much making that word is worth
            word_score = getWordScore(word, n)

            # If the score for that word is higher than your best score
            if word_score > max_score:

                # Update your best score, and best word accordingly
                max_score = word_score
                best_word = word

    # return the best word you found.
    return best_word
    
# define the function canWord
def canWord(word, hand):
    letters = getFrequencyDict(word)

    for c in letters:
        if letters[c] > hand.get(c, 0):
            return False

    return True

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    # Keep track of the total score
    score = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) != 0:
    
        # Display the hand
        print "Hand: ", displayHand(hand)
        
        # The computer chooses a word
        word = compChooseWord(hand, wordList, n)
        
        # If compChooseWord returns None:
        if word == None:
        
            # End the game (break out of the loop)
            break
        
        # Otherwise, update the score
        else:
            word_score = getWordScore(word, n)
            score += word_score
            
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            print "Computer earned " + str(word_score) + " points with the word " + word +". Total score: " + str(score) + " points.\n"
                
            # Update the hand 
            hand = updateHand(hand, word)
        
        # The computer has no choice left
        print "Total score: " + str(score) + " points.\n"
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    # initialize the game
    hand = None
    choice = raw_input("Enter n to play a new hand, r to replay the last hand, or e to exit: ")
    print
    
    # as long as he has not exited
    while choice != "e":
        
        # if he chooses to start a new hand
        if choice == "n":
            # deal a new hand
            hand = dealHand(HAND_SIZE)
                            
        # if he chooses to replay his hand
        elif choice == "r":
            # if he never played a hand, tell him to
            if hand == None:
                print "You have not played a hand yet. Start a new hand.\n"
                choice = raw_input("Enter n to play a new hand, r to replay the last hand, or e to exit: ")
                print
                continue
        
        # if he types something different, tell him
        else:
            print "Invalid command."
            choice = raw_input("Enter n to play a new hand, r to replay the last hand, or e to exit: ")
            print
            continue
            
        # prompt the user to choose the player
        player = raw_input("Enter u to play, or c to make the computer play")
        
        # if he types something different, tell him
        while player != "u" and player != "c":
            print "Invalid command."
            player = raw_input("Enter u to play, or c to make the computer play")
        
        # if he types 'u', make him play
        if player == "u":
            playHand(hand, wordList, HAND_SIZE)
        # else make the computer play
        else:
            compPlayHand(hand, wordList, HAND_SIZE)

        choice = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        print
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)