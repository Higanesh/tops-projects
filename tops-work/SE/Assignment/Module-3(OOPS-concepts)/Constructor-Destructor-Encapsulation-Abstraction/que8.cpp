/*
Que8. Write a C++ program to implement a class called Student that has private member variables for name, class, roll number, and marks. Include member functions to calculate the grade based on the marks and display the student's information. Accept address from each student implement using of aggregation
*/

#include<iostream>

using namespace std;

class Stud_address{
    
public:
    string address;

    void accept_add(){
        cout<<"Enter student address: "<<endl;
        //cin>>address;
        getline(cin, address);
    }
    
    void show_add(){
        cout<<"Address: "<<address<<endl;
    }
};

class Student{

private:
    string name;
    string stud_class;
    int roll_no;
    int marks;
    Stud_address s_add;

public:
    Student(string name,string stud_class,int roll_no,int marks){
        this->name = name;
        this->stud_class = stud_class;
        this->roll_no = roll_no;
        this->marks = marks;
        s_add.accept_add();
    }
    
    char grade;
    void stud_grade(int marks){
        if(marks >= 85){
            grade = 'A';
        }else if(marks >= 65){
            grade = 'B';
        }else if(marks >= 35){
            grade = 'C';
        }else{
            grade = 'F';
        }
    }

    void display(){
        cout<<"Student Details:"<<endl;
        cout<<"Name: "<<name<<endl;
        cout<<"Class: "<<stud_class<<endl;
        cout<<"Roll no.: "<<roll_no<<endl;
        cout<<"Marks: "<<marks<<endl;
        cout<<"Grade: "<<grade<<endl;
        if(grade == 'F'){
            cout<<"your grade is F it means you are FAIL"<<endl;
        }
        s_add.show_add();
    }

};

int main(){
    
    string name,stud_class;
    int roll_no,marks;
    cout<<"Enter student details like name,class,roll no and marks"<<endl;
    cin>>name>>stud_class>>roll_no>>marks;
    Student s(name,stud_class,roll_no,marks);
    s.stud_grade(marks);
    s.display();
    return 0;
}