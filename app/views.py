from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Story, Posts
from django.contrib.auth.models import User

# Create your views here.

# POSTS 


# Create post

# Read Posts
def posts(request):
    posts = Posts.objects.all()
    # print(request.user.username)
    return render(request, 'app/index.html', {'posts':posts})

# Update Post 

# Delete post 
 
# Fetch user posts
def user_posts(request):
    posts = Posts.objects.filter(user=request.user)
    return render(request, 'app/user_posts.html', {'posts':posts})


def users_posts(request, username):
    user = User.objects.get(username=username)
    posts = user.posts_set.all()

    return render(request, 'app/users_posts.html', {'user':user, 'posts':posts})

# STORIES



# Create story

def create_story(request):
    if request.method == 'POST':
        image = request.POST.get('image')
        if image:
            expiration_timestamp = timezone.now() + timezone.timedelta(hours=24)
            content = request.POST.get('content')
            story = Story.objects.create(user=request.user, image=image, content=content, expiration_timestamp=expiration_timestamp)
            return redirect('view_stories')
        else:
            # Handle error when content is empty 
            pass
    return render(request, 'create_story.html', {'story':story})
    

# Read Stories

# Update Story 

# Delete Story 
