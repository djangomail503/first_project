from django.shortcuts import render
from django.http import HttpResponse
from first_app import forms

from . import models

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse


#---------------------------------
from django.views.generic import CreateView
# Create your views here.

#--------------------------------
class PostCreateView(CreateView):

    model = models.Post
    form_class = forms.PostModelForm
    template_name = 'first_app/post_create.html'
    #context_object_name = 'my_form'

#-------------------------------














def user_login(request):

    if request.method=='POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password=password)

        if user:
            login(request, user)
            request.session['user_login'] = True

            #return HttpResponse("<h1>Logged In</h1>")
            return redirect(reverse('home'))

        else:
            return HttpResponse("<h1>Credentials not matched</h1>")


    return render(request, template_name='register/login.html')



#-----------------------------------------------------------------------

def user_logout(request):

    del request.session['user_login']

    logout(request)

    return redirect(reverse('home'))


















def profile_view_fn(request):
    prof_obj = models.UserProfileModel.objects.get(pk=1)
    context = {'object': prof_obj}
    return render(request, template_name='register/profile_view.html', context=context)









def user_create_view(request):

    form_obj = forms.UserModelForm()

    if request.method == 'POST':
        form_obj = forms.UserModelForm(request.POST)
        if form_obj.is_valid():
            var = form_obj.save(commit=False)

            pwd  = request.POST.get('password') 
            var.set_password(pwd)
            var.save()
            return HttpResponse("Your Model Object is Saved ")
        else:
            return HttpResponse(f'<h1> {form_obj.errors.as_data()} </h1>')

    return render(request, template_name='register/user_register.html', context={'my_form':form_obj})














def user_profile_view(request):

    form_obj = forms.UserProfileModelForm
    if request.method == 'POST':
        form_obj = forms.UserProfileModelForm(request.POST, request.FILES)
        if form_obj.is_valid():
            var = form_obj.save(commit=False)
            var.save()
            return HttpResponse("Your Model Object is Saved ")
        else:
            return HttpResponse(f'<h1> {form_obj.errors.as_data()} </h1>')

    context = {'my_form': form_obj}
    return render(request, template_name='register/profile.html', context = context)
























def app_fn(request):

    html = '<h1> Welcome to My APP Home Page</h1>'
    return HttpResponse(html)


def dev_fn(request, device, dev_name):
    print('#####################', device)
    return HttpResponse(f"You have Searched For {device} for {dev_name} ")


def demo_fn(request, year, month, pk):
    #print('##########################', type(year), type(month))
    return HttpResponse(f"You have Searched For Year {year} and {month} ")


def register_view(request):

    form_obj = forms.RegisterForm 

    if request.method == 'POST':

        # f_name = request.POST.get('fname')    #request.POST.get(<input field name attr>)
        # l_name = request.POST.get('lname')
        # email = request.POST.get('email')

        form_obj = forms.RegisterForm(request.POST)


        #if form is valid this return True
        if form_obj.is_valid():
            return HttpResponse(f'<h1> Your Data is Submitted </h1>')

        else:
            print(form_obj.errors)

            print('*******************************888', form_obj.errors.as_data())
            return HttpResponse(f'<h1> {form_obj.errors.as_data()} </h1>')

        #print(f_name, l_name, email)
        

    context = {'my_form': form_obj}

    return render(request, template_name='register/sign_up.html', context= context)



