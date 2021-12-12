# Unit 5 Assignment
##Application - Level 4+

import random

# Reading from a file
numFile = open("ranks.dat", "r")

# list fields
rankList = []
powerList = []
numberList = []

# lists of decks
deckList = []
firstPlayerDeck = []
secondPlayerDeck = []
overflowDeck = []

#Separates each part of information from ranks.dat
while True:
    text = numFile.readline()            ##reads the line
    text = text.rstrip("\n")             ##rstrip removes the newline character read at the end of the line 
    if text=="":                         ##explains that if there is no text, the data is complete
        break
    info = text.split(",")               ##shows that all the information is divided by commas
    rankList.append(info[0])             ##adds the first section of the text to the list rankList
    powerList.append(int(info[1]))       ##adds the second section of the text to the list powerList
    numberList.append(int(info[2]))      ##adds the third section of the text to the list numberList
    tempList = [info[0]] * int(info[2])  ##tempList is a list to ensure that each rank as its corresponding number of cards
    deckList.extend(tempList)            ##adds the corresponding number of the rank to the deck
numFile.close()
numCards = len(deckList)                 ##to find number of cards
numGames = 0                             ##to define the number of games

#Game Title
print("                 WELCOME TO THE GAME OF WAR!") ##displays title
print("<>"*31)                                        ##divider
print()                                               ##spaces out the next subtitle

