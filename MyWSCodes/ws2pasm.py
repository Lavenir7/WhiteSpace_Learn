# -*- coding: utf-8 -*-
'''WHITESPACE_CODE TO PASM_CODE'''

file_name = 'prime'
pasmDirPath = './WhiteSpace_Note/pasm_code'
wsDirPath = './WhiteSpace_Note/ws_code'
PASM_SUFFIX = '.pasm'

SPACE = 's'
TAB = 'T'
LF = 'n'

SPACE = ' '
TAB = '\t'
LF = '\n'
if len(SPACE) != 1 or len(TAB) != 1 or len(LF) != 1:
    exit('ERROR 1')

EMPTY = 0
NUMBER = 1
LABEL = 2

poorne = {SPACE: 1, TAB: -1}

OPSEPPARAM_NUMBER = ' '
OPSEPPARAM_LABEL = '_'
COMMANDSEP = '\n'
BEFORETAB = '    '


LabelDict: dict = {}

def whitespace2integer(bins: str) -> int:
    '''二进制str转数字int'''
    return sum([2**i for i,k in enumerate(bins[::-1]) if k==TAB])

def adds(*sl: list[str]) -> str:
    '''字符串连接'''
    return ''.join(sl)

OperationSet = { # IMP操作集
    adds(SPACE): {
        adds(SPACE): (NUMBER, 'push', '将数字压入栈'),
        adds(LF, SPACE): (EMPTY, 'dup', '复制栈顶'),
        adds(TAB, SPACE): (NUMBER, 'copy', '拷贝栈中第n个(n由参数给出)数据到栈顶'),
        adds(LF, TAB): (EMPTY, 'swap', '交换栈顶的两个值'),
        adds(LF, LF): (EMPTY, 'drop', '丢弃栈顶'),
        adds(TAB, LF): (NUMBER, 'slide', '保留栈顶的同时丢弃n个数据'),
    },
    adds(TAB, SPACE): {
        adds(SPACE, SPACE): (EMPTY, 'add', '加法'),
        adds(SPACE, TAB): (EMPTY, 'sub', '减法'),
        adds(SPACE, LF): (EMPTY, 'mul', '乘法'),
        adds(TAB, SPACE): (EMPTY, 'div', '除法'),
        adds(TAB, TAB): (EMPTY, 'mod', '求模'),
    },
    adds(TAB, TAB): {
        adds(SPACE): (EMPTY, 'store', '保存到堆'),
        adds(TAB): (EMPTY, 'retrieve', '从堆中取出数据'),
    },
    adds(LF): {
        adds(SPACE, SPACE): (LABEL, 'label', '在该处设定一个跳转标签s(s由参数给出)'),
        adds(SPACE, TAB): (LABEL, 'call label', '调用子程序s'),
        adds(SPACE, LF): (LABEL, 'jmp label', '跳转标签s'),
        adds(TAB, SPACE): (LABEL, 'jz label', '如果栈顶等于0则跳转标签s'),
        adds(TAB, TAB): (LABEL, 'jn label', '如果栈顶小于0则跳转标签s'),
        adds(TAB, LF): (EMPTY, 'ret', '结束子程序'),
        adds(LF, LF): (EMPTY, 'end', '结束程序'),
    },
    adds(TAB, LF): {
        adds(SPACE, SPACE): (EMPTY, 'printc', '输出栈顶字符'),
        adds(SPACE, TAB): (EMPTY, 'printi', '输出栈顶数字'),
        adds(TAB, SPACE): (EMPTY, 'readc', '读取字符放置栈顶'),
        adds(TAB, TAB): (EMPTY, 'readi', '读取数字放置栈顶'),
    }
}

def ws2pasm(ws_code: str) -> str:
    '''将ws代码转成pasm代码'''
    pasm_code = ''
    piece_instruct = ''
    char_index = 0
    ws_code_lens = len(ws_code)
    while char_index < ws_code_lens:
        piece_instruct += ws_code[char_index]
        char_index += 1
        if piece_instruct in OperationSet: # 找到一个指令
            piece_op = ''
            if char_index == ws_code_lens:
                break
            while (piece_op not in OperationSet[piece_instruct]): # 找到指令所执行的操作
                piece_op += ws_code[char_index]
                char_index += 1
                if char_index == ws_code_lens:
                    break
            if adds(piece_instruct, piece_op) == adds(LF, SPACE, SPACE): # 设定标签操作
                pasm_code += OperationSet[piece_instruct][piece_op][1]
            else:
                pasm_code += BEFORETAB + OperationSet[piece_instruct][piece_op][1]
            if char_index == ws_code_lens:
                break
            if OperationSet[piece_instruct][piece_op][0] == EMPTY: # 操作无参数
                pasm_code += COMMANDSEP
            elif OperationSet[piece_instruct][piece_op][0] == NUMBER: # 操作有数字参数
                param = ''
                while True:
                    char = ws_code[char_index]
                    char_index += 1
                    param += char
                    if char == LF or char_index == ws_code_lens: # 读到LF时停止读取参数
                        break
                if param[-1] != LF:
                    continue
                if param == LF:
                    param_int = 0
                else:
                    param_int = whitespace2integer(param[1:-1])*poorne[param[0]]
                pasm_code += OPSEPPARAM_NUMBER + str(param_int) + COMMANDSEP
            elif OperationSet[piece_instruct][piece_op][0] == LABEL: # 操作有标签参数
                param = ''
                while True:
                    char = ws_code[char_index]
                    char_index += 1
                    param += char
                    if char == LF or char_index == ws_code_lens: # 读到LF时停止读取参数
                        break
                if param[-1] != LF:
                    continue
                if param not in LabelDict:
                    LabelDict[param] = len(LabelDict)
                if adds(piece_instruct, piece_op) == adds(LF, SPACE, SPACE): # 设定标签操作
                    pasm_code += OPSEPPARAM_LABEL + f'{LabelDict[param]}:' + COMMANDSEP
                else:
                    pasm_code += OPSEPPARAM_LABEL + str(LabelDict[param]) + COMMANDSEP
            else: # 
                exit('ERROR -999')
            piece_instruct = ''
    return pasm_code

if __name__ == '__main__':
    with open(f'{wsDirPath}{file_name}.ws') as f:
        ws = f.read()
    pasm = ws2pasm(ws)
    with open(f'{pasmDirPath}{file_name}{PASM_SUFFIX}', 'w') as f:
        f.write(pasm)
    print(f'{pasmDirPath}{file_name}{PASM_SUFFIX} 已写入')