/*
Que3. Write a C++ program to create a class called Car that has private member variables for company, model, and year. Implement member functions to get and set these variables.
*/

#include<iostream>

using namespace std;

class Car{

    string company;
    string model;
    string year;
public:
    void set_car_details(string company,string model,string year){
        this->company = company;
        this->model = model;
        this->year = year;
    }

    void get_car_details(){
        cout<<"Car detials are as follows:"<<endl;
        cout<<"Car company: "<<company<<endl;
        cout<<"Car model: "<<model<<endl;
        cout<<"Car year: "<<year;
    }
};

int main(){

    Car car;
    string comp,mod,yr;
    cout<<"Enter car details like"<<endl;
    cout<<"Car company: ";
    cin>>comp;
    cout<<"Car model: ";
    cin>>mod;
    cout<<"Car year: ";
    cin>>yr;
    car.set_car_details(comp,mod,yr);
    car.get_car_details();
    return 0;
}