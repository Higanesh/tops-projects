/*
Que11. Write a program to calculate the area of circle, rectangle and triangle using Function Overloading
Rectangle: Area * breadth Triangle: ½ *Area* breadth Circle: Pi * Area *Area
*/

#include<iostream>
using namespace std;

class Area{

    public:
        float area(float length, float width){
            float areaOfRectangle;
            areaOfRectangle = length * width;
            return areaOfRectangle;
        }

        float area(float base, float height, char triangle){
            float areaOfRectangle;
            areaOfRectangle = 0.5 * base * height;
            return areaOfRectangle;
        }

        float area(float radius){
            const float PI = 3.14;
            float areaOfCircle;
            areaOfCircle = PI * radius * radius;
            return areaOfCircle;
        }
};

int main(){
    Area a;
    float length, width, base, height, radius;
    cout<<"Enter length and width for rectangle: "<<endl;
    cin>>length>>width;

    cout<<"Enter base and height for triangle: "<<endl;
    cin>>base>>height;

    cout<<"Enter radius for circle: "<<endl;
    cin>>radius;

    cout<<"Area of Rectangle: "<<a.area(length,width)<<endl;
    cout<<"Area of Triangle: "<<a.area(base,height,'T')<<endl;
    cout<<"Area of Circle: "<<a.area(radius);
    return 0;
}