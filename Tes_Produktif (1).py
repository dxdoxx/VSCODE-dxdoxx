
# a = variabel
# enkos = enkripsi kosong / penyimpanan kosong dan sebaliknya (deckos)
# p_enc = panjang encription
# print(" ====== Reverse Texts ======")

# enc = input(' Encryption       : ')
# dec = input(' Decryption       : ')

# enckos = ''
# deckos = ''

# p_enc = len(enc) - 1    # len (enc) = dengan panjang a dari belakang dikurangi 1
#                         # maka seperti contoh aku denhgan jumlah 0 1 2 3 dan - 1 maka dihitung 
#                         # dari belakang
# p_dec = len(dec) - 1

# while p_enc >= 0: # ketika b >= 0 maka :
#     enckos = enckos + enc[p_enc] # enkos + enc dengan [] artinya mengacu pada variable p_enc
#     p_enc = p_enc - 1 # dengan p_enc = penc - 1 dan diulangi sampai selesai

# # Sama saja cuman text nya yang beda
# while p_dec >= 0:
#     deckos = deckos + dec[p_dec]
#     p_dec = p_dec - 1

# print("\n ========== Hasil ==========")
# print(" Hasil Encryption : ", enckos)
# print(" Hasil Decription : ", deckos)

# def encrypt(text,s):
#     result = ''

#     for i in range(len(text)): # i termasuk variable
#         char = text[i] # text yang mengacu didalamnya i (tuple kalau gak list)
        
#         # Filter
#         if (char.isupper()): # isupper (filter huruf besar)
#             result += chr((ord(char) + s - 65) % 26 + 65)
#             # ord(char) adalah letak nomer berapa text tersebut dalam ASCII
#             # (letak ASCII + s(pergeseran nya) - 65) kemudian modulus 26 + 65

#         elif (char.isnumeric()): # isnumeric (filter nomer)
#             result += chr((ord(char) + s - 48) % 10 + 48)
        
#         elif (ord(char) >= 33 and ord(char) <= 47): # letak nomer text ASCII dengan range antara 13 sampai 47
#             result += chr((ord(char) + s - 33) % 14 + 33)
            
#         # Encrypt lowercase characters in plain text
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
#     return result

# print("\n ======= Cyper Texts =======")
# print(" ========= Encript =========")
# text = input(" Text Encryption Chyper : ")
# s = int(input(" Pergeseran             : "))

# print("\n ========== Hasil ==========")
# print (" Plain Text    : " + text)
# print (" Shift pattern : " + str(s))
# print (" Cipher        : " + encrypt(text,s))

# Decription
# def decript(text,s):
#     result = ''
# # transverse the plain text
#     for i in range(len(text)):
#         char = text[i]

# # Encrypt uppercase characters in plain text
#         if (char.isupper()):
#             result += chr((ord(char) - s - 65) % 26 + 65)
        
#         elif (char.isnumeric()):
#             result += chr((ord(char) - s - 48) % 10 + 48)
        
#         elif (ord(char) >= 33 and ord(char) <= 47):
#             result += chr((ord(char) - s - 33) % 14 + 33)
        
#         elif (ord(char) >= 58 and ord(char) <= 64):
#             result += chr((ord(char) - s - 58) % 6 + 58)
# # Encrypt lowercase characters in plain text
#         else:
#             result += chr((ord(char) - s - 97) % 26 + 97)
#     return result

# print("\n ========= Decript =========")
# text = input(" Text Encryption Chyper : ")
# s = int(input(" Pergeseran             : "))

# print("\n ========== Hasil ==========")
# print (" Plain Text    : " + text)
# print (" Shift pattern : " + str(s))
# print (" Cipher        : " + decript(text,s))

# Root 13
# rot13trans = ''.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -',
# 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm- ') # Jumlah harus sama

# # Function to translate plain text

# def rot13(text1):
#     return text1.translate(rot13trans)

# def main():
#     print(" ========= ROOT 13 =========")
#     print(" ========= Encript =========")
#     txt1 = input(" ROT13 Encript : ")
#     print(" Hasil Encript :", rot13(txt1))

# if __name__ == "__main__" :
#     main()

# def rot13(text2):
#     return text2.translate(rot13trans)

# def main():
#     print("\n ========= Decript =========")
#     txt2 = input(" ROT13 Decript : ")
#     print(" Hasil Decript :", rot13(txt2))

# if __name__ == "__main__":
#     main()

rot18trans = ''.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 -',
'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234- ') # Jumlah harus sama

# Sebuah fungsi bisa menerima parameter, bisa mengembalikan suatu nilai, dan bisa dipanggil berkali-kali secara independen
def rot18(text1):
    return text1.translate(rot18trans)

def main():
    print("\n ========= ROOT 18 =========")
    print(" ========= Encript =========")
    txt1 = input(" ROT18 Encript : ")
    print(" Hasil Encript :", rot18(txt1))

if __name__ == "__main__":
    main()

def rot18(text2):
    return text2.translate(rot18trans)

def main():
    print("\n ========= Decript =========")
    txt2 = input(" ROT18 Decript : ")
    print(" Hasil Decript :", rot18(txt2))

if __name__ == "__main__":
    main()




# MIX ENCRYPT
# print(" ===== MIX Encryptions =====")
# mix_all = input(" Encryption       : ")
# s = int(input(" Shift pattern    : "))
# enckos = ''

# p_enc = len(mix_all) - 1    

# while p_enc >= 0: 
#     enckos = enckos + mix_all[p_enc] 
#     p_enc = p_enc - 1 

# def encrypt(mix_all,s):
#     result = ''

#     for i in range(len(mix_all)): 
#         char = mix_all[i]
        
#         # Filter
#         if (char.isupper()): 
#             result += chr((ord(char) + s - 65) % 26 + 65)

#         elif (char.isnumeric()): 
#             result += chr((ord(char) + s - 48) % 10 + 48)
        
#         elif (ord(char) >= 33 and ord(char) <= 47): 
#             result += chr((ord(char) + s - 33) % 14 + 33)

#         elif (char.isspace()):
#             result += chr((ord(char) + s - 32) % 1 + 32)

#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
#     return result

# rot13trans = ''.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -',
# 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm- ') # Jumlah harus sama

# # Function to translate plain text

# def rot13(mix_all):
#     return mix_all.translate(rot13trans)

# rot18trans = ''.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 -',
# 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234- ') # Jumlah harus sama

# # Sebuah fungsi bisa menerima parameter, bisa mengembalikan suatu nilai, dan bisa dipanggil berkali-kali secara independen
# def rot18(mix_all):
#     return mix_all.translate(rot18trans)

# print("\n ========== Hasil ==========")
# print(" Hasil Reverse :", enckos)
# print (" Caesar Cipher : " + encrypt(mix_all,s))

# def main():
#     print(" Hasil ROOT 13 :", rot13(mix_all))

# if __name__ == "__main__" :
#     main()

# def main():
#     print(" Hasil ROOT 18 :", rot18(mix_all))
    
# if __name__ == "__main__" :
#     main()