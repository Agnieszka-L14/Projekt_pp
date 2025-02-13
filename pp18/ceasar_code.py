#VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ

delta =3

def decode_letter(letter, delta):
    if letter <'A' or letter> 'Z':
        return letter
    n = ord(letter) -detla
    if n< ord('A'):
        n +=ord('Z') - ord('A') + 1
    return chr(n)

def decode(string, delta):
    decoded = ""
    for letter in string :
        decoded += decode_letter(letter, delta)
    return decoded

print(decode( 'VWXGLD ', delta))

