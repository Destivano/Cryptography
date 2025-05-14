def word_to_ascii_list(word): # Votre word_to_ascii
    return [ord(char) for char in word]

def ascii_list_to_word(ascii_list):
    return ''.join(chr(code) for code in ascii_list)