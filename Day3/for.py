real_user = 'harris'
real_pass = '1234'

tries = int(input("Berapa Kali Coba: "))

for tries in range(tries,0,-1):
    print (f"Anda memiliki {tries} coba")
    guess_user = input('Masukkan username: ')
    guess_pass = input('Masukkan password: ')

    if guess_user == real_user and guess_pass == real_pass:
        print("==Login Berhasil==")
        break
    else:
        print("==Login Invalid==")

print ("==Exiting Loop==")