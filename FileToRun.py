import logging

# TODO: use logging instead of file.write()
# TODO: perform input validation for repeatability
# TODO: perform input validation for input_filename, cipher_filename, output_filename

output_file = open('output.txt', 'w')

# initial permutation table IP
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# inverse initial permutation table IP^-1
IP_INVERSE = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

# expansion table for transforming 32-bit block to 48-bits
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# Permuted Choice 1 table for transforming the key
PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# Permuted Choice 2 table for reducing key size to 48-bits
PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

# S-boxes
S = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
     [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
     [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
     [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
     [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
     [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
     [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
     [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
     ]

# Straight Permutation Table
P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]


def xor(block1: list, block2: list):
    """
    Performs the XOR operation on two blocks of same dimensions
    :param block1: list of first operand
    :param block2: list of second operand
    :return: block with result of XOR operation
    """
    if len(block1) != len(block2):
        output_file.write("Invalid operation. Inputs need to have same dimensions.")
        return

    return [a ^ b for a, b in zip(block1, block2)]


def initial_permutation(block: list) -> list:
    """
    Perform initial permutation on the block using IP table
    :arg block: list of 64 bits
    :return: list of 64 bits after permutation
    """
    return [block[x - 1] for x in IP]


def inverse_initial_permutation(block: list) -> list:
    """
    Perform inverse initial permutation on the block using IP^-1 table
    :arg block: list of 64 bits
    :return: list of 64 bits after inverse initial permutation
    """
    return [block[x - 1] for x in IP_INVERSE]


def sbox_substitution(six_bit: list, sbox_index: int) -> list:
    """
    Performs sbox substitution for one six bit input block
    :param six_bit: list of 6 int bits
    :param sbox_index: int ranging from numbers 0-7
    :return: list of 4 bits
    """

    row = int(''.join(str(b) for b in [six_bit[0], six_bit[5]]), 2)
    column = int(''.join(str(b) for b in six_bit[1:5]), 2)
    output = S[sbox_index][row][column]
    output = format(output, '04b')
    output = [int(bit) for bit in output]
    return output


def key_schedule(key: list) -> list:
    """
    Generate sub-keys from the given key using key schedule algorithm
    :arg key: list containing 56-bit key
    :return subkeys:
    """

    # check for odd parity
    key_after_parity = [key[i:i + 7] for i in range(0, len(key), 7)]
    for bit in key_after_parity:
        if bit.count(1) % 2:
            bit.append(0)
        else:
            bit.append(1)
    key_after_parity = [bit for byte in key_after_parity for bit in byte]
    output_file.write(f"\nKey before permute but after parity is:\n{''.join([str(bit) for bit in key_after_parity])}\n")

    # Permute the key using PC1 table
    key_after_permutation = [key_after_parity[x - 1] for x in PC1]
    output_file.write(f"\nKey after permute is:\n{''.join([str(bit) for bit in key_after_permutation])}\n")

    # Split the key into left and right 28-bit halves
    C, D = key_after_permutation[:28], key_after_permutation[28:]

    # Generate 16 sub-keys by rotating left halves and right halves by 1 or 2 bits
    subkeys = []
    for i in range(16):
        if i in [0, 1, 8, 15]:
            C = C[1:] + C[:1]
            D = D[1:] + D[:1]
        else:
            C = C[2:] + C[:2]
            D = D[2:] + D[:2]
        subkey = C + D
        subkey = [subkey[x - 1] for x in PC2]
        subkeys.append(subkey)

    return subkeys


def f_function(R: list, subkey: list) -> list:
    """
    Performs the f function on a 32-bit block and a 48-bit subkey
    :arg R: list of 32 bits (half block) of initial permutation input
    :arg subkey: list of 48 bits obtained from key_schedule
    :return: list of 32 bits (result of f-function)
    """
    # Expand the 32-bit block to 48-bits using E table
    R = [R[x - 1] for x in E]
    output_file.write(f"\nExpansion permutation: {''.join([str(bit) for bit in R])}\n")

    # XOR the expanded block with the subkey
    R = [x ^ y for x, y in zip(R, subkey)]
    output_file.write(f"\nXOR with key: {''.join([str(bit) for bit in R])}\n")

    # Perform S-Box substitution using S
    R = [R[i:i + 6] for i in range(0, len(R), 6)]

    S_boxes = []
    for i in range(8):
        S_boxes.append(sbox_substitution(R[i], i))

    result = [nibble for S_box in S_boxes for nibble in S_box]
    output_file.write(f"\nS-box permutation: {''.join([str(bit) for bit in result])}\n")

    # Perform permutation using P
    result = [result[p - 1] for p in P]
    output_file.write(f"\nP-box permutation: {''.join([str(bit) for bit in result])}")

    return result


def encrypt(plain_text_block: list, subkeys: list) -> list:
    """
    Encrypts a block of input text and performs 16 DES cycles
    :param plain_text_block: list of 64 bits
    :param subkeys: list of 48 bits
    :return: list of 64 bits of encrypted text
    """

    # permuted block
    plain_text_block = initial_permutation(plain_text_block)

    output_file.write(f"Initial permutation result: {''.join([str(b) for b in plain_text_block])}\n\n")

    # left and right permuted input blocks
    L, R = plain_text_block[:32], plain_text_block[32:]

    # DES cycles
    for i in range(16):
        output_file.write(f'\nIteration: {i + 1}\n')
        output_file.write(f'L_i-1:\n{"".join([str(bit) for bit in L])}\n\n'
                          f'R_i-1:\n{"".join([str(bit) for bit in R])}\n\n')
        temp = R
        R = xor(L, f_function(R, subkeys[i]))
        output_file.write(f"\n\nXOR with L_i-1 (This is R_i):\n{''.join([str(bit) for bit in R])}\n")
        L = temp

    # inverse initial permutation
    ciphertext = inverse_initial_permutation(R + L)

    output_file.write(f"\n\nFinal permutation: {''.join([str(bit) for bit in ciphertext])}\n\n\n")

    return ciphertext


def decrypt(ciphertext: list, subkeys: list) -> list:
    """
    Decrypts block of cipher text to return original plain text
    :param ciphertext: list of 64 bits
    :param subkeys: list of 48 bits
    :return: list of 64 bits of original plain text
    """

    # permuted block
    ciphertext = initial_permutation(ciphertext)

    # left and right permuted input blocks
    L, R = ciphertext[:32], ciphertext[32:]

    # reverse DES cycles for decryption
    for i in range(15, -1, -1):
        temp = R
        R = xor(L, f_function(R, subkeys[i]))
        L = temp

    # inverse initial permutation
    block = inverse_initial_permutation(R + L)

    output_file.write(f"\n\nDecrypted block: {''.join([str(bit) for bit in block])}")

    return block


def process_plain_text(filename: str) -> list:
    """
    Converts text file into a list of 64-bit blocks
    :param filename: string name of text file (.txt)
    :return blocks: list containing blocks of 64 bits representing filename
    """
    with open(filename, 'r') as file:
        text = file.read()

    output_file.write(f'Text to encrypt: {text}')

    # list containing bytes representing each character in text file
    bytes = [format(ord(char), '08b') for char in text if char.isalnum()]

    # zero padding
    while len(bytes) % 8 != 0:
        bytes.append('00000000')

    # list containing lists of bits
    bits = [[int(bit) for bit in byte] for byte in bytes]

    # list containing only bits
    bits = [bit for byte in bits for bit in byte]

    # list containing blocks of 64 bits
    blocks = [bits[i:i + 64] for i in range(0, len(bits), 64)]

    return blocks


def generate_key(password: str) -> list:
    """
    Converts password into a 56-bit key
    :param password: string user input
    :return: list of bits representing password
    """

    # list containing bytes representing each character in password
    bytes = [format(ord(char), '07b') for char in password if char.isalnum()]

    # flat list of 56 bits representing password
    key = [int(bit) for byte in bytes for bit in byte]

    return key


def input_password() -> str:
    """
    Accepts password entered by user
    :return password: valid user input
    """

    while True:
        # user input for a password
        password = input("Enter password (8 alphanumeric characters): ")

        # input validation
        if password == 'exit':
            print("Exiting program...")
            break
        if len(password) != 8:
            print("Invalid length. (exit to cancel)")
            continue
        if not password.isalnum():
            print("Invalid password. (exit to cancel)")
            continue
        break

    return password


def main():
    # user input
    password = input_password()
    key = generate_key(password)

    plain_text_blocks = process_plain_text('plaintext.txt')
    output_file.write(f'\nKey: {password}\n')

    subkeys = key_schedule(key)
    for a in range(len(subkeys)):
        output_file.write(f'\nKey {a + 1} is {"".join([str(bit) for bit in subkeys[a]])}')

    output_file.write(f'\n\nData after preprocessing:\n')
    for block in plain_text_blocks:
        for block_index in range(0, len(block), 8):
            output_file.write(''.join([str(bit) for bit in block[block_index:block_index + 8]]))
        output_file.write('\n')

    cipher_text_blocks = []
    for cipher_outer_index in range(len(plain_text_blocks)):
        output_file.write(f'\nBlock: {cipher_outer_index + 1}\n')
        cipher_text_blocks.append(encrypt(plain_text_blocks[cipher_outer_index], subkeys))

    decrypted_plain_text = []
    output_file.write(f"\n\n\nDecryption routine: \n\n\n")
    for cipher_text_block in cipher_text_blocks:
        decrypted_plain_text.append(decrypt(cipher_text_block, subkeys))


main()
