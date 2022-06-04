from django.shortcuts import render

def hello(request):
    content = {'text':'hello'}
    return render(request, 'index.html', content)