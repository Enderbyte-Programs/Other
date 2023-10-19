import random
import enchant
import multiprocessing
d = enchant.Dict("en_US")

### CONFIG START
WORDLIM = 0
### CONFIG END

def is_word(word:str):
    return d.check(word)
validx = list("abcdefghijklmnopqrstuvwxyz ")

def run():
    global WORDLIM
    if WORDLIM == 0:
        WORDLIM = int(input("Minimum word length? "))
    while True:
        word = ""
        while True:
            selw = random.choice(validx)
            if selw == " ":
                break
            else:
                word += selw
        #print(word)
        if len(word) >= WORDLIM:
            if is_word(word):
                print(word.strip(),end=" ",flush=True)
if __name__ == "__main__":
    run()