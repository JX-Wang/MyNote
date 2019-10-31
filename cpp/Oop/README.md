## C++面向对象机制

一个简单的woody类
```C++
#include <iostream>
using namespace std;

class woody{
    public:
        double age;
        double height;
        char gender;
};

int main(){
    woody w1;
    woody w2;
    w1.age = 22;
    w1.height = 176;
    w1.gender = 'F';

    w2.age = 23;
    w2.height = 176.0;
    w2.gender = 'M';

    std::cout << w1.age << " " << w1.height << " " << w1.gender << std::endl;
    std::cout << w2.age << " " << w2.height << " " << w2.gender << std::endl;
}
```
### 空类

空类的大小不为0，C++编译器为空类安插一个字节.

因为C++不允许占用0字节的对象出现,所有对象都必须能够用内存地址定位.

```C++
class Empty{
};

int main(int argc, char** argv)
{
    std::cout << "Sizeof Empty class is -> " << sizeof(Empty) << std::endl;
    return 0;
}

输出: Sizeof Empty class is -> 1

```


### 类的继承

##### 简单继承
简单继承不涉及到虚函数和多重继承
子类对象含有父类对象的成员变量，并且布局上父类成员更靠前
```C++
class A
{
public:
	A(int a1=0,int a2=0);
	void A1();
protected:
	int a1;
	int a2;
};

class B :public  A
{
public:
	B(int a1=0,int a2=0,int b1=0);
	void B1();
protected:
	int b1;
```
![](https://github.com/JX-Wang/MyNote/blob/master/cpp/Oop/oop-inheriteasy.png)



