def caesar_cipher_decryption(e):

    for shift in range(0, 26):
        output_list = [chr(((ord(c) - 97 + shift) % 26) + 97) for c in e]
        output_string = ''.join(output_list)
        print("shift:", shift, output_string)

caesar_cipher_decryption("mjqqtbtwqi")