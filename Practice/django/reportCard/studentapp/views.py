from django.shortcuts import render
from studentapp.models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    studentData = Student.objects.all()

    paginator = Paginator(studentData, 5) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    return render(request, 'index.html',{"studentData":page_obj})

def marks(request,id):
    studentId = StudentId.objects.get(student_id=id)
    student = Student.objects.get(student_id=studentId)
    studentMarks = Marks.objects.filter(student=student)
    
    total_obtained = sum(marks.marks for marks in studentMarks)  # Sum of obtained marks
    total_max = len(studentMarks) * 100  # Max marks (assuming each subject has a max of 100)
    
    # Calculate the percentage
    if total_max > 0:
        percentage = (total_obtained / total_max) * 100
    else:
        percentage = 0

    # Check for Pass/Fail status
    status = "Pass" if percentage >= 40 else "Fail"

    return render(request, 'marks.html', {"studentMarks":studentMarks,"percentage":percentage,"status":status})