def isEmailValid(email):
    # Memisahkan isi email = local_part@domain
    # menjadi [local_part, domain]
    content = email.split("@")

    #cek email tidak boleh mengandung spasi
    haveNoSpace = email.find(" ") == -1

    #cek content harus berisi 2 item yaitu local_part dan domain
    isContent = len(content) == 2

    #cek local_part, hanya boleh huruf, angka, dan underscore
    isIdentifier = content[0].isidentifier()

    #cek domain harus ada pada list content
    #cek domain harus ada titik . tapi hanya boleh ditengah, . tidak boleh diakhir atau awal domain
    isDomain = len(content) == 2 and content[1].find(".") != -1 and (not content[1].startswith(".")) and (not content[1].endswith("."))
    
    # print(haveNoSpace, isContent, isIdentifier, isDomain)
    return haveNoSpace and isContent and isIdentifier and isDomain


emails = ["alunsujjada@gmailcom", "alunsujjada@gmail.com", "alun.sujjada@gmail.com", "alunsujjada.gmail.com", "alun.sujjada@gmailcom"]

for email in emails:
    isValid = isEmailValid(email)
    print(f"{email} => {isValid}")