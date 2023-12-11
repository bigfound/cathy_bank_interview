def get_last_member(n, quit_index):
    if n < 1:
        return -1
    members_index = [i for i in range(n)]
    start = 0
    quit_member = -1
    while members_index:
        quit_member_index = (start + quit_index - 1) % n
        quit_member = members_index.pop(quit_member_index)
        n -= 1
        start = quit_member_index
    return quit_member + 1


if __name__ == '__main__':
    n = 2
    quit_index = 3
    last_person_index = get_last_member(n, quit_index)
    print('n is {}'.format(n))
    print('The index of Person leaving is {}'.format(n))
    print('The last person index is {}'.format(last_person_index))
