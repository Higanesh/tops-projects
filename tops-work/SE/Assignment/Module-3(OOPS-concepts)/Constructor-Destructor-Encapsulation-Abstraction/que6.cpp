/*
Que6. Write a C++ program to implement a class called Employee that has private member variables for name, employee ID, and salary. Include member functions to calculate and set salary based on employee performance. Using of constructor
*/

#include<iostream>

using namespace std;

class Employee{

    private:
        string name;
        string emp_id;
        double salary;
    public:
        Employee(string name,string emp_id,double salary){
            this->name = name;
            this->emp_id = emp_id;
            this->salary = salary;
        }

        void setSalaryBasedOnPerformance(char performanceRating){

            switch (performanceRating)
            {
            case 'A': salary += salary * 0.20;
                    break;
            case 'B': salary += salary * 0.10;
                    break;
            case 'C': salary += salary * 0.05;
                    break;
            case 'D': salary;
                    break;
           default:
                cout<<"Invalid performance rating! No salary changes made."<<endl;
                return;
            }
            cout<<"Salary updated based on performance rating '"<<performanceRating<<"'."<< endl;
        }

        void display(){
            cout<<"Employee Name: "<<name<<endl;
            cout<<"Employee ID: "<<emp_id<<endl;
            cout<<"Employee Salary: Rs."<<salary<<endl;
        }
};

int main(){

    Employee e("Ganesh","1234",16000);
    
    cout<<"Initial employee details:"<<endl;
    e.display();

    char rating;
    cout<<"\nEnter performance rating (A, B, C, D): ";
    cin>>rating;

    e.setSalaryBasedOnPerformance(rating);

    cout<<"Updated employee details:"<<endl;
    e.display();
    return 0;
}