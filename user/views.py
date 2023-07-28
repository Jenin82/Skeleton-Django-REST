from django.shortcuts import render

# Create your views here.
def homePage(request):
    context = {'todo': todo}
    return render(request, 'user/home.html', context)