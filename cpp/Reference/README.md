C++传递参数的方式有值传递，指针传递和引用传递三种方式，引用传递参数会改变主调函数中的实参变量
#### 值传递：
形参是实参的拷贝，改变形参的值并不会影响外部实参的值。从被调用函数的角度来说，值传递是单向的（实参->形参），参数的值只能传入，
不能传出。当函数内部需要修改参数，并且不希望这个改变影响调用者时，采用值传递。

#### 指针传递：
形参为指向实参地址的指针，当对形参的指向操作时，就相当于对实参本身进行的操作

#### 引用传递：
形参相当于是实参的“别名”，对形参的操作其实就是对实参的操作，在引用传递过程中，被调函数的形式参数虽然也作为局部变量在栈
中开辟了内存空间，但是这时存放的是由主调函数放进来的实参变量的地址。被调函数对形参的任何操作都被处理成间接寻址，即通过
栈中存放的地址访问主调函数中的实参变量。正因为如此，被调函数对形参做的任何操作都影响了主调函数中的实参变量

使用引用传递交换变量的值

```C++
#include <iostream>
using namespace std;

void c(int x){
    std::cout << "X address -> " << &x << std::endl;
    x++;
}

void c1(int& x){
    std::cout << "X address -> " << &x << std::endl;
    x++;
}

void c2(int *x){
    std::cout << "X address -> " << x << std::endl;
    *x=*x+1;
}

int main ()
{
    int x = 100;
    std::cout << "X original address is ->" << &x << '\n' << std::endl;

    c(x);
    std::cout << "After Value Deliver X is ->" << x << '\n' << std::endl;

    c1(x);
    std::cout << "After Reference Deliver X is ->" << x << '\n' << std::endl;

    c2(&x);
    std::cout << "After Pointer Deliver X is ->" << x << '\n' << std::endl;

   return 0;
}

```

输出结果如下
```C++
X original address is ->0x7ffc8fde10f4

X address -> 0x7ffc8fde10dc
After Value Deliver X is ->100

X address -> 0x7ffc8fde10f4
After Reference Deliver X is ->101

X address -> 0x7ffc8fde10f4
After Pointer Deliver X is ->102

```


