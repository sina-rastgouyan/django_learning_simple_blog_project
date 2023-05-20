from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


# Create your views here.
class PostListView(generic.ListView):
    template_name = 'blog/blog_home.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.filter(status='pub')
    
# def blog_home_view(request):
#     all_posts = Post.objects.filter(status='pub')
#     context = {
#         'post_list': all_posts
#     }
#     return render(request, 'blog/blog_home.html', context)

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     context = {
#         'post' : post
#     }

#     return render(request, 'blog/post_detail.html', context)
    
class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/new_post.html'

# def new_post_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = PostForm()
#             return redirect('blog_home')
#     else:
#         form = PostForm()

#     context = {
#         'form': form
#     }

#     return render(request, 'blog/new_post.html', context)

class PostUpdateView(generic.UpdateView):
    model= Post
    form_class = PostForm
    template_name = 'blog/update_post.html'

# def edit_post_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)

#     if form.is_valid():
#         form.save()
#         return redirect('blog_home')
#     else:
#         form = PostForm(instance=post)
    
#     context = {
#         'form': form
#     }

#     return render(request, 'blog/update_post.html', context)
    
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post_ensurement.html'
    success_url = reverse_lazy('blog_home')

# def delete_post_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     if request.method == 'POST':
#         post.delete()
#         return redirect('blog_home')
    
    
#     return render(request, 'blog/delete_post_ensurement.html')
