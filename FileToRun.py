
def input_password() -> str:
    """
    Validates password entered by user
    :return: string with validated password
    """

    while True:
        # user input for a password
        password = input("Enter password (8 characters): ")

        # input validation
        if password == 'exit':
            break
        if len(password) != 8:
            print("Invalid length. (exit to cancel)")
            continue

        break

    return password


def process_input_text(filename: str) -> list:
    """
    Converts plain text to blocks of 64 bits with zero padding
    :arg: string file name of the plain text
    :return: list with preprocessed plain text
    """

    # file object for plaintext
    with open(filename, 'r') as file:
        # string containing contents in file
        file_str = file.read()

    # list containing only numbers [0-9] and letters ['A'-'Z', 'a'-'z']
    file_list = [character for character in file_str if character.isalnum()]

    # list containing binary ASCII values of elements in file list
    file_list = [bin(ord(character)).replace('0b', '') for character in file_list]

    # loop for zero padding
    while len(file_list) % 8 != 0:
        file_list.append('00000000')

    # loop to make each binary ascii value 8 bits long
    for i in range(len(file_list)):
        while len(file_list[i]) < 8:
            file_list[i] = '0' + file_list[i]
        file_list[i] = [int(bit) for bit in file_list[i]]

    # loop to make blocks of 64-bits
    preprocessed_plain_text = [[] for i in range(len(file_list) // 8)]
    for i in range(len(file_list)):
        preprocessed_plain_text[i // 8].append(file_list.pop(0))

    return preprocessed_plain_text


def generate_key_schedule():
    """

    :return:
    """


def perform_substitution():
    return


def perform_permutation(plain_text: list, permutation_table: list) -> list:
    permuted_plain_text = []
    return permuted_plain_text


def cipher_function():
    """

    :return:
    """
    return


def encipher_text(key, plain_text):
    """

    :return: cipher text
    """

    temp_text = plain_text

    # initial permutation table
    initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                           60, 52, 44, 36, 28, 20, 12, 4,
                           62, 54, 46, 38, 30, 22, 14, 6,
                           64, 56, 48, 40, 32, 24, 16, 8,
                           57, 49, 41, 33, 25, 17, 9, 1,
                           59, 51, 43, 35, 27, 19, 11, 3,
                           61, 53, 45, 37, 29, 21, 13, 5,
                           63, 55, 47, 39, 31, 23, 15, 7]

    # inverse initial permutation table
    inverse_initial_permutation = [40, 8, 48, 16, 56, 24, 64, 32,
                                   39, 7, 47, 15, 55, 23, 63, 31,
                                   38, 6, 46, 14, 54, 22, 62, 30,
                                   37, 5, 45, 13, 53, 21, 61, 29,
                                   36, 4, 44, 12, 52, 20, 60, 28,
                                   35, 3, 43, 11, 51, 19, 59, 27,
                                   34, 2, 42, 10, 50, 18, 58, 26,
                                   33, 1, 41, 9, 49, 17, 57, 25]

    # loop to permute each 64-bit block in plain text
    for i in range(len(temp_text)):
        temp_text[i] = perform_permutation(temp_text[i], initial_permutation)

    # TODO: perform complex key-dependant computation
    for key_index in range(16):
        for block_index in range(len(temp_text)):
            cipher_function()

    pre_output = []
    # loop to permute each 64-bit block in pre-output
    for block in pre_output:
        perform_permutation(block, inverse_initial_permutation)

    return


def decipher_text(key, cipher_text):
    """

    :return: plain text
    """
    return


def main():
    """

    :return:
    """

    plaint_text = process_input_text('plaintext.txt')
    # password = input_password()

    s_box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
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
              [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

    p_box = [16, 7, 20, 21,
             29, 12, 28, 17,
             1, 15, 23, 26,
             5, 18, 31, 10,
             2, 8, 24, 14,
             32, 27, 3, 9,
             19, 13, 30, 6,
             22, 11, 4, 25]




if __name__ == '__main__':
    main()
