# WhiteSpace
## 简述
WhiteSpace 是一种只用空白字符（空格`SPACE`，制表位`TAB`和回车`LF`）编程的语言，而其它可见字符统统作为注释。

它本身是个指令式、基于堆栈的语言。其程式运行在上的虚拟机器均有一个堆栈（Stack）和堆（Heap）。程序员可自由将整数推进堆栈中（只可以是整数，因为暂时并无浮点数或实数工具），同时也可以通过堆作为变量和数据结构的暂存区。

###### 借助这种语言，可以在满篇空白的代码中插入一篇文章，从而在看起来完全无关的文章中隐藏一段代码。

---

## 语法
命令由一系列空格、制表位和换行符组成。所有其他字符都被忽略，因此可用于注释。例如，`Tab-Space-Space-Space` (add) 执行栈顶两个元素的算术加法。

命令的前一部分将被翻译为指令修改参数（IMP），IMP 后面所跟随的是操作。

### IMP 指令集如下：
IMP|指令集
:-:|:-:
`[Space]`|栈操作
`[Tab][Space]`|算术
`[Tab][Tab]`|堆操作
`[LF]`|指令控制
`[Tab][LF]`|I/O
### IMP 所对应的操作集如下：

IMP|命令|参数|说明
:-:|:-:|:-:|:-:
`[Space]`|`[Space]`|数字|将数字压入栈 (push)
`[Space]`|`[LF][Space]`|-|复制栈顶 (dup)
`[Space]`|`[Tab][Space]`|数字|拷贝栈中的第n个(栈顶为第0个)(n由参数给出)数据到栈顶 (copy)
`[Space]`|`[LF][Tab]`|-|交换栈顶的两个值 (swap)
`[Space]`|`[LF][LF]`|-|丢弃栈顶元素 (drop)
`[Space]`|`[Tab][LF]`|数字|保留栈顶的同时丢弃栈顶以下的n个数据 (slide)
`[Tab][Space]`|`[Space][Space]`|-|加法`subtop + top` (add)
`[Tab][Space]`|`[Space][Tab]`|-|减法`subtop - top` (sub)
`[Tab][Space]`|`[Space][LF]`|-|乘法`subtop * top` (mul)
`[Tab][Space]`|`[Tab][Space]`|-|除法`subtop / top` (div)
`[Tab][Space]`|`[Tab][Tab]`|-|求模`subtop mod top` (mod)
`[Tab][Tab]`|`[Space]`|-|保存到堆: (store)
`[Tab][Tab]`|`[Tab]`|-|从堆中取出数据 (retrieve)
`[LF]`|`[Space][Space]`|标签|在该处设定一个跳转标签 (label)
`[LF]`|`[Space][Tab]`|标签|调用子程序 (call)
`[LF]`|`[Space][LF]`|标签|跳转标签 (jmp)
`[LF]`|`[Tab][Space]`|标签|取出栈顶元素并判断：等于0则跳转标签 (jz)
`[LF]`|`[Tab][Tab]`|标签|取出栈顶元素并判断：小于0则跳转标签 (jn)
`[LF]`|`[Tab][LF]`|-|返回调用处 (ret)
`[LF]`|`[LF][LF]`|-|结束程序 (end)
`[Tab][LF]`|`[Space][Space]`|-|输出栈顶字符 (printc)
`[Tab][LF]`|`[Space][Tab]`|-|输出栈顶数字 (printi)
`[Tab][LF]`|`[Tab][Space]`|-|读取字符 (readc)
`[Tab][LF]`|`[Tab][Tab]`|-|读取数字 (readi)

### 与堆相关的几条说明：
- `store`: 【个人实践理解】将栈顶两个元素构成键值对`subtop: top`，然后放入堆中；
- `retrieve`: 【个人实践的理解】取出栈顶元素，索引堆中的元素，将索引到的元素放入栈顶，若索引不到，则构建新的键值对`top: 0`，然后将索引到的元素(0)放入栈顶；
- `readc`: 【个人实践理解】将读取的字符`char`与栈顶元素`top`构成键值对`top: char`，然后放入堆中；
- `readi`: 【个人实践理解】将读取的数字`int`与栈顶元素`top`构成键值对`top: int`，然后放入堆中；

### 数字
数字由 `[Space]`(0) 和 `[Tab]`(1) 组成，并以 `[LF]` 终止。数字中的第一个 `[Space]/[Tab]` 表示数字的符号，如果是 `[Space]` ，则数字为正`(+)`，如果是 `[Tab]` ，则数字为负`(-)`。其余的尾随空格和制表符代表二进制数的其余部分。

### 标签
标签只是以 `[LF]` 结尾的空格和制表符列表。只有一个全局命名空间，因此所有标签都必须是唯一的。

---

## 编辑和运行
我们可以在 [在线IDE](https://vii5ard.github.io/whitespace/) 对 whitespace 进行编辑和运行，同时有着许多示例代码可供参考。

在运行的时候，该网站 IDE 可以查看翻译的伪汇编代码（whitespace 虚拟机字节码），并且可以时刻中断来查看堆栈情况，方便调试程序和观察代码运行。
