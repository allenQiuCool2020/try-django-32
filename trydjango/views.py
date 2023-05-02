from django.http import HttpResponse
import random
from django.template.loader import render_to_string
from articles.models import Article

def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends a request)
    Return HTML as a response ( We pick to return the response )
    """
    print("a",*args, **kwargs)
    random_number = random.randint(1,3)
    article_obj = Article.objects.get(id=random_number)
    article_list = Article.objects.all()
    context = {
        "article_list": article_list,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    
    HTML_STRING = render_to_string("home-view.html", context=context)

    
    return HttpResponse(HTML_STRING)  