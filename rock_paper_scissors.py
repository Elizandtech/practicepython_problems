## Make a two-player Rock-Paper_Scissors game. ##
# /// Ask for plays, compare, print message to the winner /// #
# ///////// Ask players if they want to start a new game ///////////#

while True:
    try:
        game = input("Start game? Hit Enter or type 'no': ")
        if game == 'no':
            break
        if game != 'no' and game != '':
            raise Exception

        while True:
            try:
                player_1 = input("Player One: enter rock, paper or scissors: ")
                if player_1 !='rock' and player_1 !='scissors' and player_1 !='paper':
                    raise Exception

                player_2 = input("Player Two: enter rock, paper or scissors: ")
                if player_2 !='rock' and player_2 !='scissors' and player_2 !='paper':
                    raise Exception
                break
            except:
                print('Invalid entry')
                continue

    except:
        print("Incorrect input")
        continue

    Two = ('Player 2 Wins!! '+ player_2 + ' beats '+ player_1)
    One = ('Player 1 Wins!! '+ player_1 + ' beats '+ player_2)

    if (player_1 == 'rock' and player_2 == 'scissors') or (player_1 == 'scissors' and player_2 == 'paper') or (player_1 == 'paper' and player_2 == 'rock'):
        print(One)

    elif (player_1 == 'scissors' and player_2 == 'rock') or (player_1 == 'paper' and player_2 == 'scissors') or (player_1 == 'rock' and player_2 == 'paper'):
        print(Two)

    else:
        print("It's tied!")

print("See you later! ")
