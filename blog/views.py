from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models as blog_models

# Create your views here.
def index(request):
    template = loader.get_template('blog/index.html')
    context = { 'posts': blog_models.Post.objects.order_by('-pub_date') }
    return HttpResponse(template.render(context, request))


def about(request):
    return render(request, 'blog/about.html', context={'title': 'Blog About'})
