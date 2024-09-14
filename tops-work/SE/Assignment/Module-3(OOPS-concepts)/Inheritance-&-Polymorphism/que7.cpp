/*
Que7. Write a C++ Program to illustrates the use of Constructors in multilevel inheritance
*/

/*
multilevel inheritance is a type of inheritance where a class is derived from a base class, and then another class is derived from that derived class, forming a chain. Constructors play a key role in initializing objects of classes in such inheritance hierarchies. When an object of the most derived class is created, the constructors of all the base classes are called in the order of inheritance.
*/

#include<iostream>
using namespace std;

class Vehicle{
    private:
        string type = "petrol";
        string color = "Matte Blue";
    public:
        Vehicle(){
            cout<<"Type of vehicle: "<<type<<endl;
            cout<<"Color of vehicle: "<<color<<endl;   
        }
};

class Bike : public Vehicle{
    private:
        int seating = 2;
        int noOfWheels = 2;

    public:
        Bike(){
            cout<<"Seating capacity of bike: "<<seating<<endl;
            cout<<"Number of wheels bike has: "<<noOfWheels<<endl;
        }
};

class Access : public Bike{
    private:
        float avg = 45.00;
        string model_no = "125 bt";

    public:
        Access(){
            cout<<"Access give the avg of: "<<avg<<endl;
            cout<<"Model number of vehicle: "<<model_no;
        }
};

int main(){

    Access access;
    return 0;
}