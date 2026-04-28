# doing something to do

import time
import random

questions=[("What is the capital of India","Delhi"),
           ("What is 5+5 ", "10"),
           ("Which Language is used to write Python Program ", "Python"),
           ("What colour is sky ", "Blue"),
           ("What is 10/2 ", "5")]

def play_quiz():
    score = 0
    time_limit = 10
    random.shuffle(questions)
    print("\nQuiz started you have -_- ", time_limit, "Second for each questions.\n")

    for q , ans in questions:
        print("Q -_- ", q)

        start = time.time()
        user_ans = input("Ans -_- ").lower()
        end = time.time()

        time_taken = end-start

        if time_taken>time_limit:
            print("Times Up...")

        elif user_ans == ans.lower():
            print("Right Answer")
            score +=1
        else:
            print("Wrong Answer")

        print("-"*30)
    print("\n Quiz Finished")
    print("Your score -_- ", score)
