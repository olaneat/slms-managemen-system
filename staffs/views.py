from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import StaffProfileForm
from django.contrib.auth.decorators import login_required
from .models import StaffProfile
from subjects.models import Assignment, Subject
from subjects.forms import GiveAssignemtForm
# Create your views here.
def staff_index(request):
    user = get_object_or_404(StaffProfile, user=request.user)
    username = user.surname
    subjects = Subject.objects.all()
    assignment = Assignment.objects.all()
    return render(request, 'staffs/index.html', locals())

@login_required
def give_assignment(request):
    if request.method == 'POST':
        assignment_form = GiveAssignemtForm(request.POST)
        if assignment_form.is_valid() and assignment_form.cleaned_data:
            assignment_form.save()
            return redirect('staffs:index')
        else:
            return HttpResponse('Kindly crosscheck the form again')
    else:
        assignment_form = GiveAssignemtForm()
    return render(request, 'subjects/give_assignment.html', {'assignment_form': assignment_form})

@login_required
def edit_profile(request):
    if  request.method == 'POST':
        profile_form = StaffProfileForm(request.POST, request.FILES, instance=request.user.staffprofile)
        if profile_form.is_valid() and profile_form.cleaned_data:
            profile_form.save()
            return redirect('staffs:index')
        else:
            return HttpResponse('Kindly Cross check ur form again')
    else:
        profile_form = StaffProfileForm()
    return render(request, 'staffs/profile_form.html', {'profile_form':profile_form})


@login_required
def  retrive_assignment(request):
    submitted_assignment = Assigment.object.filter(question__contain='question')
    return render(request, 'staffs/submmited_assignment.html', {'submitted_assignment':submitted_assignment})
