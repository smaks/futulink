from .models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

class BlogIndex(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'  
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.order_by('-posted')[:5]

class PostView(generic.DetailView):
    template_name = 'blog/post.html'
    model = Post
    #def get_queryset(self):
    #    return Blog.objects.filter(posted__lte=timezone.now())

class CategoryView(generic.DetailView):
    template_name = 'blog/category.html'
    model = Category
    def get_queryset(self):
        return Category.objects

#def blog(request):
#    latest_post_list = Question.objects.order_by('-posted')[:5]
#    context = {'latest_post_list': latest_post_list}
#    return render(request, 'blog/index.html', context)

#def view_post(request, slug):
#    current_post = get_object_or_404(Blog, slug=slug)
#    context = {'current_post': current_post}
    #return render(request, 'blog/post.html', context)

#def view_category(request, slug):
#    category = get_object_or_404(Category, slug=slug)
#    context = {'category':category}
#    return render(request, 'blog/category.html', context)
