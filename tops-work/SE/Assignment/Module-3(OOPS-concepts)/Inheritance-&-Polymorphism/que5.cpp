/*
Que5. Assume that the test results of a batch of students are stored in three different classes. Class Students are storing the roll number. Class Test stores the marks obtained in two subjects and class result contains the total marks obtained in the test. The class result can inherit the details of the marks obtained in the test and roll number of students. (Multilevel Inheritance)
*/

#include<iostream>
using namespace std;

class Student{
protected:
    int roll_no;
};

class Test : public Student{
protected:
    int sub1_marks;
    int sub2_marks;

};

class Result : public Test{

    int total_marks;

public:
    void studentDatails(int roll_no,int sub1_marks,int sub2_marks){
        this->roll_no = roll_no;
        this->sub1_marks = sub1_marks;
        this->sub2_marks = sub2_marks;
    }

    void display(){
        cout<<"Roll no.: "<<roll_no<<endl;
        cout<<"Sub1 marks: "<<sub1_marks<<endl;
        cout<<"Sub2 marks: "<<sub2_marks<<endl;
        cout<<"Total marks: "<<sub1_marks+sub2_marks;
    }
};

int main(){

    Result r;
    int r_no,sub1,sub2;
    cout<<"Enter roll no, sub1 marks and sub2 marks of student: "<<endl;
    cin>>r_no>>sub1>>sub2;
    r.studentDatails(r_no,sub1,sub2);
    r.display();
    return 0;
}