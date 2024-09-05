/*
Que1. WAP to create simple calculator using class
*/

#include <iostream>

using namespace std;

class Calculator
{
    public:
    int a = 20,b = 3,res;

    int addition(){
        return a + b;
    }

    int subtraction(){
        return a - b;
    }

    int multiplication(){
        return a * b;
    }

    float division(){
        return a / b;
    }

    int modulus(){
        return a % b;
    }
};

int main(){

    Calculator cal;
    cout<<cal.addition()<<endl;
    cout<<cal.subtraction()<<endl;
    cout<<cal.multiplication()<<endl;
    cout<<cal.division()<<endl;
    cout<<cal.modulus();
    return 0;
}