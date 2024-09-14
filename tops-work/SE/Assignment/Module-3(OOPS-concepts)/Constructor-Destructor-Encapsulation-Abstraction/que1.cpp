/*
Que1. Write a program to find the multiplication values and the cubic values using inline function
*/

#include<iostream>
using namespace std;

    inline int multiply(int no1,int no2){
        return no1 * no2;   
    }

    inline int cubic(int no){
        return no * no * no;
    }

int main(){
    
    int no,no1,no2;
    cout<<"Enter values for num, num1 & num2: "<<endl;
    cin>>no>>no1>>no2;
    cout<<"multiply of two numbers: "<<multiply(no1,no2)<<endl;
    cout<<"Cube of number: "<<cubic(no);
    return 0;
}