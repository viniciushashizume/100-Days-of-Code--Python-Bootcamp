def encrypt(msg, shift):
    newMsg = ''
    for i in range(len(msg)):
        letter = msg[i]
        indexLetter = alphabet.index(letter)
        shiftedIndex = (indexLetter + shift) % 26
        newMsg += alphabet[shiftedIndex]
    print(f'Mensagem encriptada: {newMsg}')
    return newMsg

def decrypt(encryptedMsg, shift):
    newMsg = ''
    for i in range(len(encryptedMsg)):
        letter = encryptedMsg[i]
        indexLetter = alphabet.index(letter)
        shiftedIndex = (indexLetter - shift) % 26
        newMsg += alphabet[shiftedIndex]
    print(f'Mensagem descriptografada: {newMsg}')
    return newMsg

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y','z']
#shift = int(input('Shift number: '))
#msg = str(input('Message to encrypt: '))

#encrypt(msg, shift)
#encryptedMsg = encrypt(msg, shift)
decrypt('lix', 23)

