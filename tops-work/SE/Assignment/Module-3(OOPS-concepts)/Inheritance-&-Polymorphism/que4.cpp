/*
Que4. Write a C++ Program display Student Mark sheet using Multiple inheritance
*/

#include<iostream>
using namespace std;

class Student
{
    protected:
        string name;
        int roll_no;
        string faculty;

    public:
        void get_student_details(){
            cout<<"Enter student name: "<<endl;
            cin>>name;
            cout<<"Enter student roll number: "<<endl;
            cin>>roll_no;
        }
    
        void display_student_details(){
            cout<<"Student name: "<<name;
            cout<<"Roll No.: "<<roll_no;
        }
};

class Marks{
    protected:
        float math,science,english;
    
    public:
        void get_marks(){
            cout<<"Enter marks of math: "<<endl;
            cin>>math;
            cout<<"Enter marks of science: "<<endl;
            cin>>science;
            cout<<"Enter marks of english: "<<endl;
            cin>>english;
        }

        void display_marks(){
            cout<<"Marks in Math: "<<math<<endl;
            cout<<"Marks in Science: "<<science<<endl;
            cout<<"Marks in English: "<<english<<endl;
        }
};

class Marksheet : public Student, public Marks{
    private:
        float total;
        float percentage;

    public:
        void calculateResult(){
            total = math + science + english;
            percentage = (total / 300) * 100;
        }

        void displayMarkSheet() {
        cout <<"\n---- Student Mark Sheet ----"<<endl;
        display_student_details();  
        display_marks();           
        cout<<"Total Marks: "<<total<<"/300"<<endl;
        cout<<"Percentage: "<<percentage<<"%"<<endl;

        if(percentage >= 60) {
            cout<<"Result: First Division"<<endl;
        } else if(percentage >= 50) {
            cout<<"Result: Second Division"<<endl;
        } else if (percentage >= 40) {
            cout<<"Result: Third Division"<<endl;
        } else {
            cout<<"Result: Fail"<<endl;
        }
    }
};

int main(){

    Marksheet m;
    m.get_student_details();
    m.get_marks();

    m.calculateResult();
    m.displayMarkSheet();
    return 0;
}
