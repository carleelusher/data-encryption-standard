# What is secret key encryption?
#     In secret key encryption, a single shared key is used to encrypt and decrypt the message.

# What is symmetric key encryption?
#     Symmetric key encryption uses the same key for encryption and decryption.
#     Symmetric key encryption is a form of secret key encryption.

# What is substitution(confusion)?
#     Each plain text letter maps to unique ciphertext letter.
#     Can be of two types: mono-alphabetic and poly alphabetic.

# What is permutation (diffusion)?
#     The rearrangement of the letters in a ciphertext is permutation.

# What is DES?
#     DES is a combination of substitution and permutation (confusion and diffusion).
#     This combination is applied repeatedly for 16 cycles.


def process_input_text(plaintext):
    """

    :return:
    """

    # file object for plaintext
    with open(plaintext, 'r') as file:
        # string containing contents in file
        file_str = file.read()

    # list containing only numbers [0-9] and letters ['A'-'Z', 'a'-'z']
    file_processed_list = [c for c in file_str if c.isalnum()]

    # list containing binary ASCII values of elements in file_processed_list
    file_processed_bin = [bin(ord(b)).replace('0b', '') for b in file_processed_list]

    # int storing number of zero rows for padding
    num_fill_zeros = (len(file_processed_bin) // 8 + 1) * 8

    # loop for padding
    for i in range(num_fill_zeros - len(file_processed_bin)):
        file_processed_bin.append('00000000')

    # loop to make each binary ascii value 8 bits long
    for i in range(len(file_processed_bin)):
        bin_ascii_len = len(file_processed_bin[i])
        if bin_ascii_len < 8:
            for j in range(8 - bin_ascii_len):
                file_processed_bin[i] = '0' + file_processed_bin[i]
        file_processed_bin[i] = [int(bit) for bit in file_processed_bin[i]]

    # loop to make blocks of 64-bits
    temp = [[] for i in range(len(file_processed_bin) // 8)]

    for i in range(len(file_processed_bin)):
        x = i // 8
        temp[x].append(file_processed_bin.pop(0))

    print(len(temp))

    return temp


def generate_key_schedule():
    """

    :return:
    """

    password = input("Enter password (8 characters): ")


def perform_substitution():
    return


def perform_permutation():
    return


def encrypt_text(key, plaintext):
    """

    :return:
    """
    return


def decrypt_text():
    """

    :return:
    """
    return


def main():
    """

    :return:
    """


if __name__ == '__main__':
    main()
