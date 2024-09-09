/*
Que5. Write a C++ program to create a class called Triangle that has private member variables for the lengths of its three sides. Implement member functions to determine if the triangle is equilateral, isosceles, or scalene.
*/

#include<iostream>

using namespace std;

class Triangle{

private:
    float a,b,c;
public:
    void equilateral(){
        cout<<"Triangle is equilateral";
    }

    void isosceles(){
        cout<<"Triangle is isosceles";
    }

    void scalene(){
        cout<<"Triangle is scalene";
    }
};

int main(){

    Triangle t;
    float x,y,z;
    cout<<"Enter three sides lenght for triangle"<<endl;
    cin>>x>>y>>z;
    if((x+y+z) == 180){
        if(x == y && y == z){
        t.equilateral();
        }else if(x == y || y == z || x == z){
            t.isosceles();
        }else{
            t.scalene();
        }
    }else{
        cout<<"Lenght of sides are invalid";
    }
       return 0;
}