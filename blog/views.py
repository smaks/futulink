from .models import Post, Category, Tag, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django import forms


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
    def get_queryset(self):
        return Post.objects

class CategoryView(generic.DetailView):
    template_name = 'blog/category.html'
    model = Category
    def get_queryset(self):
        return Category.objects

class TagView(generic.DetailView):
    template_name = 'blog/tag.html'
    model = Tag
    def get_queryset(self):
        return Tag.objects

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        slug=request.POST.get('slug','')
        tags = request.POST.getlist('tags','')
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

              
            #post.published_date = timezone.now()
            post.save()
            for tag in tags:
                post.tags.add(tag)
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def detail(request):
    post = PostView(request)
    return post.as_view()

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('posted')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect(post)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:blog')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=comment.post.pk)
    comment.approve()
    return redirect(post)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=comment.post.pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect(post)




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

