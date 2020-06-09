print('Pesan apa aja mbak?')

pesanan = ['es teh manis', 'nasi pecel', 'sambal bawang']
print('Mbak sudah pesan')
for n in range(len(pesanan)):
    print(n+1, pesanan[n])

while True:
    lanjut = input('Ada tambahan mbak? (y/n) ')
    if lanjut == 'n':
        break
    elif lanjut == 'y':
        tambah = input('Tambah apa mbak? ')
        pesanan.append(tambah)
    else:
        continue

print('Saya ulang pesanannya ya mbak')

for n in range(len(pesanan)):
    print(n+1, pesanan[n])

print('Terima kasih')