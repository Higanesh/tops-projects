/*
Que2. Write a program of Addition, Subtraction, Division, Multiplication using constructor.
*/

#include<iostream>

using namespace std;

class Calculator{

    int num1, num2;

    public:
        Calculator(int num1,int num2){
            this->num1 = num1;
            this->num2 = num2;
        }
        
        int addition(){
            return num1 + num2;
        }

        int subtraction(){
            return num1 - num2;
        }

        int multiplication(){
            return num1 * num2;
        }

        int division(){
            return num1 / num2;
        }

};

int main(){
int n1,n2;
cout<<"Enter two numbers for Arithmetic Operations"<<endl;
cin>>n1>>n2;
Calculator cal(n1,n2);

cout<<"Addition of two numbers is: "<<cal.addition()<<endl;
cout<<"Subtraction of two numbers is: "<<cal.subtraction()<<endl;
cout<<"Multiplication of two numbers is: "<<cal.multiplication()<<endl;
cout<<"Division of two numbers is: "<<cal.division()<<endl;
return 0;
}