

def alphabet_position(letter):
    lower_letter = letter.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return alphabet.index(lower_letter)

def rotate_character(char, rot):

    alphabet = ["a", "b", "c", "d", "e", "f", "g", 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if str(char).isalpha():
        char_index = alphabet_position(char)
        if char.isupper():
            return  alphabet[(char_index+rot)%26].upper()
        else:
            return  alphabet[(char_index+rot)%26].lower()
    else:
        return char


def encrypt(text,rot):
    s = ''
    newText = []
    for i in range(len(text)):
        newText.append(rotate_character(text[i],int(rot)))
    return s.join(newText)
