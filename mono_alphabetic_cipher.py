'''
# In this cipher, the letters of the alphabet are shifted by a specified number of positions to create a new
# mapping for encryption and decryption. This shifting of letters is essential for encoding and
# decoding messages using the cipher. The `generate_cipher_key` function in your code implements this
# shifting process by creating a mapping between the original alphabet and the shifted alphabet based
# on the given shift value. This mapping is then used in the `encrypt` and `decrypt` functions to
# process the input message accordingly.
'''
def generate_cipher_key(shift) -> dict:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    '''
    # The comment `in the above line the letters are shifted back in the string and the no. of letters
    # shifted back = shift value` is explaining the process happening in the line of code where the
    # `shifted_alphabet` is generated.
    '''
    key = dict(zip(alphabet, shifted_alphabet))
    return key

def encrypt(message,key) -> str:
    """
    The `encrypt` function takes a message and a key, then encrypts the message using the key by
    replacing each alphabetic character with its corresponding value in the key while maintaining the
    case of the characters.
    
    :param message: The `message` parameter in the `encrypt` function is the text that you want to
    encrypt using a given `key`. The function will iterate over each character in the message and
    encrypt it based on the key provided. If the character is a letter, it will be replaced with the
    corresponding value from
    :param key: The `key` parameter in the `encrypt` function is a dictionary that maps characters to
    their encrypted counterparts. Each character in the message will be replaced with its corresponding
    value from the `key` dictionary during encryption
    :return: The function `encrypt` returns the encrypted message after applying the encryption key to
    each character in the input message.
    """
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message += key[char]
            else:
                encrypted_message += key[char.lower()].upper()
        else:
            encrypted_message += char

    return encrypted_message 
 
def decrypt(cipher_text,key) -> str:
    """
    The function decrypts a given cipher text using a provided key mapping.
    
    :param cipher_text: The `cipher_text` parameter is the encrypted message that you want to decrypt
    using the provided `key`. The `decrypt` function will use the `key` to reverse the encryption
    process and return the decrypted message
    :param key: The `key` parameter is a dictionary that maps characters to their corresponding
    encrypted characters. It is used to decrypt a given cipher text by replacing each encrypted
    character with its original character based on the mapping provided in the `key` dictionary
    :return: The function `decrypt` returns the decrypted message after applying the reverse key to the
    given cipher text.
    """
    reverse_key  = {v:k for k, v in key.items()}
    decrypted_message = ''
    for char in cipher_text:
        if char.isalpha():
            if char.islower():
                decrypted_message += reverse_key[char]
            else:
                decrypted_message += reverse_key[char.lower()].upper()
        else:
            decrypted_message += char

    return decrypted_message

def main():
    shift = int(input('enter shift value for cipher'))
    key = generate_cipher_key(3) 
    
    choice = input("Encrypt or decrypt? (e/d): ").lower()
    if choice == 'e':
        plain_text = input("Enter the message to encrypt: ")
        encrypted = encrypt(plain_text, key)
        print("Encrypted message:", encrypted)
    elif choice == 'd':
       cipher_text = input("Enter the message to decrypt: ")
       decrypted = decrypt(cipher_text, key)
       print("Decrypted message:", decrypted)
    else:
      print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
      
if __name__ == "__main__":
   main()


