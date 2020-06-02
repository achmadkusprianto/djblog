from django.shortcuts import render, get_object_or_404
# harus login untuk membuat newpost, update, delete
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# CRUD django utk post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# untuk tampilan home, urutan post,dsb
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-tanggal_post']
    paginate_by = 5

# setting pengarang link di home
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(pengarang=user).order_by('-tanggal_post')

# untuk detail view (klik judul diarahkan ke link khusus post tersebut)
class PostDetailView(DetailView):
    model = Post

# untuk create post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['judul', 'konten']


    def form_valid(self, form):
        form.instance.pengarang = self.request.user
        return super().form_valid(form)

# untuk update post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['judul', 'konten']


    def form_valid(self, form):
        form.instance.pengarang = self.request.user
        return super().form_valid(form)

    # cek apakah current user adalah pengarang (supaya pengarang yg post saja yg bisa update)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.pengarang:
            return True
        return False

# untuk delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.pengarang:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'judul': 'About'})
