label_0:
    push 1
label_1:
    dup
    printi
    push 10
    printc
    push 1
    add
    dup
    push 11
    sub
    jz label_2
    jmp label_1
label_2:
    drop
    end
label_3:
    add
    ret
label_4:
    dup
    retrieve
    dup
    jz label_5
    printc
    push 1
    add
    jmp label_4
label_5:
    drop
    drop
    ret
label_6:
    dup
    dup
    readc
    retrieve
    dup
    push 10
    sub
    jz label_7
    drop
    push 1
    add
    jmp label_6
label_7:
    drop
    push 1
    add
    push 0
    store
    ret
label_8:
    push 10
    push 13
    printc
    printc
    ret