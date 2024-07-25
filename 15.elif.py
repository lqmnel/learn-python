# Belajar Elif => Else if

menu_pilihan = input("Silahkan Pilih Menu [1-3] :")

if menu_pilihan == "1":
    print("Anda Memilih Menu 1")
elif menu_pilihan == "2":
    print("Anda Memilih Menu 2")
elif menu_pilihan == "3":
    print("Anda Memilih Menu 3")
else:
    print("Menu Tidak Tersedia")

if menu_pilihan == "x":
    print("Program Keluar")