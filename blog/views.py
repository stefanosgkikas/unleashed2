from .models import Post
from django.shortcuts import (get_object_or_404, redirect, render)
from django.views.generic import CreateView, ListView, View, YearArchiveView, MonthArchiveView, ArchiveIndexView
from .forms import PostForm
from user.decorators import require_authenticated_permission

#def post_list(request):
#    return render(request,'blog/post_list.html', {'post_list': Post.objects.all()})

class PostArchiveYear(YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True

class PostArchiveMonth(MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'

@require_authenticated_permission('blog.add_post')
class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    #template_name = 'blog/post_form.html'
        
#    def get(self, request):
#        return render(request, self.template_name, {'form': self.form_class()})

#    def post(self, request):
#        bound_form = self.form_class(request.POST)
#        if bound_form.is_valid():
#            new_post = bound_form.save()
#            return redirect(new_post)
#        else:
#            return render(request, self.template_name, {'form': bound_form})


class PostUpdate(View):
    form_class = PostForm
    model = Post
    template_name = 'blog/post_form_update.html'

    def get(self, request, slug):
        post = get_object_or_404(self.model, slug=slug)
        context = {'form': self.form_class(instance=post), 'post': post,}
        return render(request, self.template_name, context)
    
    def post(self, request, slug):
        post = get_object_or_404(self.model, slug=slug)
        bound_form = self.form_class(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {'form': bound_form, 'post': post,}
            return render(request, self.template_name, context)

class PostDelete(View):

    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_confirm_delete.html', {'post': post})
    
    def post(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        post.delete()
        return redirect('blog_post_list')

class PostList(ArchiveIndexView):
    allow_empty = True
    allow_future = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'

#class PostList(ListView):
#    model = Post    
      
#    def get(self, request):
#        post_list = Post.objects.all() 
#        return render(request, 'blog/post_list.html', {'post_list': post_list})
      
#    def post(self, request, slug):
#        post = get_object_or_404(Post, slug__iexact=slug)
#        post.delete()
#        return redirect('blog_post_list')

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request,'blog/post_detail.html', {'post': post})

#def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
    return render(request,'blog/post_detail.html', {'post' : post })
