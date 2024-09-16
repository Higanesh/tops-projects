/*
Que1. Write a program of to swap the two values using template
*/

#include<iostream>
using namespace std;

template <typename T>
class Template{

    T val1, val2;

    public:

        Template(T val1, T val2){
            this->val1 = val1;
            this->val2 = val2;
        }

        void printValue(){
            cout<<"Before Swapping:"<<endl;
            cout<<"Value1 = "<<val1<<endl;
            cout<<"Value2 = "<<val2<<endl;
        }

        void swapValue(){
        T temp;
        temp = val1;
        val1 = val2;
        val2 = temp;
        cout<<"After Swapping:"<<endl;
        cout<<"Value1 = "<<val1<<endl;
        cout<<"Value2 = "<<val2<<endl;
    }
};


int main(){
    Template<float> temp(20.34,30.45);
    temp.printValue();
    temp.swapValue();
    return 0;
}