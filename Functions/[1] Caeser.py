# Simple Caesar encrypting algorithm

def encrypt_caesar(msg, shift=3):
    ans = ''
    for i in msg:
        
        if i.isalpha():
            if i.islower():
                ans = ans + chr(ord('а')+(ord(i) - ord('а') + shift) % 32)
            if i.isupper():
                ans = ans + chr(ord('А')+(ord(i) - ord('А') + shift) % 32)
        else:
            ans = ans + i
    return ans

def decrypt_caesar(msg, shift=3):
    ans = ''
    for i in msg:
        if i.isalpha():
            if i.islower():
                ans = ans + chr(ord('а')+(ord(i) - ord('а') - shift) % 32)
            if i.isupper():
                ans = ans + chr(ord('А')+(ord(i) - ord('А') - shift) % 32)
        else:
            ans = ans + i
    return ans


msg = "Да здравствует салат Цезарь!"

shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
