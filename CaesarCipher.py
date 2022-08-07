import string

decryptedMessage = str(input("Enter the message to be encrypted: "))
inputShift = int(input("Enter the number of character shifts:"))

alphabet = string.printable
tempShift = alphabet[inputShift:] + alphabet[:inputShift]
table = str.maketrans(alphabet, tempShift)
encryptedMessage = decryptedMessage.translate(table)

print("Original message: %s" % (decryptedMessage))
print("Encrypted message: %s" % (encryptedMessage))

a = input("Press close to exit the program")
