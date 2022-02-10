from django.shortcuts import render

# Create your views here.
def main_ind(request) :

    return render(request, 'main/index.html')