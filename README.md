# PRODIGY_CS_01
Prodigy infotech Cyber security Task-01

# PRODIGY_CS_01
Prodigy infotech Cyber security Task-01

Task1: "Caesar Cipher Implementation"

This Python code implements the Caesar Cipher, a simple substitution cipher where each letter in the plaintext is shifted a certain number of positions down the alphabet
Key Features:

Encryption: Shifts each letter in the plaintext by the specified shift value.
Decryption: Shifts each letter in the ciphertext back by the same shift value to recover the plaintext.
Case-Insensitive: Handles both uppercase and lowercase letters seamlessly by converting the input message to uppercase.
User-Friendly:
Prompts the user for input: message, shift value, and encryption/decryption mode.
Provides clear output for the encrypted or decrypted message.
Includes basic input validation for the mode.

How it Works:

caesar_cipher(text, shift, mode) function:

Takes the text, shift value, and mode as input.
Iterates through each character in the text.
If the character is an alphabet:
Determines the starting alphabet (A for uppercase, a for lowercase).
Calculates the shifted position by adding the shift value and taking the modulo 26 to handle wrapping around the alphabet.
Converts the shifted position back to a character.
If the character is not an alphabet (e.g., spaces, punctuation), it remains unchanged.
Returns the resulting encrypted or decrypted message.
if __name__ == "__main__": block:

Prompts the user for input:
message: The text to be encrypted or decrypted.
shift: The number of positions to shift the letters.
mode: 'encryption' or 'decryption'.
Converts the input message to uppercase for case-insensitive handling.
Calls the caesar_cipher function with the appropriate arguments:
For encryption, shift is used directly.
For decryption, -shift is used to reverse the encryption.
Prints the encrypted or decrypted message.
Usage:

Save the code as a Python file (e.g., caesar_cipher.py).
Run the script from your terminal: python caesar_cipher.py
Enter the message, shift value, and mode when prompted.
