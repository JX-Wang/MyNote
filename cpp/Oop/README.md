C++的类

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

#### 类的继承

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
![avatar](https://github.com/JX-Wang/MyNote/tree/master/cpp/Oop/oop-inheriteasy.jpg)



