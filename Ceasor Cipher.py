listed_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listed_alphabets1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

try_again = 'yes'


while try_again.lower() == 'yes':
    encrypted_message = []
    decrypted_message = []
    if try_again.lower() == 'yes':
            choice = input("Type 'encode' for encrypt, type 'decode' for decrypt:\n")
            if choice.lower() == 'encode':
                message = (input("Please Enter Your Message : \n")).lower()
                shift_number = 1
                while 1 <= shift_number <= 25:
                    shift_number = int(input('Please Enter the Shift Number (1 to 25) : \n'))
                    if 1 <= shift_number <= 25:
                        break
                    else:
                        shift_number = 1

                for x in range(26):
                    listed_alphabets[x] = listed_alphabets1[(x + shift_number) % 26]

                for y in message:
                    index_of_letter = listed_alphabets.index(y)
                    encrypted_message.append(listed_alphabets1[index_of_letter])

                print(''.join(encrypted_message))



            elif choice == 'decode':
                message = (input("Please Enter Your Message : \n")).lower()
                shift_number = 1
                while 1 <= shift_number <= 25:
                    shift_number = int(input('Please Enter the Shift Number (1 to 25) : \n'))
                    if 1 <= shift_number <= 25:
                        break
                    else:
                        shift_number = 1
                for x in range(26):
                    listed_alphabets[x] = listed_alphabets1[(x + shift_number) % 26]

                for y in message:
                    index_of_letter = listed_alphabets1.index(y)
                    decrypted_message.append(listed_alphabets[index_of_letter])

                print(''.join(decrypted_message))

            try_again = input("Do You Want to Continue? Enter 'yes' for continue.")

input()
