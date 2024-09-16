/*
Que9. Write a Program of Two 1D Matrix Addition using Operator Overloading
*/

#include<iostream>
using namespace std;

class Matrix{

    int size,res;

    public:
        int matrix1[10],matrix2[10];
        void inputmatrix(int size){

            cout<<"Enter elements of 1st Matrix: "<<endl;
            for(int i = 0; i < size; i++){
                cin>>matrix1[i];
            }

            cout<<"Enter elements of 2nd Matrix: "<<endl;
            for(int i = 0; i < size; i++){
                cin>>matrix2[i];
            }
        }

        void displayMatrix(){

            cout<<"Matrix-1: "<<endl;
            for(int i = 0; i < size; i++){
                cout<<matrix1[i]<<" ";
            }

            cout<<"Matrix-2: "<<endl;
            for(int i = 0; i < size; i++){
                cout<<matrix2[i]<<" ";
            }
        }

        Matrix operator+(Matrix obj){

            Matrix res[size];
            for(int i = 0; i < size; i++){
                res->matrix1[i] = matrix1[i] + matrix2[i];
            }
            //return res;
        }
};