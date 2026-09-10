"""Caesar cipher and letter frequency analysis program."""

import string


def caesar_cipher(text, shift):
	"""Encrypt text by shifting each alphabetic character by shift positions."""
	alphabet = string.ascii_lowercase
	encrypted_text = ""

	for character in text:
		if character.isalpha() and character.lower() in alphabet:
			original_index = alphabet.index(character.lower())
			shifted_index = (original_index + shift) % len(alphabet)
			shifted_character = alphabet[shifted_index]
			encrypted_text += shifted_character.upper() if character.isupper() else shifted_character
		else:
			encrypted_text += character

	return encrypted_text


def caesar_decipher(cyphertext, shift):
	"""Decrypt Caesar-encrypted text using the original encryption shift."""
	return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
	"""Count occurrences of each alphabet letter, ignoring case and other characters."""
	frequencies = {letter: 0 for letter in string.ascii_lowercase}

	for character in text.lower():
		if character in frequencies:
			frequencies[character] += 1

	return frequencies


def display_frequency(frequencies):
	"""Print a frequency dictionary in alphabetical order."""
	for letter, count in frequencies.items():
		print(f"{letter}: {count}")


def main():
	"""Run the interactive Caesar cipher menu."""
	message = ""
	shift = 0

	while True:
		print("\nCaesar Cipher Menu")
		print("1. Enter a message")
		print("2. Enter a shift value")
		print("3. View cipher, letter frequencies, and deciphered text")
		print("4. Exit")

		choice = input("Choose an option: ").strip()

		if choice == "1":
			message = input("Enter a message: ")
		elif choice == "2":
			try:
				shift = int(input("Enter a shift value: "))
			except ValueError:
				print("Please enter a whole number for the shift.")
		elif choice == "3":
			if not message:
				print("Please enter a message first.")
				continue

			ciphered_text = caesar_cipher(message, shift)
			deciphered_text = caesar_decipher(ciphered_text, shift)

			print(f"\nCiphered text: {ciphered_text}")
			print("Letter frequencies:")
			display_frequency(letter_frequency(message))
			print(f"Deciphered text: {deciphered_text}")
		elif choice == "4":
			print("Goodbye!")
			break
		else:
			print("Please choose an option from 1 to 4.")


if __name__ == "__main__":
	main()
