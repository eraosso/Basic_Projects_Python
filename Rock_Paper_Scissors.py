# Python implementatior for Rock-Paper-Scissors:

from random import randint

opcoes = ['Rock', 'Paper', 'Scissors']

number_of_player_wins = 0
number_of_computer_wins = 0
games = 0

def player():
    while True:
        try:
            jogador = int(input("Please enter your choice: \n[0]-Rock\n[1]-Paper\n[2]-Scissors\n"))
            if 0 <= jogador <= 2:
                return jogador
            else:
                print("Choice must be an integer between 0 and 2!")
                continue
        except ValueError:
            print("Choice must be an integer between 0 and 2!")

def computer():
    return randint(0, 2)


def player_wins():
    print("Player wins!")
    global games, number_of_player_wins
    games += 1
    number_of_player_wins += 1

def computer_wins():
    print("Computer wins!")
    global games, number_of_computer_wins
    games += 1
    number_of_computer_wins += 1

def decide(jogador, computador):
    if jogador < computador:
        player_wins()
    else:
        computer_wins()

def analisa(jogador, computador):
    global games
    if jogador == computador:
        print("It's a tie! Try again!")
        games += 1
    elif jogador == computador - 2:
        player_wins()
    elif computador == jogador -2:
        computer_wins()
    else:
        decide(jogador, computador)

print("Welcome to the game!")
continuar = "Y"
while continuar.lower() == "y":
    jogador = player()
    computador = computer()
    analisa(jogador, computador)
    continuar = input("Do you want to play more? ('Y/N')")

print("Total # of games: {}".format(games))
print("Player wins: {} - {:.2%}".format(number_of_player_wins, number_of_player_wins / games))
print("Computer wins: {} - {:.2%}".format(number_of_computer_wins, number_of_computer_wins / games))
print("Total number of ties: {}".format(games - number_of_computer_wins - number_of_player_wins))



