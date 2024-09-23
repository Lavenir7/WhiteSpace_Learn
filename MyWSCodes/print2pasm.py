# -*- coding: utf-8 -*-
'''String to PASM_CODE'''

PASM_Print_Code = '''label_n1:
    dup
    jz label_n2
    printc
    jmp label_n1
label_n2:
    ret'''

def PASM_String_Code(string):
    string = string[::-1]
    res = f'    push 0\n'
    for si in string:
        res += f'    push {ord(si)}\n'
    res += '    call label_n1'
    return res

if __name__ == '__main__':
    s = 'END.' # 要打印的内容
    print('PASM Print Code:')
    print('='*20)
    print(PASM_Print_Code)
    print('='*20)
    print()
    print('PASM String Code:')
    print('='*20)
    print(PASM_String_Code(s))
    print('='*20)
    print(f'{len(s)+2: >8} lines totle')
    if not s.endswith('\n'):
        print(f"\033[4;33m[Warning]: String doesn't end with '\\n', the '\\n' ASCII Code is '10'.\033[0m")