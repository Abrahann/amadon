from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
    print ("")
    return render(request, 'index.html')

def checkout(request):
    request.session['total'] = float(request.POST['quantity_tshirt']) * float(request.POST['price_tshirt']) + float(request.POST['quantity_sweater']) * float(request.POST['price_sweater']) + float(request.POST['quantity_cup']) * float(request.POST['price_cup']) + float(request.POST['quantity_book']) * float(request.POST['price_book'])
    request.session['quantity'] = int(float(request.POST['quantity_tshirt']) + float(request.POST['quantity_sweater']) + float(request.POST['quantity_cup']) + float(request.POST['quantity_book']))
    

    if request.session.get('runningQuantity') == None:
        request.session['runningQuantity'] = 0
    
    request.session['runningQuantity'] = int(float(request.session['runningQuantity']) + (float(request.session['quantity'])))
    
    if request.session.get('runningTotal') == None:
        request.session['runningTotal'] = 0
    
    request.session['runningTotal'] = int(float(request.session['runningTotal']) + (float(request.session['total'])))

    return redirect('/process') 

def process(request):
    context={
        'total':request.session['total'],
        'amount':request.session['runningQuantity'],
        'Spend':request.session['runningTotal']
    }
    return render(request,'show.html', context)


def reset(request):
     
    request.session.clear()

    return redirect('/buy')
    
