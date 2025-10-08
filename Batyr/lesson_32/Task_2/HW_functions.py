def encode_with_ceasar(in_str, code=0):
    result = ''
    code = code % 26

    for letter in in_str:
        letter_code = ord(letter)

        if letter_code < 65 or (90 < letter_code < 97) or (letter_code > 122):
            result += letter
            continue
        new_code = letter_code + code

        if code >= 0:
            if 65 <= letter_code <= 90 < new_code:
                codes_difference = (new_code - 90) % 26
                new_code = 64 + codes_difference

            if 97 <= letter_code <= 122 < new_code:
                codes_difference = (new_code - 122) % 26
                new_code = 96 + codes_difference

        else:
            if new_code < 65 <= letter_code <= 90:
                codes_difference = abs(65 - new_code) % 26

                new_code = 91 - codes_difference

            if new_code < 97 <= letter_code <= 122:
                codes_difference = abs(97 - new_code) % 26
                new_code = 123 - codes_difference
        result += chr(new_code)
    return result
# # TESTING
# print(encode_with_ceasar('ABCDe', 28))
# print(encode_with_ceasar('CDEFg', -28))
#
# print(encode_with_ceasar('dsakljlk', 1000))
# print(encode_with_ceasar('pemwxvxw', -1000))