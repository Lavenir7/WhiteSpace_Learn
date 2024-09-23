    push 0
    push 32
    push 58
    push 114
    push 101
    push 98
    push 109
    push 117
    push 110
    push 32
    push 97
    push 32
    push 114
    push 101
    push 116
    push 110
    push 69
    call label_0
    push 0
    readi
    push 0
    retrieve
label_1:
    dup
    printi
    push 10
    printc
    dup
    push 1
    sub
    jz label_2
    call label_3
    jmp label_1
label_2:
    end
label_3:
    dup
    push 2
    mod
    jz label_4
    push 3
    mul
    push 1
    add
    ret
label_4:
    push 2
    div
    ret
    end
label_5:
    copy 1
    jz label_6
    dup
    copy 2
    store
    push 1
    add
    slide 1
    jmp label_5
label_6:
    swap
    store
    ret
label_0:
    dup
    jz label_7
    printc
    jmp label_0
label_7:
    drop
    ret
label_8:
    dup
    retrieve
    dup
    jz label_9
    printc
    push 1
    add
    jmp label_8
label_9:
    drop
    drop
    ret