def create_game(deckList):
    firstPlayerDeck = []                         ##empties deck for the preceding round so that the deck begins with no cards 
    secondPlayerDeck = []                        ##empties deck for the preceding round so that the deck begins with no cards    
    if numGames == 0:                            ##creates the guidline that this is the first game for the following to be executed and displayed to the user
        #Displays the Prerequisite Knowledge
        print("="*61)                                     ##Border
        print("                  Level 2: Prerequisites") ##Title
        print("="*61)                                     ##Border
        ##Organizes each rank, power, and number in a table-like fashion
        print("Rank\t\t\tSkill\t\t\tNumber")              ##Table Organizer
        print("-"*61)                                     ##Border
        ##table information
        for i in range(len(rankList)):
            print("%-15s\t\t %2i\t\t         %2i" %(rankList[i], powerList[i], numberList[i]))
        print()                                  ##spaces out the next subtitle
        #Displaying the Deck
        print ("="*61)                                     ##Border
        print ("                Level 3 Part I: The Deck") ##Title
        print ("="*61)                                     ##Border
        print(deckList)                                    ##displays the deck list
        print ("There are %i cards in the deck" %numCards) ##displays the number of cards in the deck
        print()                                            ##spaces out the next subtitle
        #Dealing the Cards
        print ("="*61)                                      ##Border
        print ("                 Level 3 Part II: Dealing") ##Title
        print ("="*61)                                      ##Border
        random.shuffle(deckList)                               ##Creates a random decklist for both players
        for i in range (0, numCards, 2):                       ##ensures that every other card is choses so that the card of player 1 and player 2 don't overlap
            firstPlayerHand = deckList[i]                      ##puts every other card in the shuffled deck in the first player's list
            firstPlayerDeck.append(firstPlayerHand)
            print ("Player 1 is dealt: %s." %firstPlayerHand)  ##displays every time player 1 gets a card
            secondPlayerHand = deckList[i+1]                   ##puts every other remaining card in the shuffled deck in the second player's list
            secondPlayerDeck.append(secondPlayerHand)        
            print ("Player 2 is dealt: %s." %secondPlayerHand) ##displays every time player 2 gets a card
        ##displays complete deck for player 1
        print("Player 1 deck:") 
        print(firstPlayerDeck)
        ##displays complete deck for player 2
        print("Player 2 deck:")
        print(secondPlayerDeck)
        print()                                                ##spaces out the next subtitle
        overflowDeck = []
        #Playing the Game
        print ("="*61)                                     ##Border
        print ("                 Level 4 Part I: Playing") ##Title
        print ("="*61)                                     ##Border
        for i in range (len(firstPlayerDeck)):                     ##makes the length half of the deck since half was given to each player
            firstPlayerRank = firstPlayerDeck[0]                   ##makes the rank related to the first card in the first player's deck
            del firstPlayerDeck[0]                                 ##deletes the corresponding card to make sure there is no card duplication
            firstPlayerIndex = rankList.index(firstPlayerRank)     ##Creates a variable firstPlayerIndex by directly going into the list for ranks
            firstPlayerPower = powerList[firstPlayerIndex]         ##Finds the first player's power by using their index and going into the list for power
            secondPlayerRank = secondPlayerDeck[0]                 ##makes the rank related to the first card in the second player's deck
            del secondPlayerDeck[0]                                ##deletes the corresponding card to make sure there is no card duplication
            secondPlayerIndex = rankList.index(secondPlayerRank)   ##Creates a variable secondPlayerIndex by directly going into the list for ranks
            secondPlayerPower = powerList[secondPlayerIndex]       ##Finds the second player's power by using their index and going into the list for power
            if firstPlayerPower == secondPlayerPower:              ##creates the outline that the powers of the first player and the second player should be the same
                print("It's a tie! They are added to the overflow deck!") ##displays the tie to the user
                ##saves both cards into the overflow deck
                overflowDeck.append(firstPlayerRank)
                overflowDeck.append(secondPlayerRank)
            elif firstPlayerPower > secondPlayerPower:                                               ##creates the outline that the power of player 1 is larger than that of of player 2
                print("%s beats %s, the cards go to player 1." %(firstPlayerRank, secondPlayerRank)) ##displays the victory of player 1
                ##adds all cards to the deck of player 1
                firstPlayerDeck.append(firstPlayerRank)
                firstPlayerDeck.append(secondPlayerRank)
                firstPlayerDeck.extend(overflowDeck)
                overflowDeck = []                                                                    ##empties out the cards in the overflow deck after putting them in the first player's deck
            else:                                                                                    ##creates the outline of the remaining possibility of power comparison (power of player 2 is larger than that of player 1)
                print("%s beats %s, the cards go to player 2." %(secondPlayerRank, firstPlayerRank)) ##displays the victory of player 2
                ##adds all card to the deck of player 2
                secondPlayerDeck.append(firstPlayerRank)
                secondPlayerDeck.append(secondPlayerRank)
                secondPlayerDeck.extend(overflowDeck) 
                overflowDeck = []                                                                    ##empties out the cards in the overflow deck after putting them in the second player's deck    
        print("Game Over.")                                                                          ##lets the user know that the game is completed
        print()                                                                                      ##spaces out the next subtitle
        #The Game Recap
        print ("="*61)                                      ##Border
        print ("              Level 4 Part II: Game Recap") ##Title
        print ("="*61)                                      ##Border  
        firstPlayerNumCards = len(firstPlayerDeck)                   ##finds the number of cards in the first player's deck
        secondPlayerNumCards = len(secondPlayerDeck)                 ##finds the number of cards in the second player's deck
        overflowNumCards = len(overflowDeck)                         ##finds the number of cards in the overflow deck
        ##displays the game summary to the user
        print("Player 1 has %i cards." %firstPlayerNumCards)
        print("Player 2 has %i cards." %secondPlayerNumCards)
        print("There are %i cards in the overflow deck." %overflowNumCards)
        print()                                                      ##spaces out the next subtitle
        deck = []
        return firstPlayerNumCards, secondPlayerNumCards, overflowNumCards
    
    if numGames != 0:                               ##creates the guidline that this must not be the first game for the following to be executed and for nothing to be displayed to the user
        firstPlayerDeck = []                        ##empties deck for the preceding round so that the deck begins with no cards
        secondPlayerDeck = []                       ##empties deck for the preceding round so that the deck begins with no cards
        overflowDeck = []                           ##empties deck for the preceding round so that the deck begins with no cards
        #Dealing the Cards
        random.shuffle(deckList)                    ##Creates a random decklist for both players
        for i in range (0, numCards, 2):            ##ensures that every other card is choses so that the card of player 1 and player 2 don't overlap
            firstPlayerHand = deckList[i]           ##puts every other card in the shuffled deck in the first player's list
            firstPlayerDeck.append(firstPlayerHand)
            secondPlayerHand = deckList[i+1]        ##puts every other remaining card in the shuffled deck in the second player's list
            secondPlayerDeck.append(secondPlayerHand) 
        #Playing the Game
        for i in range (len(firstPlayerDeck)):                     ##makes the length half of the deck since half was given to each player
            firstPlayerRank = firstPlayerDeck[0]                   ##makes the rank related to the first card in the first player's deck
            del firstPlayerDeck[0]                                 ##deletes the corresponding card to make sure there is no card duplication
            firstPlayerIndex = rankList.index(firstPlayerRank)     ##Creates a variable firstPlayerIndex by directly going into the list for ranks
            firstPlayerPower = powerList[firstPlayerIndex]         ##Finds the first player's power by using their index and going into the list for power
            secondPlayerRank = secondPlayerDeck[0]                 ##makes the rank related to the first card in the second player's deck
            del secondPlayerDeck[0]                                ##deletes the corresponding card to make sure there is no card duplication
            secondPlayerIndex = rankList.index(secondPlayerRank)   ##Creates a variable secondPlayerIndex by directly going into the list for ranks
            secondPlayerPower = powerList[secondPlayerIndex]       ##Finds the second player's power by using their index and going into the list for power
            if firstPlayerPower == secondPlayerPower:              ##creates the outline that the powers of the first player and the second player should be the same
                ##saves both cards into the overflow deck
                overflowDeck.append(firstPlayerRank)
                overflowDeck.append(secondPlayerRank)
            elif firstPlayerPower > secondPlayerPower:             ##creates the outline that the power of player 1 is larger than that of of player 2
                ##adds all cards to the deck of player 1
                firstPlayerDeck.append(firstPlayerRank)
                firstPlayerDeck.append(secondPlayerRank)
                firstPlayerDeck.extend(overflowDeck)
                overflowDeck = []                                  ##empties out the cards in the overflow deck after putting them in the first player's deck
            else:                                                  ##creates the outline of the remaining possibility of power comparison (power of player 2 is larger than that of player 1)
                ##adds all card to the deck of player 2
                secondPlayerDeck.append(firstPlayerRank)
                secondPlayerDeck.append(secondPlayerRank)
                secondPlayerDeck.extend(overflowDeck) 
                overflowDeck = []                                  ##empties out the cards in the overflow deck after putting them in the second player's deck    
    firstPlayerNumCards = len(firstPlayerDeck)                     ##finds the number of cards in the first player's deck
    secondPlayerNumCards = len(secondPlayerDeck)                   ##finds the number of cards in the second player's deck
    overflowNumCards = len(overflowDeck)                           ##finds the number of cards in the overflow deck
    return firstPlayerNumCards, secondPlayerNumCards, overflowNumCards ##returns the number of cards in each deck to use further in the Summary Chart 


