from simplecrypt import encrypt, decrypt, DecryptionException


with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    with open("passwords.txt", 'r') as passwords:
        for password in passwords:
            password = str(password).strip()
            try:
                msg = decrypt(password, encrypted)
                print(password, ' is correct')
                print('message is: ', msg.decode('utf-8'))
                break
            except DecryptionException:
                print(password, ' is wrong')
                continue
