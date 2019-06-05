from django.shortcuts import render
from django.http import HttpResponse
from . import quests_scraping
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'scival/about.html')


def contact(request):
    return HttpResponse("We are at contact")


@login_required
def quests(request):
    return render(request, 'scival/quests.html')
# Create your views here.

def crawling_process(request):
    # Get the text
    djtext = request.POST['text']
    print(djtext)
    quests_scraping.main_process()
    # Analyze the text
    return HttpResponse("Crawling Process has been done. Please check your output")
    #pass


