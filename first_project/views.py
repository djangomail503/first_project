
from django.http import HttpResponse

from django.shortcuts import render

def index_fn(request):

    html = "<h1> Welcome to My Home Page </h1>"

    #return HttpResponse(html)

    qty = 2
    prc = 10
    result = qty*prc

    discount = 20

    fruits =['Apple', 'Banana', 'Mango']

    dct = {  'price': result,   'dsct': discount,  'fruits': fruits}

    return render(request, template_name='index.html', context=dct)



#-------------------------------------------------------------------------------
def next_fn(request):

    html = "<h1> Welcome to my Next Page </h1>"

    return HttpResponse(html)

def base_fn(request):

    return render(request, template_name='base/base.html')



