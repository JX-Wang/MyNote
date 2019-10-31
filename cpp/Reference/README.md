C++可以使用引用进行实参的传递

C++传递参数的方式有值传递，指针传递和引用传递三种方式，引用传递参数会改变主调函数中的实参变量
```C++
#include <iostream>
using namespace std;
 
void swap(int& x, int& y);
 
int main ()
{
   int a = 100;
   int b = 200;
 
   cout << "交换前，a 的值：" << a << endl;
   cout << "交换前，b 的值：" << b << endl;
 
   swap(a, b);
 
   cout << "交换后，a 的值：" << a << endl;
   cout << "交换后，b 的值：" << b << endl;
 
   return 0;
}
 
void swap(int& x, int& y)
{
   int temp;
   temp = x; 
   x = y; 
   y = temp; 
  
   return;
}
```
