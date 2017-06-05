from django.shortcuts import render_to_response

# Create your views here.

def news_list(request):
    return render_to_response("news/news_list.html")