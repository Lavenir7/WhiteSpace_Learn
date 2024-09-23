    call label_0
label_0: # 主程序
    push 0
    push 58
    push 114
    push 101
    push 103
    push 101
    push 116
    push 110
    push 105
    push 95
    push 115
    push 111
    push 112
    push 32
    push 97
    push 32
    push 114
    push 101
    push 116
    push 110
    push 69
    call label_10
    # 读入数字，存在堆中{0: n}
    push 0
    readi
    push 0
    retrieve
    jn label_-1 # 读入负数结束程序
    # 判断1不是质数
    push 0
    retrieve
    push 1
    sub
    jz label_4
    # 从2开始试因子
    push 2
    call label_1
    jmp label_0
label_1: # 循环程序
    dup
    push 0
    retrieve
    sub
    jz label_2 # 查找到n，n无因子，即为质数
    dup
    push 0
    retrieve
    swap # subtop mod top
    mod
    jz label_4 # 模结果为0，找到因子，即非质数
    push 1
    add
    jmp label_1
label_2: # 输出是质数
    push 0
    push 10
    push 46
    push 101
    push 109
    push 105
    push 114
    push 80
    push 32
    push 97
    push 32
    push 115
    push 73
    call label_10
    drop
    ret
label_4: #输出不是质数
    push 0
    push 10
    push 46
    push 101
    push 109
    push 105
    push 114
    push 80
    push 32
    push 97
    push 32
    push 116
    push 111
    push 78
    call label_10
    drop
    ret
label_10: #打印字符串1
    dup
    jz label_11
    printc
    jmp label_10
label_11: #打印字符串2
    ret
label_-1: #结束程序
    push 0
    push 10
    push 46
    push 68
    push 78
    push 69
    call label_10
    end