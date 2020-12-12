from django.shortcuts import render


def homepage(request):
    return render(request, 'travelers_best_friend_app/homepage.html')
