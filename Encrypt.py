from hashlib import sha256

enter = input("Entrez le nom du fichier à chiffrer: ")
output = input("Entrez le nom du fichier final: ")
key = input(("Entrez la clé: "))
keys = sha256(key.encode('utf-8')).digest()

with open(enter, 'rb') as f_enter:
    with open(output, 'wb') as f_output:
        i = 0
        while f_enter.peek():
            c = ord(f_enter.read(1))
            j = i % len(keys)
            b = bytes([c ^ keys[j]])
            f_output.write(b)
            i = i + 1
