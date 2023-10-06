from django.http.response import HttpResponse
from .models import Tag, Startup, NewsLink
from django.template import Context, loader
from django.shortcuts import (get_object_or_404, redirect, render)
from .forms import TagForm, StartupForm, NewsLinkForm
from django.views.generic import DetailView, CreateView, DeleteView, View
from .utils import UpdateView
#from .utils import ObjectUpdateMixin, ObjectDeleteMixin
from django.urls import reverse_lazy, reverse
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from user.decorators import (require_authenticated_permission, class_login_required)



# η tag list με class based view
class TagList(View):
   template_name = 'organizer/tag_list.html'

   def get(self, request):
      tags = Tag.objects.all()
      context = {'tag_list': tags}
      return render(request, self.template_name, context)

# η tag list με function view
#def tag_list(request):
#    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})

class TagPageList(View):
    paginate_by = 5
    template_name = 'organizer/tag_list.html'

    def get(self, request, page_number):
        tags = Tag.objects.all()
        paginator = Paginator(tags, self.paginate_by)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        if page.has_previous():
            prev_url = reverse('organizer_tag_page', args=(page.previous_page_number()))
        else:
            prev_url = None
        if page.has_next():
            next_url = reverse('organizer_tag_page', args=(page.next_page_number()))
        else:
            next_url = None
        context = {
                        'is_paginated': page.has_other_pages(),
                        'next_page_url': next_url,
                        'paginator': paginator,
                        'previous_page_url': prev_url,
                        'tag_list': page,
                    }
        return render(request, self.template_name, context)

class TagDetail(DetailView):
    context_object_name = 'tag'
    model = Tag
    template_name = ('organizer/tag_detail.html')

# η tag detail view σε class based view
#class TagDetail(View):

 #   def get(self, request, slug):
  #      tag = get_object_or_404(Tag, slug__iexact=slug)
   #     return render(request, 'organizer/tag_detail.html', {'tag': tag})

# η tag detail view με function view
#def tag_detail(request, slug):
#   	 return render(request, 'organizer/tag_detail.html', {'tag': get_object_or_404(Tag, slug=slug)})

# def tag_create(request):
#    if request.method == 'POST':
#        form = TagForm(request.POST)
#           if form.is_valid():
#               new_tag = form.save()
#               return redirect(new_tag)
#           else: # empty data or invalid data
#               return render(request, 'organizer/tag_form.html', {'form': form})
#     else: # request.method != 'POST'
#           form = TagForm()
#           return render(request, 'organizer/tag_form.html', {'form': form})    

@require_authenticated_permission('organizer.add_tag')
class TagCreate(CreateView):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


class StartupCreate(CreateView):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'


class NewsLinkCreate(CreateView):
        form_class = NewsLinkForm
        template_name = 'organizer/newslink_form.html'

@require_authenticated_permission('organizer.change_startup')
class StartupUpdate(UpdateView):
    form_class = StartupForm
    model = Startup
    
@require_authenticated_permission('organizer.change_tag')
class TagUpdate(UpdateView):
    form_class = TagForm
    model = Tag
    

class NewsLinkUpdate(UpdateView):
    form_class = NewsLinkForm
    model = NewsLink
      


#class NewsLinkUpdate(View):
#       template_name = ('organizer/newslink_form_update.html')

#        def get(self, request, pk):
#            newslink = get_object_or_404(NewsLink, pk=pk)
#            context = {'form': self.form_class(instance=newslink), 'newslink': newslink,}
#            return render(request, self.template_name, context)
        
#        def post(self, request, pk):
#            newslink = get_object_or_404(NewsLink, pk=pk)
#            bound_form = self.form_class(request.POST, instance=newslink)
#            if bound_form.is_valid():
#                new_newslink = bound_form.save()
#                return redirect(new_newslink)
#            else:
#                context = {'form': bound_form, 'newslink': newslink,}
#                return render(request, self.template_name, context)                   

#class NewsLinkDelete(View):

#    def get(self, request, pk):
#        newslink = get_object_or_404(NewsLink, pk=pk)
#        return render(request, 'organizer/newslink_confirm_delete.html', {'newslink': newslink})
    
#    def post(self, request, pk):
#        newslink = get_object_or_404(NewsLink, pk=pk)
#        startup = newslink.startup
#        newslink.delete()
#        return redirect(startup)

class NewsLinkDelete(DeleteView):
    model = NewsLink

    def get_success_url(self):
        return (self.object.startup.get_absolute_url())

class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list') # μόλις σβηστεί κάνει redirect στην tag_list url
    template_name = ('organizer/tag_confirm_delete.html') 

class StartupDelete(DeleteView):
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')
    template_name = ('organizer/startup_confirm_delete.html')       


# H startp list με classed based view
class StartupList(View):
    page_kwarg = 'page'
    paginate_by = 5 # 5 items per page
    template_name = 'organizer/startup_list.html'

    def get(self, request):
        startups = Startup.objects.all()
        paginator = Paginator(startups, self.paginate_by)
        page_number = request.GET.get(self.page_kwarg)
        #page = paginator.page(page_number)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(pkw=self.page_kwarg, n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(pkw=self.page_kwarg, n=page.next_page_number())
        else:
            next_url = None    
        context = {'is_paginated': page.has_other_pages(), 'next_page_url': next_url, 'paginator': paginator, 'previous_page_url': prev_url, 'startup_list': page}
        #context = {'is_paginated': page.has_other_pages(), 'paginator': paginator, 'startup_list': page}
        return render(request, self.template_name, context)

# Η startup list με function view
#def startup_list(request):
#     return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()}) 

#η startup detail view με class based view
#class StartupDetail(View):
#
#   def get(self, request, slug):
#        startup = get_object_or_404(Startup, slug__iexact=slug)
#        return render(request, 'organizer/startup_detail.html', {'startup': startup})

# η startup detail view με function view
#def startup_detail(request, slug):
 #   startup = get_object_or_404(Startup, slug=slug)
  #  return render(request,'organizer/startup_detail.html',{'startup': startup})
    # return render(request, 'organizer/startup_detail.html', {'startup': get_object_or_404(Startup, slug=slug)})  

class StartupDetail(DetailView):
    context_object_name = 'startup'
    model = Startup
    template_name = ('organizer/startup_detail.html')