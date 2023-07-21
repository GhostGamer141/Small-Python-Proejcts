import random
import time
import threading


class timer:
      
    def __init__(self):
        self._running = True
      
    def terminate(self):
        self._running = False
      
    def run(self):
        global n
        n = 15
        while self._running and n > 0:
            n -= 1
            time.sleep(1)


def scramble_word(word):
    return ''.join(random.sample(word[0], len(word[0])))

def word_selector(l):
    word = random.choice(list(l.items()))
    answer = word[0]
    hint = word[1]
    question = scramble_word(word)
    return question,answer,hint 


def time_mode():
    print("You have Chosen the timed mode which means you will have only 15 seconds to guess the word, if you fail to do so you will lose the gmae")
    while True:
        status = input("Your timer will start after the word is revealed. Are you ready?[Y/N]:").upper()
        if status in ['YES','Y']:
            for i in range(3,0,-1):
                print(i)
                time.sleep(1)
            print('Your time starts now!')
            question,answer,hint = word_selector(words)
            print(f"Your word is: {question}: ")
            c = timer()
            timer_thread = threading.Thread(target=c.run)
            timer_thread.start()
            while n>0 :
                ans = input(f"Unscramble: {question} -> ")
                if ans == answer:
                    print("You got the right answer!")
                    c.terminate()
                    break
                elif ans == 'h':
                    print(f"hint -> {hint}\n")
                else:
                    print("Incorrect try again!\n")
            else:
                c.terminate()
                print("Times up :(")
                break
                
            break
                    
            
        else:
            break
            
            

def normal_mode():
    print("You have chosen the Un-Timed mode, you will be free to guess the answer without any pressure :D! No stress is always great isn't it?")
    inPlay = True
    while inPlay == True:
        status = input("READY? [Y/N]").upper()
        if status in ['YES','Y']:
            quesiton,answer,hint = word_selector(words)
            print(f"The scrambled word is: {quesiton}")
            while True:
                ans = ans = input("ans [for hint press 'h']: ").lower()
                if ans == 'h':
                    print(f"hint -> {hint}\n")
                    continue
                elif ans == answer:
                    print("YAY you got it!\n")
                    inPlay = False
                    break
                else:
                    print("Incorrect Try Again!\n")

        else:
            print("Hope to see you again!")
            break



#__main__

words = {'butterfly':'insect with wings', 'wonderful':'describing something nice'}

print("Welcome to word Decypher!!\nTry to Unscamble the words as quick as you can! You have both time modes and un timed modes!")


while True:
    while True:

        game_mode = input("Which game mode would you like to play? Timed[T] or Un-timedp[UT]  [T/UT]?: ").upper()
        if game_mode == 'T':
            time_mode()
            break
        elif game_mode == 'UT':
            normal_mode()
            break
        else:
            print("Please enter a valid option")

    if input("would you like to play again? [Y/N]?").upper() in ['YES','Y']:
        continue
    else:
        print("Thanks for playing!")
        break