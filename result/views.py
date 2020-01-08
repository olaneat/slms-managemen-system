from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from students.models import UserProfile
from .forms import SubjectOfferedForm
# Create your views here.

def add_subject_score(request):
    if request.method == 'POST':
        grade_form = SubjectOfferedForm(request.POST)
        if grade_form.is_valid() and grade_form.cleaned_data:
            grade_form.save()
            return HttpResponse('subject scores successfully added')
        else:
            return HttpResponse('invalid input try again')
    else:
        grade_form = SubjectOfferedForm()
    return render(request, 'result/scores_form.html', {'grade_form':grade_form})


def student_result(request):
    students = get_object_or_404(UserProfile, user=request.user)
    student = Student.objects.get(student_reg_no =students.student_id)
    term = get_object_or_404(Term, current_term = True)
    student_num = students.student_id
    session = get_object_or_404(Session, is_current_session = True)
    subject_result = SubjectOffered.objects.filter(student_number = student_num, term=term)
    result = Result.objects.get(student_number=student_num, term=term, session=session)
    return render(request, 'result/terminal_result.html', locals())