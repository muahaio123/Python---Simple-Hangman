import random

# import only system from os
from os import system, name
  
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals and fruits
words_animals = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

words_fruits = ('apple apricot avocado banana berry blackberry bloodorange blueberry boysenberry breadfruit '
                'cantaloupe cherry citron citrus coconut crabapple cranberry current date dragonfruit durian elderberry fig '
                'grape grapefruit guava honeydew jackfruit kiwi kumquat lemon lime lingonberry loquat lychee '
                'mandarin mango marionberry melon mulberry '
                'nectarine orange papaya passionfruit peach pear persimmon pineapple plantain plum pluot pomegranate pomelo prune '
                'quince raisin raspberry starfruit strawberry tangelo tangerine uglifruit watermelon').split()

words_countries = ('afghanistan armenia azerbaijan bahrain bangladesh bhutan brunei '
                   'cambodia china cyprus easttimor georgia india indonesia iran iraq israel '
                   'japan jordan kazakhstan kuwait kyrgyzstan laos lebanon malaysia maldives mongolia myanmar '
                   'nepal northkorea oman pakistan palestine philippines qatar russia saudiarabia singapore southkorea srilanka syria '
                   'taiwan tajikistan thailand turkey turkmenistan unitedarabemirates uzbekistan vietnam yemen ').split()

words_bank = (words_animals, words_fruits, words_countries) # combine the word bank to simplify code

again = 'y' # if the player wants to try again

while again == 'y':
    clear() # clearing the screen for another try
    topic = -1
    
    # initialize everything needed for the game
    while not (topic >= 0 and topic <= 2):
        topic = int(input("Please choose your topic: 0 for ANIMALS | 1 for FRUITS | 2 for ASIAN COUNTRIES: "))

    word_chosen = random.choice(words_bank[topic])

    print("A word has been chosen. You now have 6 lives!")
    #print(word_chosen) # debugging purpose

    # initialize the output for the user that their word has this many characters hidden
    output = []
    for c in word_chosen:
        output += '_'

    lives = 0 # how many lives the player have spent
    user = [] # a list of all the characters the user have inputted
    
    while '_' in output and lives < 6: # during the game
        print(HANGMANPICS[lives]) # print the ucrrent status of the hangman
        print(' '.join(output)) # print the words guess corrected

        input_char = input("\nPlease make your choice - a character at a time: ").lower()

        while input_char in user: # prompt for another char if the user already input a previous char
            input_char = input(f"You have tried {input_char} already! Please try again with another character: ")
            
        user.append(input_char)
        
        if not input_char in word_chosen: # wrong char has been inputted
            lives += 1
            print(f"\nThere is no '{input_char}' in the chosen word. You have {6 - lives} live(s) left")
            
        else: # user have inputted the correct character
            for position in range(len(word_chosen)):
                if word_chosen[position] in user:
                    output[position] = word_chosen[position]

            if '_' in output:
                print("NICE - Keep it rolling!!!")

    if lives < 6:
        print(f"\nYou have guessed the correct word: {word_chosen}")
        print("\nCongratulation!!! You have WON <3")
    else:
        print(HANGMANPICS[lives])
        print(f"You have LOST - the solution is: {word_chosen} !")
        print("\nBetter luck next time =))")

    again = input("\nWould you like to play another game? Y for YES | ANYTHING else for NO: ").lower()
