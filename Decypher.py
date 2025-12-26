## Name: Seth Gersbach
## Student id: 14045002
##
## Coded_text = iyseivnryuvvkwqanliyilplvqigvwalhrghuklwcqmgxsjxsbhwnydlrvqqkstiyijiqhgatgvavfmctarylprvbyiyivmfpnkpkmgvrjvgsvtwvgiavtaixnhvfhcjzaalsaydieemumptxegdcgiqtcrkjiumnghfgamwcothvhgvwlrigzruqsprldwpajhvgrpehkmojthkvvfuhrgatzwuzhhvmtuaabkhbnqcmfowlrlxqignwlrnczxwlvxnmtjxzzrytaiyidwxmfbpeehcuguthvazqflneafawliseptjxoiuhrqerrkqrrwxuwijarrnehfgziptvhcvhlphmzidixsvfibytuyuiwmbgpehoivmaliiyemqxnexejgcqhvgvklwcqmixgjmlgrjibgxmfqdauxgvlwarytaiksuzhegxpdsvmossaxxlwzoinkczrybkegxbglsalwrwgvekwqeawxehwxhrqxckxzwxkumwfawdhvubhciyifcvlpcwgudvxxsscuwqxetszglqrrfmwfyypkinwkfgsbhhshgwvwmgsztcuiicdpvmnaixnhvfhcnekivpnotfafmueawwzwnqhafhcjpsdhvlapmitmhrjbsvpqlhfnmtulaasvrlxuifkbanlryejifxrkxjivjbephbdmluhrgmdiihcepvvpemkudrqtazqabhhehavjgzwlrytuijiokbotiremqxwxuwijarrfetxeugdwnlirxwapeaiwzpgartuxgrrvdlwvhcrvqkrrgbclikbrwuteveemumptcgsdqwmptaklgcjlgmdueq
##
##

## JCU academic word list https://www.jcu.edu.au/__data/assets/pdf_file/0004/1015348/Academic-Word-List.pdf
Coded_text = "iyseivnryuvvkwqanliyilplvqigvwalhrghuklwcqmgxsjxsbhwnydlrvqqkstiyijiqhgatgvavfmctarylprvbyiyivmfpnkpkmgvrjvgsvtwvgiavtaixnhvfhcjzaalsaydieemumptxegdcgiqtcrkjiumnghfgamwcothvhgvwlrigzruqsprldwpajhvgrpehkmojthkvvfuhrgatzwuzhhvmtuaabkhbnqcmfowlrlxqignwlrnczxwlvxnmtjxzzrytaiyidwxmfbpeehcuguthvazqflneafawliseptjxoiuhrqerrkqrrwxuwijarrnehfgziptvhcvhlphmzidixsvfibytuyuiwmbgpehoivmaliiyemqxnexejgcqhvgvklwcqmixgjmlgrjibgxmfqdauxgvlwarytaiksuzhegxpdsvmossaxxlwzoinkczrybkegxbglsalwrwgvekwqeawxehwxhrqxckxzwxkumwfawdhvubhciyifcvlpcwgudvxxsscuwqxetszglqrrfmwfyypkinwkfgsbhhshgwvwmgsztcuiicdpvmnaixnhvfhcnekivpnotfafmueawwzwnqhafhcjpsdhvlapmitmhrjbsvpqlhfnmtulaasvrlxuifkbanlryejifxrkxjivjbephbdmluhrgmdiihcepvvpemkudrqtazqabhhehavjgzwlrytuijiokbotiremqxwxuwijarrfetxeugdwnlirxwapeaiwzpgartuxgrrvdlwvhcrvqkrrgbclikbrwuteveemumptcgsdqwmptaklgcjlgmdueq"

import numpy as np


