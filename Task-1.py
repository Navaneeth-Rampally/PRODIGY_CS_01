# Implement Caesar Cipher
""" Task: Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption
""" 
def caesar_cipher(text, shift, mode):
  """
  Encrypts or decrypts a message using the Caesar Cipher.

  Args:
    text: The message to be encrypted or decrypted.
    shift: The number of positions to shift the letters.
    mode: 'encrypt' for encryption, 'decrypt' for decryption.

  Returns:
    The encrypted or decrypted message.
  """

  result = ""
  for char in text:
    if char.isalpha():
      # Determine the starting alphabet (A for uppercase, a for lowercase)
      start = ord('A') if char.isupper() else ord('a')
      # Calculate the shifted position
      shifted_position = (ord(char) - start + shift) % 26 + start
      # Convert back to a character
      result += chr(shifted_position)
    else:
      result += char
  return result

if __name__ == "__main__":
  message = input("Enter the message: ").upper()  # Convert to uppercase for case-insensitive handling
  shift = int(input("Enter the shift value: "))
  mode = input("Enter mode to perform (encryption/decryption): ").lower()

  if mode == 'encryption':
    encrypted_message = caesar_cipher(message, shift, 'encrypt')
    print("Encrypted message:", encrypted_message)
  elif mode == 'decryption':
    decrypted_message = caesar_cipher(message, -shift, 'decrypt') 
    print("Decrypted message:", decrypted_message)
  else:
    print("Invalid mode. Please enter 'encryption' or 'decryption'.")