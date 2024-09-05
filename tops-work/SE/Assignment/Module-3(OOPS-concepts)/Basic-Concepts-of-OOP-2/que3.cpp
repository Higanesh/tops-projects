/*
Que3. Write a C++ program to implement a class called Circle that has private member variables for radius. Include member functions to calculate the circle's area and circumference.
*/

#include <iostream>

using namespace std;

const float PI = 3.14;
class Circle{
    private:
        float radius;
    public:
        float area,circumference;

        Circle(){
            cout<<"Enter radius for circle "<<endl;
            cin>>radius;
        }
        
        float area_of_circle(){
            if(radius < 0){
                cout<<"Invalid Radius"<<endl;
                return 0;
            }
            area = PI * radius * radius;
            return area;
        }

        float circumference_of_circle(){
            if(radius < 0){
                cout<<"Invalid Radius"<<endl;
                return 0;
            }
            circumference = 2 * PI * radius;
            return circumference;
        }
};

int main(){

    Circle c;
    cout<<"Area of circle: "<<c.area_of_circle()<<endl;
    cout<<"Circumference of circle "<<c.circumference_of_circle()<<endl;
    return 0;
}