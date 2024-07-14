alphabet = 'J	I	H	G	F	E	D	C	B	A	Z	Y	X	W	V	U	T	S	R	Q	P	O	Ñ	N	M	L	K'
custom_key = [3,5,7]
directions = [-1, 1, -1, 1]

def custom_cipher(message, keys, directions):
    
    final_message = ''
    used_indices = set()

    # Start at the first character
    current_index = 0

    alphabet_length = len(message)
    direction_index = 0

    while len(final_message) < alphabet_length:
        for key in keys:
            direction = directions[direction_index % len(directions)]
            direction_index += 1
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

def encrypt(message, key, directions):
    return custom_cipher(message, key, directions)

def decrypt(message, key, directions):
    reverse_directions = [-d for d in directions]
    return custom_cipher(message, key, reverse_directions)

alphabet_clean = alphabet.replace('\t', '').replace(' ', '').lower()

print(f'\nOriginal abc: {alphabet_clean}')
print(f'Key: {custom_key}')
print(f'Directions: {directions}')
encrypted = encrypt(alphabet_clean, custom_key,directions)
print(f'\nEncrypted abc: {encrypted}')
