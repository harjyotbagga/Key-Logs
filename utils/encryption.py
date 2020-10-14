import numpy as np

"""
Decryption of the Key-Logger Keys
"""

hill_key = "oplk"

def encrypt(msg):
    """
    Encryption Steps:
        # Replace spaces with nothing
        # Ask for keyword and get encryption matrix
        # Append zero if the messsage isn't divisble by 2
        # Populate message matrix
        # Calculate length of the message
        # Calculate P * C
        # Dot product
        # Modulate and add 65 to get back to the A-Z range in ascii
        # Change back to chr type and add to text
        # Repeat for the second column
    """
    msg = msg.replace(" ", "")
    C = make_key()
    len_check = len(msg) % 2 == 0
    if not len_check:
        msg += "0"
    P = create_matrix_of_integers_from_string(msg)
    msg_len = int(len(msg) / 2)
    encrypted_msg = ""
    for i in range(msg_len):
        row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
        integer = int(row_0 % 26 + 65)
        encrypted_msg += chr(integer)
        row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
        integer = int(row_1 % 26 + 65)
        encrypted_msg += chr(integer)
    return encrypted_msg

def make_key():
    """
    Makes sure the cipher determinant is relatively prime to 26 and only a/A - z/Z are given
    """
    determinant = 0
    C = None
    while True:
        cipher = hill_key
        C = create_matrix_of_integers_from_string(cipher)
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        inverse_element = find_multiplicative_inverse(determinant)
        if inverse_element == -1:
            print("Determinant is not relatively prime to 26, uninvertible key")
        elif np.amax(C) > 26 and np.amin(C) < 0:
            print("Only a-z characters are accepted")
            print(np.amax(C), np.amin(C))
        else:
            break
    return C

def find_multiplicative_inverse(determinant):
    multiplicative_inverse = -1
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse

def create_matrix_of_integers_from_string(string):
    """
    Maps strings to a list of integers: 
    a/A <-> 0, b/B <-> 1 ... z/Z <-> 25
    """
    integers = [chr_to_int(c) for c in string]
    length = len(integers)
    M = np.zeros((2, int(length / 2)), dtype=np.int32)
    iterator = 0
    for column in range(int(length / 2)):
        for row in range(2):
            M[row][column] = integers[iterator]
            iterator += 1
    return M

def chr_to_int(char):
    char = char.upper()
    integer = ord(char) - 65
    return integer
