#!/usr/bin/env python3


import prompt
import random


print("Welcome to the Brain Games!")
name = prompt.string('May I have you name?  ')
print('Hello, ' + name + '!')
print('Answer "yes" if number is even, otherwise answer "no".')

attempts = 3
count = 0

while count < attempts:
    number = random.randint(1, 1000)
    print('Question: ' + str(number))
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    user_answer = prompt.string('Your answer: ')
    if user_answer == answer:
        print('Correct!')
    else:
        print("'" + user_answer + "' is wrong answer ;(. Correct answer was '" + answer + "'.")
        print("Let's try again, " + name + "!")
        break
    count += 1

if count == attempts:
    print('Congratulations, ' + name + '!')

