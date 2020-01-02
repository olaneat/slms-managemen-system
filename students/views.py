from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import UserProfile
from .forms import StudentProfileForm
from subjects.models import Subject, Assignment, SubmitAssignment
from subjects.forms import SubmitAssignemtForm
# Create your views here.

def student_index(request):
    student = get_object_or_404(UserProfile, user = request.user)
    student_klass = student.class_name
    assignment = Assignment.objects.filter(student_class = student_klass)
    return render(request, 'students/index.html', locals() )

def submit_assignment(request, id):
    assignment = get_object_or_404(Assignment, id=id)
    assignment_submitted = SubmitAssignment.objects.all()
    answers = assignment.answers.all()
    new_answer = None
    if request.method == 'POST':
        assignment_form = SubmitAssignemtForm(request.POST, request.FILES,)
        if assignment_form.is_valid() and assignment_form.cleaned_data:
            new_answer = assignment_form.save(commit=False)
            new_answer.assignment = assignment
            new_answer.save()           
            return HttpResponse('Assignment successfully submited')
    else:
        assignment_form = SubmitAssignemtForm()
    return render(request, 'subjects/assignment_detail.html', {'assignment': assignment,
                                                                'new_answer': new_answer,
                                                                'assignment_form': assignment_form})

def edit_profile(request):
    if  request.method == 'POST':
        profile_form = StudentProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid() and profile_form.cleaned_data:
            profile_form.save()
            return redirect('students:index')
    else:
        profile_form = StudentProfileForm()
    return render(request, 'students/profile_form.html', {'profile_form':profile_form})


