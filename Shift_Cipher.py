import sys
import platform


# 加密
def shift_cipher_encrypt():
    list_s = []
    r_move = int(input('请输入加密移位参数(右移)：  '))
    s = input('请输入需要加密的字符： ')
    print("密文:", end='')
    c = ""
    for i in s:
        list_s.append(ord(i))
    for i in list_s:
        i += r_move
        while i > 127:
            i -= 128
        c += chr(i)
    return c


def shift_cipher_encrypt(s, r_move):
    list_s = []
    c = ""
    for i in s:
        list_s.append(ord(i))
    for i in list_s:
        i += r_move
        while i > 127:
            i -= 128
        c += chr(i)
    return c


# 解密


def shift_cipher_decrypt():
    l_move = int(input('请输入解密移位参数(左移)： '))
    s = input('请输入需要解密的字符： ')
    list_s = []
    m = ""
    for i in s:
        list_s.append(ord(i))
    for i in list_s:
        i -= l_move
        while i < 0:
            i += 128
        m += chr(i)
    return m


def shift_cipher_decrypt(s, l_move):
    list_s = []
    m = ""
    for i in s:
        list_s.append(ord(i))
    for i in list_s:
        i -= l_move
        while i < 0:
            i += 128
        m += chr(i)
    return m


# 爆破密文
def shift_brute(s, match_str):
    result = []
    for k in range(128):
        tmp = shift_cipher_decrypt(s, k)
        if match_str in tmp:
            result.append(tmp)
    return result


if __name__ == '__main__':
    logo = R'''
 ____  _     _  __ _         ____ _       _               
/ ___|| |__ (_)/ _| |_      / ___(_)_ __ | |__   ___ _ __ 
\___ \| '_ \| | |_| __|____| |   | | '_ \| '_ \ / _ \ '__|
 ___) | | | | |  _| ||_____| |___| | |_) | | | |  __/ |   
|____/|_| |_|_|_|  \__|     \____|_| .__/|_| |_|\___|_|   
                                   |_|                                        
    '''

    if platform.system() == 'Windows':
        import publish_logo

        publish_logo.printSkyBlue(logo)
    elif platform.system() == 'Linux':
        print(f"\033[36m{logo}\033[0m")
    print('\n')

    while 1:
        answer = input("请输入所需的操作：移位加密/E or 移位解密/D or 退出/Q: ")
        i = 1
        if answer.upper() == 'E':
            s = input('请输入需要加密的字符： ')
            r_move = int(input('请输入加密移位参数(右移)：'))
            print(shift_cipher_encrypt(s, r_move) + '\n')
        elif answer.upper() == 'D':
            s = input('请输入需要解密的字符： ')
            l_move = input('请输入解密移位参数(左移)，如果不知道请输入N：')
            if l_move.upper() == 'N':
                match_str = input('请输入您需要匹配的字符串，没有请不填：')
                print("可能的明文:" + shift_brute(s, match_str))
            elif l_move.isnumeric():
                l_move = int(l_move)
                print("明文为:" + shift_cipher_decrypt(s, l_move), end="\n")
        elif answer.upper() == 'Q':
            sys.exit()
        else:
            print('输入错误！')
