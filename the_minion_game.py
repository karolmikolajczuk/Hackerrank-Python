vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def minion_game(string):
    #cononants
    stuart_points = 0
    #vowels
    kevin_points = 0

    #prepare
    string = string.lower()
    
    for index in range(len(string)):
        #vowel or consonant
        if string[index] in vowels:
            #count substring from that
            #increment player's point's
            kevin_points += len(string)-index
            #kevin_points += len(string[index:])
        
        else:        
            #count substring from that
            #increment player's point's
            stuart_points += len(string)-index
            #stuart_points += len(string[index:])

    # check who is the winner and print it
    if kevin_points > stuart_points:
        print('Kevin ' + str(kevin_points))
    elif kevin_points < stuart_points:
        print('Stuart ' + str(stuart_points))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

