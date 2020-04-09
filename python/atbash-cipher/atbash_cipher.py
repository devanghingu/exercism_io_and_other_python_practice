from string import ascii_lowercase
atbash_table = str.maketrans(ascii_lowercase, ascii_lowercase[::-1]) # return all char table 


def translate(text):
    return_text=[]
    for c in text.lower():
        if c.isalnum():
            return_text.append(c)
    return ''.join(return_text).translate(atbash_table)

def encode(plain_text):
    print(atbash_table)
        
    cipher_text = translate(plain_text)
    return ' '.join(cipher_text[i:i + 5] for i in range(0, len(cipher_text), 5))

def decode(ciphered_text):
    return translate(ciphered_text)






