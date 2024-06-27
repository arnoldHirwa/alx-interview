#!/usr/bin/python3
""" UTF8 Module """


def validUTF8(data):
    """ function for validating utf8 """
    flag = False
    jump_list = {30: 3, 14: 4, 6: 5}
    char_leng = {3: 3, 4: 2, 5: 1}
    list_len = 0
    if (len(data) == 0) or (len(data) == 1 and data[0] >> 7 == 0):
        return True
    for num in data:
        if list_len:
            list_len -= 1
        else:
            flag = False
        if len(bin(num)[2:]) == 9:
            num = int(bin(num)[3:], 2)
        if num >> 7 != 0 and len(bin(num)[2:]) >= 8:
            if (not flag and num >> 6 == 2):
                return False
            elif (flag and num >> 6 != 2):
                return False
            for test_point, shift in jump_list.items():
                if num >> shift == test_point:
                    list_len = char_leng[shift]
                    break
            if not (list_len or flag):
                return False
            else:
                flag = True
        elif num >> 7 == 0 and flag:
            return False
    if list_len:
        return False
    return True
