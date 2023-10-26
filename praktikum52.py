total_harga = 0.0

while True:
    umur_input = input("Masukkan umur: ")
    
    if umur_input.isdigit():
        umur = int(umur_input)
        
        if umur <= 2:
            harga = 0
        elif 3 <= umur <= 12:
            harga = 14
        elif umur >= 65:
            harga = 18
        else:
            harga = 23

        total_harga += harga
        print(f"{'Gratis' if harga == 0 else f'Harga ${harga:.2f}'}")
        print(f"Running total: ${total_harga:.2f}")
    else:
        print("Masukkan umur yang valid!")

    lanjutkan = input("Lanjutkan? (ya/tidak): ")
    if lanjutkan.lower() != "ya":
        break

uang_diberikan = float(input("Masukkan jumlah uang: "))
kembalian = uang_diberikan - total_harga

if kembalian >= 0:
    print(f"Kembalian: ${kembalian:.2f}")
else:
    print("Uang yang dimasukkan kurang!")
