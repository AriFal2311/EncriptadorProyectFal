alphabet = 'T	W	H	L	B	X	U	R	I	S	K	D	J	A	E	O	V	F	Y	P	N	Z	G	Q	C	M'
custom_key = [3, 5]

def custom_cipher(message, keys, direction=1):
    
    final_message = ''
    used_indices = set()

    # Start at the first character
    current_index = 0

    alphabet_length = len(message)

    while len(final_message) < alphabet_length:
        for key in keys:
            """if key[1]== -1:
                direction = -1
            else:
                direction = 1"""
            count = 0
            # while count <= key:
            while count < key:
                current_index = (current_index + direction) % alphabet_length
                if current_index not in used_indices:
                    count += 1
            
            while current_index in used_indices:
                current_index = (current_index + direction) % alphabet_length

            final_message += message[current_index]
            used_indices.add(current_index)
            if len(final_message) == alphabet_length:
                break
        

    return final_message

def encrypt(message, key):
    return custom_cipher(message, key)
    
def decrypt(message, key):
    # Decryption logic is more complex and might need reverse implementation
    return custom_cipher(message, key, -1)

alphabet_clean = alphabet.replace('\t', '').replace(' ', '').lower()

print(f'\nOriginal abc: {alphabet_clean}')
print(f'Key: {custom_key}')
encrypted = encrypt(alphabet_clean, custom_key)
print(f'\nEncrypted abc: {encrypted}')
