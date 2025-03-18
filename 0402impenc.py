import _0401encapsulation as enc

#siapkan lagu dan playlist
lagu1 = enc.Lagu("Laskar Pelangi", "Nidji")
lagu2 = enc.Lagu("Mimpi", "Anggun")
lagu3 = enc.Lagu("Matahari", "Agnes Monica")
lagu4 = enc.Lagu("Karena Cinta", "Joy Tobing")
lagu5 = enc.Lagu("Bintang di Surga", "Peterpan")
lagu6 = enc.Lagu("Ku Tak Bisa", "Slank")
lagu7 = enc.Lagu("Ku Tak Akan", "Hyper Act")
lagu8 = enc.Lagu("Ku Tak Bisa", "Afgan")
lagu9 = enc.Lagu("Ku Tak Akan", "Hyper Act")
lagu10 = enc.Lagu("Ku Tak Bisa", "Afgan")
pl = enc.PlayList([lagu1, lagu2, lagu3, lagu4, lagu5, lagu6, lagu7, lagu8, lagu9, lagu10])

stop = False
while not stop:
    print("1. Putar lagu pertama")
    print("2. Putar lagu terakhir")
    print("3. Putar lagu saat ini")
    print("4. Putar lagu berikutnya")
    print("5. Putar lagu sebelumnya")
    print("6. Keluar")
    pilihan = input("Pilihan: ")
    if pilihan == "1":
        pl.play_first_song()
    elif pilihan == "2":
        pl.play_last_song()
    elif pilihan == "3":
        pl.play()
    elif pilihan == "4":
        pl.play_next_song()
    elif pilihan == "5":
        pl.play_prev_song()
    elif pilihan == "6":
        stop = True
        print("Pemutar dihentikan, Terima kasih")
    else:
        print("Pilihan tidak valid")
