from django.shortcuts import render_to_response

def home(request):
    print 'check'
    return render_to_response('main.html')

