real_pass = "1234"
real_user = "harris"
granted = False

print (real_user)
print (real_pass)

while granted != True:
    guess_user = input("Masukkan Username: ")
    guess_pass = input("Masukkan Password: ")

    if guess_pass == real_pass and guess_user == real_user:
        granted = True
        print ("==Access Granted==")

    else:
        print ("==Access Denied==")    