from django.shortcuts import render
from blog.models import Post

posts = [
    {
        'author' : 'GM Ariful Islam',
        'title' : 'Arifs Post 1',
        'content' : 'Arifs Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted' : 'January 15,2019'
    },
    {
        'author' : 'Kishwara Sara',
        'title' : 'Saras Post 1',
        'content' : 'Saras Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted' : 'March 8,2019'
    }
]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

# def login(request):
#     return render(request, 'blog/login.html')
#
# def register(request):
#     return render(request, 'blog/register.html')
