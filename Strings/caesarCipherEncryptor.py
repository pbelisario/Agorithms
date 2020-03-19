def caesarCipherEncryptor(string, key):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = list(alphabet)

    new_string = []

    for letter in string:
        index = alphabet_list.index(letter)
        new_key = key % 26
        shifted_index = index + new_key
        if shifted_index <= 25:
            new_string.append(alphabet_list[shifted_index])
        else:
            new_string.append(alphabet_list[(-1+(shifted_index%25))])
    
    return ''.join(new_string)

print(caesarCipherEncryptor('pedro', 1))