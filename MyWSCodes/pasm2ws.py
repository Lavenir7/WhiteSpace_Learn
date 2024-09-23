# -*- coding: utf-8 -*-
'''PASM_CODE TO WHITESPACE_CODE'''
import re

file_name = 'prime'
pasmDirPath = './WhiteSpace_Note/pasm_code/'
wsDirPath = './WhiteSpace_Note/ws_code/'

PASM_SUFFIX = '.pasm'

SPACE = 's'
TAB = 'T'
LF = 'n'

SPACE = ' '
TAB = '\t'
LF = '\n'
if len(SPACE) != 1 or len(TAB) != 1 or len(LF) != 1:
    exit('ERROR 1')

def integer2whitespace(n: int) -> str:
    if n == 0:
        return SPACE
    b = TAB if n < 0 else SPACE
    n = abs(n)
    b += ''.join([SPACE if s=='0' else TAB for s in bin(n)[2:]])
    return b

def adds(*sl: list[str]) -> str:
    '''字符串连接'''
    return ''.join(sl)

OperationSet_rev = {
    'push': adds(SPACE, SPACE),
    'dup': adds(SPACE, LF, SPACE),
    'copy': adds(SPACE, TAB, SPACE),
    'swap': adds(SPACE, LF, TAB),
    'drop': adds(SPACE, LF, LF),
    'slide': adds(SPACE, TAB, LF),
    'add': adds(TAB, SPACE, SPACE, SPACE),
    'sub': adds(TAB, SPACE, SPACE, TAB),
    'mul': adds(TAB, SPACE, SPACE, LF),
    'div': adds(TAB, SPACE, TAB, SPACE),
    'mod': adds(TAB, SPACE, TAB, TAB),
    'store': adds(TAB, TAB, SPACE),
    'retrieve': adds(TAB, TAB, TAB),
    'label': adds(LF, SPACE, SPACE),
    'call': adds(LF, SPACE, TAB),
    'jmp': adds(LF, SPACE, LF),
    'jz': adds(LF, TAB, SPACE),
    'jn': adds(LF, TAB, TAB),
    'ret': adds(LF, TAB, LF),
    'end': adds(LF, LF, LF),
    'printc': adds(TAB, LF, SPACE, SPACE),
    'printi': adds(TAB, LF, SPACE, TAB),
    'readc': adds(TAB, LF, TAB, SPACE),
    'readi': adds(TAB, LF, TAB, TAB),
    }

def del_comments(pasm_code_with_comments: str) -> str:
    '''
    删除pasm代码中的注释
    每一行#后的内容为注释
    '''
    pasm_code = ''
    for line in pasm_code_with_comments.split('\n'):
        if '#' in line:
            pasm_code += line.split('#')[0] + '\n'
        else:
            pasm_code += line + '\n'
    pasm_code = re.sub('\n[\s]*\n', '\n', pasm_code)
    return pasm_code[:-1]

def pasm2ws(pasm_code: str) -> str:
    '''将pasm代码转换成whitespace代码'''
    pasm_code = del_comments(pasm_code)
    ws_code = ''
    for c in pasm_code.split():
        if c.startswith('label_'):
            if c.endswith(':'):
                label = integer2whitespace(int(c.split('_')[1][:-1])) + LF
                ws_code += OperationSet_rev['label'] + label
            else:
                label = integer2whitespace(int(c.split('_')[1])) + LF
                ws_code += label
        else:
            try:
                c = int(c)
                ws_code += integer2whitespace(c) + LF
            except ValueError:
                ws_code += OperationSet_rev[c]
    return ws_code

if __name__ == '__main__':    
    with open(f'{pasmDirPath}{file_name}{PASM_SUFFIX}', encoding = 'utf-8') as f:
        pasm = f.read()
    ws = pasm2ws(pasm)
    with open(f'{wsDirPath}{file_name}.ws', 'w') as f:
        f.write(ws)
    print(f'{wsDirPath}{file_name}.ws 已写入')