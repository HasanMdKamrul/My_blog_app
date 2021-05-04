from django.db.models import Count,Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,redirect,reverse
from .models import Post
from marketing.models import Signup
from django.views import generic
from .forms import SigunupModelForm


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get("q")

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)|
            Q(overview__icontains=query)
        ).distinct()

        context = {
            "queryset":queryset,
        }

    return render(request, "search_results.html", context)

def get_catagory_count():
    queryset = Post.objects.values('catagories__title').annotate(Count('catagories__title'))
    return queryset

def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by("-timestamp")[0:3]

    if request.method=="POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        "object_list":featured,
        "latest":latest
    }
    return render(request, "index.html", context)
    


def blog(request):
    catagory_count = get_catagory_count()
    most_recent = Post.objects.order_by("-timestamp")[:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        "catagory_count":catagory_count,
        "queryset":paginated_queryset,
        "page_request_var":page_request_var,
        "most_recent":most_recent
    }
    return render(request, "blog.html" , context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        "post":post,
    }
    return render(request, "post.html", context)


'''
class PostListView(generic.ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "object_list"

    def get_queryset(self):
        featured = Post.objects.filter(featured=True)
        return featured
            
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest = Post.objects.order_by("-timestamp")[0:3]
        context.update(
            {
                "latest":latest
            }
        )
        
        return context        

class SignupCreateView(generic.CreateView):
    model = Signup
    template_name = "posts/test.html"
    form_class = SigunupModelForm

    def get_success_url(self):
        return reverse('posts:index')
'''