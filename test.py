import random

facts = ["Saya suka membaca", "Saya pernah ke Singapur", "Saya tinggal di Bekasi", 'Saya punya korden Doraemon', 'Saya sekolah di SMPIT Gema Nurani']

while True:
    ask = input('Apakah kamu ingin fakta tentang Nashih? (y/n)')
    if ask == 'y':
        print(random.choice(facts))
    elif ask == 'n':
        print('Menghentikan Program...')
        break
    else:
        print('Maaf, Itu bukan perintah')
