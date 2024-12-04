from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView,DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from users.models import Profile
from django.shortcuts import get_object_or_404


# Create your views here.

from django.shortcuts import render
from .models import Post

class PostListView(LoginRequiredMixin, ListView):
    template_name = "templates/post_list.html"
    model = Post
    context_object_name = "posts"

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post_form.html"
    model = Post
    
    form_class = PostForm
    success_url= reverse_lazy('post-list')
    
    def form_valid(self, form):
        # Obtém o Profile do usuário logado
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.profile = profile  # Associa o Profile ao novo Post
        return super().form_valid(form)
    
def tipos_ocorrencias(request):
    return render(request, 'descricao.html')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "post_confirm_delete.html"
    model = Post
    context_object_name = "post"
    success_url=reverse_lazy("post-list")

    def get_queryset(self):
        profile = self.request.user.profile
        return Post.objects.filter(profile=profile)



"""

def post_list(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

    """