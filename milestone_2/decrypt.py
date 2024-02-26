def decrypt(cipher_text, n):
    res = ""
    marks = "'',.:;-!?"
    for i in range(len(cipher_text)):
        ch = cipher_text[i]
        if ch == " ":
            res += " "
        elif ch in marks:
            res += ch
        elif (ch.isupper()):
            res += chr((ord(ch) - n-65) % 26 + 65)
        else:
            res += chr((ord(ch) - n-97) % 26 + 97)
    
    return res

cipher_text = input("Plain text is: ")
n = int(input("Shift is: "))
#Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.
#n = 1

print("Cipher text is: " + cipher_text)
print("Shift is: " + str(n))
print("Plain text is: " + decrypt(cipher_text,n))