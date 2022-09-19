import GuessGame
import MemoryGame
import CurrencyRouletteGame
from utils import screen_cleaner
from Score import add_score
from time import sleep
import os


def welcome(name):
    screen_cleaner()
    return "Hello "+name+" and welcome to the World of Games (WoG).\nHere you can find cool games to play."


def load_game():
    req=False
    games_list=[MemoryGame, GuessGame, CurrencyRouletteGame]
    while not req:
        print("Please choose a game to play:")
        print("\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        print("\t2. Guess Game - guess a number and see if you chose like the computer")
        print("\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
        try:
            game = int(input())
            difficulty = int(input("Please choose game difficulty from 1 to 5:\n"))
        except KeyboardInterrupt:
            import MainScores

        if 0 < game < 4 :
            if 0 < difficulty < 6 :
                req=True
                if games_list[game-1].play(difficulty):
                    print("won")
                    add_score(difficulty)
                    sleep (3)
                    screen_cleaner()
                    load_game()
                else:
                    print ("Lost!")
                    sleep(3)
                    screen_cleaner()
                    load_game()

        if not req:
            print ("\nPlease notice your input is correct \n")
