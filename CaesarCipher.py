import string

def encrypt_message(message, shift):
    alphabet = string.printable
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(table)

if __name__ == "__main__":
    decrypted_message = input("Enter the message to be encrypted: ")
    shift = int(input("Enter the number of character shifts: "))
    encrypted_message = encrypt_message(decrypted_message, shift)
    print("Original message:", decrypted_message)
    print("Encrypted message:", encrypted_message)
    input("Press enter to exit the program.")
