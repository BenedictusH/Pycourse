print ("--Calculator--")

while True:
    inp1 = input("Masukkan angka pertama: ")
    inp2 = input("Masukkan angka kedua: ")
    print ( "1 Bagi \n" 
            "2 Kali \n" 
            "3 Jumlah \n"
            "4 Kurang\n"
            "5 Exit")
    op = input("Operator yang ingin digunakan? ")

    if op == "1":
        rslt = float(inp1) / float(inp2)
        print (rslt)

    elif op == "2":
        rslt = float(inp1) * float(inp2)
        print (rslt)

    elif op == "3":
        rslt = float(inp1) + float(inp2)
        print (rslt)

    elif op == "4":
        rslt = float(inp1) - float(inp2)
        print (rslt)

    elif op == "5":
        break

    else:
        print ("Invalid Input")

import random

real_ans = random.randint(1,10)