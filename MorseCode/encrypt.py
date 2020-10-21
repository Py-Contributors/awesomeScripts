import winsound
import time


def encrypt(msg, MORSE_CODE_DICTIONARY):
    li1 = list(MORSE_CODE_DICTIONARY.keys())
    wordlist = msg.split(" ")
    EncryptedMessage = list()
    MorseWord = ""
    for i in wordlist:
        for j in i:
            if j.upper() not in li1:
                EncryptedMessage.clear()
                EncryptedMessage.append(
                    'CAN NOT BE TRANSLATED TO MORSE CODE!!')
                return EncryptedMessage
            MorseWord = MorseWord + MORSE_CODE_DICTIONARY[j.upper()]
            MorseWord = MorseWord + " "
        EncryptedMessage.append(MorseWord)
        MorseWord = ""
    return EncryptedMessage


def MakeSound(EncryptedMessage):
    for i in EncryptedMessage:
        for j in i:
            LetterList = j.split(" ")
            for k in LetterList:
                if k == '.':
                    winsound.Beep(2500, 400)
                    # time.sleep(0.001)
                elif k == '-':
                    winsound.Beep(2500, 800)
                    # time.sleep(0.001)
            time.sleep(1.5)
        time.sleep(3)


if __name__ == "__main__":
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
    e = encrypt('', MORSE_CODE_DICT)
    MakeSound(e)
