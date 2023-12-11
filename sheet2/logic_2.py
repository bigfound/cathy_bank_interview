def calculate_chars_num(s: str):
    s_to_list = list(s)
    chars = set(s.lower().replace(' ', ''))
    chars_sum = {}
    for char in chars:
        chars_sum[char] = s_to_list.count(char)
    for char, num in chars_sum.items():
        print(char, num)


if __name__ == '__main__':
    input_str = 'Hello welcome to Cathay 60th year anniversary'
    print("Input is '{}'".format(input_str))
    print('Calculate chars number: ')
    calculate_chars_num(input_str)











