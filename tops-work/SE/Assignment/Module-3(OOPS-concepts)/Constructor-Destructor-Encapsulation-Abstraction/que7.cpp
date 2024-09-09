/*
Que7. Write a C++ program to implement a class called Date that has private member variables for day, month, and year. Include member functions to set and get these variables, as well as to validate if the date is valid.
*/

#include<iostream>

using namespace std;

class Date{

    int day,month,year;
public:
    void set_date(int day,int month,int year){
        this->day = day;
        this->month = month;
        this->year = year;
    }

    bool isValidDate(){

        if(day < 31 && month <= 12 && year > 1){
            return true;
        }else{
            return false;
        }
    } 

    void get_date(){
        if(isValidDate()){
            cout<<"Date: "<<day<<"-"<<month<<"-"<<year<<endl;
        }else{
            cout<<"INVALID DATE!";
        }
    }
};

int main(){

    Date date;
    int day,month,year;
    cout<<"Enter any date"<<endl;
    cin>>day>>month>>year;
    date.set_date(day,month,year);
    date.get_date();
}