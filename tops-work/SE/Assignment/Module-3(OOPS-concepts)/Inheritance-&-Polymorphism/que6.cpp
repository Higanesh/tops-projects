/*
Que6. Write a C++ Program to show access to Private Public and Protected using Inheritance
*/

#include<iostream>
using namespace std;

class Base{

    private:
        int private_var = 10;

    protected:
        int protected_var = 20;

    public:
        int public_var = 30;

        void display_private_var(){
            cout<<"Private variable is: "<<private_var<<endl;
            cout<<"Public variable is (accessed in base class): "<<public_var<<endl;
        }
};

class Derive : public Base{
    public:
        void access_base_members(){
            public_var = 40;
            cout<<"Protected variable is: "<<protected_var<<endl;
            cout<<"Public variable is (accessed in derive class): "<<public_var<<endl;
        }
};

int main(){

    Derive obj;
    
    obj.display_private_var();
    obj.access_base_members();
    obj.public_var = 50;
    cout<<"Public variable is (accessed in main function): "<<obj.public_var<<endl;
    return 0;
}