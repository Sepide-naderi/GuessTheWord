import random

List_Of_Names = ['sepide', 'sahar', 'setayesh', 'ahmad', 'armin', 'ali', 'arman',
                 'asal', 'parvin', 'parvaneh', 'maryam', 'esmail', 'sajad']

Selected_Name = random.choice(List_Of_Names)
Guess_Count = len(Selected_Name)  # tedad dafaati ke user mitone char vared kone, be andaze tole esmie ke select shode
Guess_list = ['-'] * len(Selected_Name)  # be tole kalame '-' mizare

while Guess_Count > 0:                      #ta vaqti ke user dare hads mizane haminnjori betone guess kone
    Guess_char = input("enter a char : ")

    if Guess_char.isalpha():
        if Guess_char in Selected_Name:
            if Guess_char in Guess_list:
                print('u have guessed it before, try a new char.')
            else:
                for indx, char in enumerate(Selected_Name):
                    if char == Guess_char:
                        Guess_list[indx] = Guess_char
                print(f"ur guess was correct. => {' '.join(Guess_list)}")
                if not '-' in Guess_list:
                    print('u won!')
                    break
        else:
            print(f'wrong char! => remained guess: {Guess_Count}')
            Guess_Count -= 1
    else:
        print('enter a valid char!')
