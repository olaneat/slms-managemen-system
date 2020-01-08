from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import ParentProfileForm
# Create your views here.

def index(request):

    return render( request, 'blog/slms_index.html')

def create_profile(request):
    if request.method == 'POST':
        profile_form = ParentProfileForm(request.POST, request.FILES, instance=request.user.parentprofile)
        if profile_form.is_valid() and profile_form.cleaned_data:
            profile_form.save()
            return redirect('parents:index')
        else:
            return HttpResponse('invalid input try again')
    else:
        profile_form = ParentProfileForm()
    return render(request, 'parents/profile_form.html', {'profile_form': profile_form})

