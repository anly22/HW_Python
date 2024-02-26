def encrypt(text, n):
    res = ""
    marks = "'',.:;-!?)"
    for i in range(len(text)):
        ch = text[i]
        if ch == " ":
            res += " "
        elif ch in marks:
            res += ch
        elif (ch.isupper()):
            res += chr((ord(ch) + n-65) % 26 + 65)
        else:
            res += chr((ord(ch) + n-97) % 26 + 97)
        
    return res

text = input("Plain text is: ")
n = int(input("Shift is: "))
#The quick brown fox jumps over the lazy dog.
#n = 1

print("Plain text is: " + text)
print("Shift is: " + str(n))
print("Cipher text is: " + encrypt(text,n))