from msilib.schema import ListView

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic import DetailView
from django.views import View

from blogging.models import Post
from django.template import loader


class StubView(View):
    def get(self, request, *args, **kwargs):
        body = "Stub View\n\n"
        if args:
            body += "Args: \n"
            body += "\n".join(["\t%s" % a for a in args])
        if kwargs:
            body += "Kwargs: \n"
            body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
        return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):
    model = Post
    template_name = 'blogging/list.html'

    def get_queryset(self, request, *args, **kwargs):
        published = Post.objects.exclude(published_date__exact=None)
        posts = published.order_by('-published_date')
        context = {'posts': posts}
        return render(request, 'blogging/list.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
