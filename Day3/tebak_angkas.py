import random

real_ans = random.randint(1,10)
print ("Tebak Angkanya Antara 1 Sampai 10")
guess = ""

while guess != real_ans:
    guess = int(input("Berapa Tebakan Loe? "))
    if guess < real_ans:
        print ("Kekecilan cuy")
    elif guess > real_ans:
        print ("Kebesaran cuy")
    else:
        print ("Anjas Hoki Juga Loe")