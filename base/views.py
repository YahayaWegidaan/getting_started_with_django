from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Design with me!'},
    {'id':3, 'name':'Frontends developers!'},
]


def home(request):
    return render(request, 'base/home.html', {'rooms': rooms}) 
    
def room(request, pk):
    return render(request, 'room.html')