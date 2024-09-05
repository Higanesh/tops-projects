/*
Que4. Write a C++ program to create a class called Rectangle that has private member variables for length and width. Implement member functions to calculate the rectangle's area and perimeter.
*/

#include <iostream>

using namespace std;

class Rectangle{

    int length,width;
    public:
        float area,perimeter;
    Rectangle(){
        cout<<"Enter length and width"<<endl;
        cin>>length>>width;
    }

    public:
        float area_of_rectangle(){
            if(length < 0 && width < 0){
                cout<<"Invalid length and width"<<endl;
                return 0;
            }
            area = length * width;
            return area;
        }

        float perimeter_of_rectangle(){
            if(length < 0 && width < 0){
                cout<<"Invalid length and width"<<endl;
                return 0;
            }
            perimeter = 2 * (length + width);
            return perimeter;
        }
};

int main(){

    Rectangle rect;
    cout<<"Area of rectangle: "<<rect.area_of_rectangle()<<endl;
    cout<<"Perimeter of rectangle: "<<rect.perimeter_of_rectangle()<<endl;
    return 0;
}