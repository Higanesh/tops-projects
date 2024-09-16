/*
Que8. Write a program to Mathematic operation like Addition, Subtraction, Multiplication, Division Of two number using different parameters and Function Overloading
*/

#include<iostream>
using namespace std;

class Mathoperations{

public: 
    int mathop(int no1, int no2, int no3){
        int sum = 0;
        sum = no1 + no2 + no3;
        return sum;
    }

    int mathop(int no1, int no2){
        int sub = 0;
        if(no1 > no2){
            sub = no1 - no2;
            return sub;
        }else{
            sub = no2 - no1;
            return sub;
        }
    }

    float mathop(float no1, float no2, float no3){
        float product = 0;
        product = no1 * no2 * no3;
        return product;
    }

    float mathop(float no1, float no2){
        float res = 0;
        if(no2 == 0){
            cout<<"divide by zero error occure"<<endl;
            return res;
        }else{
            res = no1 / no2;
            return res;
        }
    }
};

int main(){
    Mathoperations m;
    cout<<"Sum of two numbers is: "<<m.mathop(2,3,4)<<endl;
    cout<<"Sub of two numbers is: "<<m.mathop(3,10)<<endl;
    cout<<"Product of two numbers is: "<<m.mathop((float)2.0,2.0,2.0)<<endl;
    cout<<"Result of two number is: "<<m.mathop((float)15.0,0.0);
    return 0;
}