/*
Que13. Write a program to find the max number from given two numbers using friend function
*/

#include<iostream>
using namespace std;

class Findmax{

    int no1,no2;

    public:
        void setNumbers(int n1,int n2){
            no1 = n1;
            no2 = n2;
        }

        void printNumbers(){
            cout<<"Number1 = "<<no1<<endl;
            cout<<"Number2 = "<<no2<<endl;
        }
        friend void maxNumber(Findmax &m);
};

void maxNumber(Findmax &m){
    int a = m.no1;
    int b = m.no2;
    a > b ? cout<<"Number1 is greater." : cout<<"Number2 is greater.";

}

int main(){

    Findmax max;
    int num1,num2;
    cout<<"Enter number1 and number 2: "<<endl;
    cin>>num1>>num2;
    max.setNumbers(num1,num2);
    max.printNumbers();
    maxNumber(max);
    return 0;
}