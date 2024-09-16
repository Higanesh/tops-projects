/*
Que12. Write a program to swap the two numbers using friend function without using third variable
*/

#include<iostream>
using namespace std;

class Swap{

    int no1,no2;

    public:
        void setNumbers(int n1,int n2){
            no1 = n1;
            no2 = n2;
        }

        void printNumbers(){
            cout<<"Before Swapping:"<<endl;
            cout<<"Number1 = "<<no1<<endl;
            cout<<"Number2 = "<<no2<<endl;
        }
        friend void swapNumber(Swap &s);
};

void swapNumber(Swap &s){
    int a = s.no1;
    int b = s.no2;
    a = a + b;
    b = a - b;
    a = a - b;
    cout<<"After Swapping:"<<endl;
    cout<<"Number1 = "<<a<<endl;
    cout<<"Number2 = "<<b<<endl;
}

int main(){

    Swap swap;
    int num1,num2;
    cout<<"Enter number1 and number 2 for swapping: "<<endl;
    cin>>num1>>num2;
    swap.setNumbers(num1,num2);
    swap.printNumbers();
    swapNumber(swap);
    return 0;
}