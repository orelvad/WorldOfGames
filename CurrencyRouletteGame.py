import requests
from random import randint
from flask import Flask


def get_money_imterval(d,randnum):
    url = 'https://v6.exchangerate-api.com/v6/1062f2f4baa84707dfb71304/latest/USD'
    response = requests.get(url)
    usd_to_ils=response.json()["conversion_rates"]["ILS"]
    t=usd_to_ils*randnum
    return (t-(5-d), t +(5-d))


def guess_from_user(randnum):
    return int(input(f"Guess value of {randnum}$ in ILS\n"))


def play(difficulty):
    randnum = randint(1, 100)
    money=get_money_imterval(difficulty, randnum)
    if money[0] < guess_from_user(randnum) < money[1]:

        return True
    else:
        return False
