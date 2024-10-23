#!/usr/bin/env python3


import prompt
import randome


def welcome_user():
        name = prompt.string('May I have you name?  ')
        print('Hello, ' + name + '!')


def main():
        print("Welcome to the Brain Games!")


if __name__ == '__main__':
     main()

welcome_user()

print('Answer "yes" if number is even, otherwise answer "no".')
attempts = 3
for count in range(attempts):
    number = randome.randint(1, 1000)
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

if count == attempts:
    print('Congratulations, ' + name + '!')

