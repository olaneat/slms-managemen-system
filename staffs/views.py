from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, get_list_or_404
from django.http import Http404
import os
from django.conf import settings
from .forms import StaffProfileForm
from django.contrib.auth.decorators import login_required
from .models import StaffProfile
from subjects.models import Assignment, Subject, SubmitAssignment
from subjects.forms import GiveAssignemtForm
# Create your views here.

def staff_index(request):
    staff = get_object_or_404(StaffProfile, user=request.user)
    teacher = staff.staff_id
    subjects = Subject.objects.filter(staff_id = teacher)
    assignments = ()
    return render(request, 'staffs/index.html', locals())

def download_assignment(request, path):
    fl_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(fl_path):
        with open(fl_path, 'r') as f:
            response = HttpResponse(f.read())


@login_required
def give_assignment(request):
    if request.method == 'POST':
        assignment_form = GiveAssignemtForm(request.POST)
        if assignment_form.is_valid() and assignment_form.cleaned_data:
            assignment_form.save()
            return redirect('staffs:staff_index')
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
            return redirect('staffs:staff_index')
        else:
            return HttpResponse('Kindly Cross check ur form again')
    else:
        profile_form = StaffProfileForm()
    return render(request, 'staffs/profile_form.html', {'profile_form':profile_form})


@login_required
def  check_assignment(request):
    staff = get_object_or_404(StaffProfileForm, user=request.user)
    staff_id = staff.staff_id
    subject = Subject.objects.filter(staff_id=staff_id)
    question = Assigment.objects.filter(question__contain='question', subject=subject)
    
    return render(request, 'staffs/submmited_assignment.html', {'submitted_assignment':submitted_assignment})

