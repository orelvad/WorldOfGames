from random import randint
import tkinter as tk


def generate_sequence(difficulty):
    rand=int(randint(1,101))
    randlist = rand
    for i in range(difficulty-1):
        rand=int(randint(1,101))
        if 9 < rand < 101:
            randlist=randlist * 10 ** 2 + rand
        elif 1 < rand < 10:
            randlist = randlist * 10 ** 1 + rand
        elif rand > 99:
            randlist = randlist * 10 ** 3 + rand
    return randlist


def show_numbers(randlist):
    root = tk.Tk()
    display = tk.Message(root, text="Memory Game")
    display_numbers = tk.Label(root, text=randlist, font=("MonoSpace",30))
    display_numbers.pack()
    display_numbers.after(700, root.destroy)
    root.mainloop()

def get_list_from_user(difficulty):
    list_from_user=int(input(f"please enter {difficulty} numbers\n"))
    return list_from_user


def is_list_equal(gen_list,usr_list):
    print(gen_list,usr_list)
    if gen_list == usr_list:
        return True
    else:
        return False


def play(difficulty):
    gen_list = generate_sequence(difficulty)
    show_numbers(gen_list)
    list_from_user = get_list_from_user(difficulty)
    is_equal = is_list_equal(gen_list, list_from_user)
    return is_equal

