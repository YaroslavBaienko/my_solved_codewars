from random import choice


questions = ["Why you are so sad?", "Why i'd like to win everyone?", "Why is something?, Why is so high?"]

question = choice(questions)
answer = input(question + " ")

while answer != "just because":
    answer = input("why? ").strip().lower()

    if answer == "just because":
        question = choice(questions)
        answer = input(question + " ")


