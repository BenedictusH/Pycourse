print('Daftar Pelanggaran Murid')

murids = ['Ian', 'Kresna', 'Enryl', 'Harris', 'Edu']

for murid in murids:
    if murid == 'Enryl':
        print(murid, '- Pelanggaran 2 atau lebih')
    elif murid == 'Harris' or murid == 'Edu':
        print(murid, '- Pelanggaran 1')
    else:
        print(murid)