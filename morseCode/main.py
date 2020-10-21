import encrypt
import decrypt

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

if __name__ == "__main__":
    while True:
        print('\nHello welcome to morsecode translator')
        print('press 1 for english to morse code')
        print('press 2 for morse code to english')
        print('press 3 to exit')
        x = input('')
        if x == '1':
            z = input('Enter the text you want to convert to morse code:')
            e_msg = encrypt.encrypt(z, MORSE_CODE_DICT)
            e_string = ""
            for i in e_msg:
                e_string = e_string + i + "/ "
            e_string = e_string[:-2]
            print('encrypted code:' + e_string)
        elif x == '2':
            z = input('Enter the code you want to convert to english:')
            d_msg = decrypt.decrypt(z, MORSE_CODE_DICT)
            d_string = ""
            for i in d_msg:
                d_string = d_string + i + ' '
            d_string = d_string[:-1]
            print(d_string)
        elif x == '3':
            exit(True)
        else:
            print('invalid input')
            continue
