/*
Que2. Write a C++ Program to find Area of Rectangle using inheritance
*/

#include<iostream>
using namespace std;

class Shape{

protected:
    float length;
    float width;
};

class Rectangle : public Shape{

public:
    Rectangle(float length,float width){
        this->length = length;
        this->width = width;
    }

    float area_of_rectangle(){
        return length * width;
    }
};

int main(){

    float l,w,area;
    cout<<"Enter length and height to calculate area of rectangle"<<endl;
    cin>>l>>w;
    Rectangle r(l,w);
    area = r.area_of_rectangle();
    cout<<"Area of rectangle is: "<<area;
    return 0;
}

