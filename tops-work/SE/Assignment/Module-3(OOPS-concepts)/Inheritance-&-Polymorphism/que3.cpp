/*
Que3. Create a class person having members name and age. Derive a class student having member percentage. Derive another class teacher having member salary. Write necessary member function to initialize, read and write data. Write also Main function (Multiple Inheritance)
*/

#include<iostream>
using namespace std;

class Person{
protected:
    string name;
    int age;
};

class Student{
protected:
    float percentage;
};

class Teacher : public Person, public Student{
    double salary;

    // void settter(string name,int age,float percentage,double salary){
    //     this->name = name;
    //     this->age = age;
    //     this->percentage = percentage;
    //     this->salary = salary;
    // }
public:
    void read(){
        cout<<"Enter Student and Teacher details:"<<endl;
        cout<<"Student name: "<<endl;
        cin>>name;
        cout<<"Teacher name: "<<endl;
        cin>>name;
        cout<<"Student name: "<<name<<endl;
        cout<<"Teacher name: "<<name<<endl;
    }
};

int main(){
    Teacher t;
    t.read();
    return 0;
}