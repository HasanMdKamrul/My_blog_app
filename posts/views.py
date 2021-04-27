from django.shortcuts import render
from .models import Post
from marketing.models import Signup
from django.views import generic




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
    


def blog(request):
    return render(request, "blog.html")

def post(request):
    return render(request, "post.html")




'''
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
    '''


