import prompt


def welcome_user():
    name = prompt.string('May I have you name?  ')
    print('Hello, ' + name + '!')


if __name__ == "__main__":
    print("Welcome to the Brain Games!")
    welcome_user()
