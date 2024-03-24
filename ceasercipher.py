#A python program to illustrate Caesar Cipher Technique
"""
    The Python program demonstrates the Caesar Cipher technique for encrypting text by shifting
    characters by a specified amount.
    
    :param text: "ATTACKATONCE"
    :param s: The variable `s` in the Caesar Cipher program represents the shift value. It determines
    how many positions each letter in the text should be shifted to encrypt the message. In the example
    provided, `s = 4`, which means each letter in the text is shifted by 4 positions to create the
    :return: The program returns the encrypted text using the Caesar Cipher technique with the given
    shift value.
"""
def encrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result

#check the above function
text = "ATTACKATONCE"
s = 4
print ("Text : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))
  