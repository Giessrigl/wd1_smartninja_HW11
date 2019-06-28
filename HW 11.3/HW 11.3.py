import random
import json
import datetime

name = str(input("What's your name? \n"))

current_time = datetime.datetime.now()

print(current_time)

secret = random.randint(1, 10)

attempts = 0
wrong_guesses = []

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

score_list_sorted = sorted(score_list, key=lambda k: k["attempts"])[:3]

for score_dict in score_list_sorted:
    print("Top scores: " + (str(score_dict.get("attempts")) + " attempts, date: " + str(score_dict.get("date"))
          + ", name: " + str(score_dict.get("name")) + ", number was: " + str(score_dict.get("secret"))))

while True:
    guess = int(input("guess the secret number (1-10): "))

    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": str(name), "secret": str(secret), "wrong_guesses": wrong_guesses})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("Congratulation! You win!")
        print("Attempts needed: " + str(attempts))
        break

    elif guess < secret:
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("Wrong number! You need to go up!")
    else:
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("Wrong number! You need to go down!")

    wrong_guesses.append(guess)

