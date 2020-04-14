from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def statistics(request):
    return render(request, "statistics.html")


def prevention(request):
    return render(request, 'prevention.html')


def symptoms(request):
    return render(request, 'symptoms.html')


def faq(request):
    return render(request, 'faq.html')


def map_stats(request):
    return render(request, 'india_map.html')


def prediction(request):
    return render(request, 'prediction.html')

def about(request):
    return render(request, 'about.html')        
