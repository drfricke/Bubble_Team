# HOMEWORK 4 --- ES2
# Caesar Cipher

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: David Fricke
# NUMBER OF HOURS TO COMPLETE: 4 hrs
# YOUR COLLABORATION STATEMENT(s): I worked on this alone.
#
#
#*****************************************

# For this assignment you are going to implement a Caesar Cipher
# A Caesar cipher works by shifting every letter in the alphabet by a set amount.
# For example the string 'abc', with a shift of 1, would become 'bcd'
# For more information: https://en.wikipedia.org/wiki/Caesar_cipher

# Decode the following messages and say what shift you used to do so.
# 1. 'sn ad, nq mns sn ad: sgzs hr sgd ptdrshnm:'
# 2. 'sg2 wg am tojcfwhs qzogg'
# 3. 'nwcz akwzm ivl amdmv gmiza iow'

# ****************Answers****************
# 1.Message: to be, or not to be: that is the question:
#   Shift Amt: 25 (reversed)
# 2.Message: es2 is my favorite class
#   Shift Amt: 14 (reversed)
# 3.Message: four score and seven years ago
#   Shift Amt: 8 (reversed)

# message: string to be encrypt
# shift: integer number of letters to shift by.
#   You can assume we will only test with integers between 0 and 25
#   However, you can write your function to work with negatives and numbers greater than 25 if you wish
def encrypt(message, shift):      
    normalized_shift = int(shift)%26
    new_word = ''
    for letter in message:
        if 65 <= ord(letter) <= 90:
            if (ord(letter) + normalized_shift) > 90:
                over = (ord(letter) + normalized_shift) - 26
                new_letter = chr(over)
                new_word += new_letter
            else:
                new_letter = chr(ord(letter)+int(normalized_shift))
                new_word += new_letter
        elif 97 <= ord(letter) <= 122:
            if (ord(letter) + normalized_shift) > 122:
                over = (ord(letter) + normalized_shift) - 26
                new_letter = chr(over)
                new_word += new_letter
            else:
                new_letter = chr(ord(letter)+int(normalized_shift))
                new_word += new_letter
        else:
            new_letter = letter
            new_word += new_letter
    print(new_word)

def decrypt(message, shift):
    normalized_shift = (26 - int(shift))%26
    new_word = ''
    for letter in message:
        if 65 <= ord(letter) <= 90:
            if (ord(letter) + normalized_shift) > 90:
                over = (ord(letter) + normalized_shift) - 26
                new_letter = chr(over)
                new_word += new_letter
            else:
                new_letter = chr(ord(letter)+int(normalized_shift))
                new_word += new_letter
        elif 97 <= ord(letter) <= 122:
            if (ord(letter) + normalized_shift) > 122:
                over = (ord(letter) + normalized_shift) - 26
                new_letter = chr(over)
                new_word += new_letter
            else:
                new_letter = chr(ord(letter)+int(normalized_shift))
                new_word += new_letter
        else:
            new_letter = letter
            new_word += new_letter
    print(new_word)


menu = 'open'
print('Hi!')
print('Hope all the homework grading is going well!')
print("Type 'stop' to escape.")
while menu != 'stop':
    print('**************************************************')
    menu = input('Are we encrypting (e) or decryting(d)? ')
    menu = menu.lower()
    if menu == 'e':
        message = input('What message would you like to encrypt? ')
        print('**************************************************')
        shift = input('What number would you like to shift it by? ')
        print('**************************************************')
        if shift.isdigit():
            encrypt(message, shift)
        else:
            print("Nice try! That's not a proper number.")
            print("Let's start over.")
    elif menu == 'd':
        message = input('What message would you like to decrypt? ')
        print('**************************************************')
        print('What number would you like to reverse it by? ')
        shift = input("(If you don't know, try all by typing 'all') ")
        print('**************************************************')
        if shift == 'all':
            for i in range(1, 27):
                shift = i
                decrypt(message, shift)
                print('^Reversed by ', shift, '^')
            print('**************************************************')
            print('Look over results to find one that makes sense!')
        elif shift.isdigit():
            decrypt(message, shift)
        else:
            print("Nice try! That's not a proper number.")
            print("Let's start over.")
        
    elif menu == 'stop':
        print('Thanks for playing! Goodbye!')
        break
