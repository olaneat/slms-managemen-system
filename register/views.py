
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import LoginForm, StaffSignupForm, StudentSignupForm
from .models import UserRole
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import CreateView

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('staffs:index')
                elif user.is_student:
                    login(request, user)
                    return redirect('students:index')
                else:
                    return HttpResponse('inValid User')
            else:
                return HttpResponse('User not found')
        else:
            return HttpResponse('invalid user Details')
    else:
        login_form = LoginForm()
    return render(request, 'register/login.html', {'login_form': login_form})


    
class StudentSignUp(CreateView):
    model = UserRole
    form_class = StudentSignupForm
    template_name = 'register/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        user.save()
        login(self.request, user)
        return redirect('students:profile')

    
class StaffSignup(CreateView):
    model = UserRole
    form_class = StaffSignupForm
    template_name = 'register/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staff'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        user.save()
        login(self.request, user)
        return redirect('staffs:profile')