def main():
    ###
    ###Decode by brute forcing the code word
    ###

    # Display message
    print('message to decrypt')
    print(Coded_text)
    # finding length
    print("converted to numbers")
    pattern_finder = decypher(Coded_text)
    print(pattern_finder)
    # coincidences
    patterns(pattern_finder)

    # go though a list of keywords and decode them againts the encode text
    Coded_Num_text = decypher(Coded_text)
    for i in nine_letter_pr_words:
        print(i)
        Output = decode(Coded_Num_text, i)
        decoded(Output)

    # decode with a single keyword
    word = "president"
    result = decode(Coded_Num_text, word)
    answer = decoded(result)
    print(''.join(answer))

    Coded_Num_text = decypher(["v", "i", "t", "k", 'c', 'o', 'w', 's', "v", "i", "t", "k"])
    result = decode(Coded_Num_text, 'dead')
    print(decoded(result))

    # used to find repeating word combinations in case

    # repeats = find_repeated_patterns(''.join(answer))
    # for pattern, positions in repeats.items():
    #     print(f"Pattern: {pattern} at positions {positions}")
    #     distances = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]
    #     print(f"  Distances between repetitions: {distances}")

    ### KEYWORD HAS SOMETHING TO DO WITH PRONE


# thereby = prone up
# thereupon = prone by
# over = udon
# husk=beau

# pr =th
# heal = bust
# he = bu
# at = if
# def=fun
# tr =ph
# te=pu
# hp=bad
# im=am

# starting word cant be
# probaly doesnt start with the
# kn = yl
# gr=ch
# pros = them
# prog = they
# prome = these
# prone = there
# produc = the bot
# prostra =  the pen
# se=qu


###
###Decode by brute forcing the starting word
###

##menu() complex running

# def menu():
#     print("D: Decypher letters to numbers")
#     user_command = input("please enter a command word:")
#     while True:
#         if user_command == "D":
#             Coded_Num_text = decypher(Coded_text)
#         if user_command == "E":
#             break
#         if user_command == "B":
#             decoder_word = 'list'
#             decode(Coded_Num_text, decoder_word)
#         print("D: Decypher letters to numbers, E: escape")
#         user_command = input("please enter a command word:")

def decypher(input_text):
    Coded_Num_text = []
    for i in input_text:
        i = i.lower()
        z = ord(i)
        z = int(z) - 97
        Coded_Num_text.append(z)
    return Coded_Num_text


def decode(input_text, input_word):
    word_coded = decypher(input_word)
    counter = 0
    end = len(word_coded)
    return_word = []
    for i in input_text:
        if counter == end:
            counter = 0

        subtract = int(word_coded[counter])
        z = i - subtract

        counter += 1

        if z < 0:
            z = z + 26
        return_word.append(z)

    ##print(return_word)
    return return_word


def decoded(input_text):
    Decoded_Num_text = []
    for i in input_text:
        z = int(i) + 97
        z = chr(z)
        Decoded_Num_text.append(z)
    print(Decoded_Num_text)
    return Decoded_Num_text


def patterns(pattern_finder):
    displaced_text = pattern_finder.copy()
    max_length = len(displaced_text)
    matching_counter = 0
    coincidences_counter = []
    while max_length > 0:
        displaced_text.pop()
        displaced_text.insert(0, " ")
        max_length = max_length - 1

        for x, y in zip(pattern_finder, displaced_text):
            if (x or y) == " ":
                pass
            elif x == y:
                matching_counter += 1

        coincidences_counter.insert(-1, matching_counter)
        matching_counter = 0
    print("number of coincidences")
    print(coincidences_counter)


from collections import defaultdict


def find_repeated_patterns(text, min_len=3, max_len=6):
    patterns = defaultdict(list)

    for length in range(min_len, max_len + 1):
        for i in range(len(text) - length + 1):
            pattern = text[i:i + length]
            patterns[pattern].append(i)

    # Only keep patterns that occur more than once
    repeated = {pat: pos for pat, pos in patterns.items() if len(pos) > 1}
    return repeated


main()
