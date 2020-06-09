import time

for loop in range(3):
    for dots in range(3):
        time.sleep(0.5)
        print ("loading" + "."*( dots + 1))