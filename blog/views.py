from django.shortcuts import render

post = [
    {
        'author': 'Avi',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '17 April 2023'
    },
    {
        'author': 'Athi',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '18 April 2023'
    }
]

def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})