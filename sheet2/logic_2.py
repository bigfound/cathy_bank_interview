def calculate_chars_num(s: str):
    s = s.upper()
    chars = set(s.upper().replace(' ', ''))
    chars_sum = {}
    for char in chars:
        chars_sum[char] = s.count(char)
        print(char, chars_sum[char])


if __name__ == '__main__':
    input_str = 'Hello welcome to Cathay 60th year anniversary'
    print("Input is '{}'".format(input_str))
    print('Calculate chars number: ')
    calculate_chars_num(input_str)