# Summary Chart of the Games   
firstPlayerNumCardsTotal = 0    ##portrays the present amount of total cards player 1 has
secondPlayerNumCardsTotal = 0   ##portrays the present amount of total cards player 2 has
overflowNumCardsTotal = 0       ##portrays the present amount of total cards the overflow deck has
while numGames < 10:            ##ensures that only ten games are played
    firstPlayerNumCardsTemp, secondPlayerNumCardsTemp, overflowNumCardsTemp = create_game(deckList) ##returns the variables pretaining to the function
    firstPlayerNumCardsTotal += firstPlayerNumCardsTemp     ##ensures that the total number of cards that the player has is being generated further in each new round
    secondPlayerNumCardsTotal += secondPlayerNumCardsTemp   ##ensures that the total number of cards that the player has is being generated further in each new round
    overflowNumCardsTotal += overflowNumCardsTemp           ##ensures that the total number of cards that the player has is being generated further in each new round
    if numGames == 0:
        print("="*61)                                                       ##Border
        print("          Level 4+: Summary Chart of Total Games")           ##Title
        print("="*61)                                                       ##Border
        print("Game Number\tPlayer 1 Cards\tPlayer 2 Cards\tOverflow Deck") ##Table Organizer
        print("-"*61)                                                       ##Border
    numGames += 1                                                           ##ensures that the number of games always increases
    ##displays the important imformation in a table format
    print("    %2i\t\t     %2i\t\t      %2i\t      %i" %(numGames, firstPlayerNumCardsTemp, secondPlayerNumCardsTemp, overflowNumCardsTemp))
firstPlayerNumCardsAvg = firstPlayerNumCardsTotal/10                        ##finds the average number of cards for player 1
secondPlayerNumCardsAvg = secondPlayerNumCardsTotal/10                      ##finds the average number of cards for player 2
overflowNumCardsAvg = overflowNumCardsTotal/10                              ##finds the average number of cards for the the overflow deck
##displays the averages in the same table format
print("Average\t\t    %.1f\t     %.1f\t     %.1f" %(firstPlayerNumCardsAvg, secondPlayerNumCardsAvg, overflowNumCardsAvg))
print()

#Game Ending
print()                                                   ##Helps with spacing
print("<>"*31)                                            ##Divider
print("          THANK YOU FOR PLAYING THE GAME OF WAR!") ##This is displayed to the user