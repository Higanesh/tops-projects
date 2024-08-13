/*
Que15. Write a C program to determine eligibility for admission to a professional course based on the following criteria
Eligibility Criteria : Marks in Maths >=65 and Marks in Phy >=55 and Marks in Chem>=50 and Total in all three subject >=190 or Total in Maths and Physics >=140 -------------------------------------- Input the marks obtained in
Physics :65 Input the marks obtained in Chemistry :51 Input the marks obtained in Mathematics :72 Total marks of Maths, Physics and Chemistry : 188 Total marks of Maths and Physics : 137 The candidate is not eligible.
*/

#include <stdio.h>

int main()
{
    int math_marks,physics_marks,chemistry_marks;
    int total_marks;
    printf("Enter marks of all subjects in following order:\n1. MATHS\n2. PHYSICS\n3. CHEMISTRY\n");
    scanf("%d %d %d",&math_marks,&physics_marks,&chemistry_marks);
    printf("maths marks - %d\nphysics marks - %d\nchemistry marks - %d\n",math_marks,physics_marks,chemistry_marks);
    total_marks = math_marks + physics_marks + chemistry_marks;
    if(math_marks >= 65 && physics_marks >= 55 && chemistry_marks >= 50 && total_marks >= 190 || math_marks+physics_marks >= 140)
    {
        printf("The candidate is ELIGIBLE");
    }
    else
    {
        printf("The candidate is NOT ELIGIBLE");
    }
    
    return 0;
}