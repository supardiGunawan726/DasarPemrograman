kalimat = input("kalimat: ")
kalimat_baru = ""

for huruf in kalimat:
    if huruf == "a" or huruf == "A":
        kalimat_baru += "4"
    elif huruf == "e" or huruf == "E":
        kalimat_baru += "3"
    elif huruf == "L":
        kalimat_baru += "7"
    elif huruf == "S":
        kalimat_baru += "5"
    else:
        kalimat_baru += huruf

print(f"\nkalimat lama: {kalimat}")
print(f"kalimat baru: {kalimat_baru}\n")