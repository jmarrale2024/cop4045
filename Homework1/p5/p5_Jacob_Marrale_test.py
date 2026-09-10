import unittest

from p5_Jacob_Marrale import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipher(unittest.TestCase):
    def test_cipher_preserves_case_spaces_and_punctuation(self):
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")

    def test_cipher_wraps_alphabet(self):
        self.assertEqual(caesar_cipher("xyz XYZ", 3), "abc ABC")

    def test_decipher_returns_original_text(self):
        message = "Meet me at 8 PM."
        encrypted_message = caesar_cipher(message, 11)
        self.assertEqual(caesar_decipher(encrypted_message, 11), message)

    def test_negative_shift(self):
        self.assertEqual(caesar_cipher("abc", -1), "zab")


class TestLetterFrequency(unittest.TestCase):
    def test_counts_letters_ignoring_case_and_nonletters(self):
        frequencies = letter_frequency("Aa! B-b? 123")
        self.assertEqual(frequencies["a"], 2)
        self.assertEqual(frequencies["b"], 2)
        self.assertEqual(frequencies["c"], 0)

    def test_returns_every_letter(self):
        frequencies = letter_frequency("")
        self.assertEqual(set(frequencies), set("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(all(count == 0 for count in frequencies.values()))


if __name__ == "__main__":
    unittest.main()