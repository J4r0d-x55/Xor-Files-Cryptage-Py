from hashlib import sha256

entree = input("Entrez le nom du fichier à chiffrer: ")
sortie = input("Entrez le nom du fichier final: ")
key = input(("Entrez la clé: "))
keys = sha256(key.encode('utf-8')).digest()

with open(entree, 'rb') as f_entree:
    with open(sortie, 'wb') as f_sortie:
        i = 0
        while f_entree.peek():
            c = ord(f_entree.read(1))
            j = i % len(keys)
            b = bytes([c ^ keys[j]])
            f_sortie.write(b)
            i = i + 1