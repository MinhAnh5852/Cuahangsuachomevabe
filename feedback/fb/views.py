from django.shortcuts import render

# Create your views here.
def get_feedback(request):
    return render(request, 'feedback.html')
