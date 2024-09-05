/*
Que5. Write a C++ program to create a class called Person that has private member variables for name, age and country. Implement member functions to set and get the values of these variables.
*/

#include <iostream>

using namespace std;

class Person{

    string name;
    int age;
    string country;

    public:
        void set_values(string name,int age,string country){
            this->name = name;
            this->age = age;
            this->country = country;
        }

        int get_values(){
            cout<<"Name :"<<name<<endl;
            cout<<"Age: "<<age<<endl;
            cout<<"Country: "<<country<<endl;
        }
};

int main(){

    Person p;
    p.set_values("Ganesh",24,"India");
    p.get_values();
    return 0;
}