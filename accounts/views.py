
from django.shortcuts import redirect, render
from accounts.forms import RegisterUserForm

# Create your views here.
def RegisterUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts/login')
    else:
        form = RegisterUserForm()

    context = {
        'form' : form
    }    

    return render(request, 'registration/register.html',context=context)