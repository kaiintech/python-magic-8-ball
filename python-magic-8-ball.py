import random

def main():
    """
    A simple Magic 8-Ball game that answers user questions at random from a list.
    Type 'exit' to leave the game.
    """

    responses = [
        "It's definitely possible",
        "It seems unlikely",
        "Yes",
        "No",
        "Maybe",
        "Not really",
        "I would think so",
        "Hell no",
        "Definitely not",
        "Ask again later",
        "I don't have a clue",
        "Absolutely! Go for it",
        "Don't count on it",
        "Signs point to yes",
        "Better not tell you now",
        "Concentrate and ask again",
        "Without a doubt",
        "My sources say no",
        "You can rely on it",
        "Very doubtful",
        "Chances look good",
        "Unlikely, sorry",
        "Yes, in due time",
        "No, try something else"
    ]

    print('\nWelcome to the Magic 8-Ball Game')
    print("I have the answers to all your questions.")
    print("Type 'exit' to leave the session.\n")

    while True:
        user_input = input('Ask your question \n>> ').strip()
        
        if user_input.lower() == 'exit':
            print('See you next time!')
            break
        
        answer = random.choice(responses)
        print(f'{answer}\n')

main()
