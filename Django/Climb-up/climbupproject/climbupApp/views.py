from django.shortcuts import render, HttpResponseRedirect, reverse, redirect, Http404, HttpResponse, get_object_or_404
from django.http import HttpResponse
from .models import Post, City, Comment
from django.http import HttpResponse, JsonResponse
import json
from django.utils.timezone import get_current_timezone
from datetime import datetime
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):# renders the homepage with all posts
    return render(request, 'climbupApp/index.html')


def load_posts(request):# provides the data to be rendered on the home page
    posts = Post.objects.all().order_by('-created_date')# getting posts out of database
    # comments= Post.comments.all()
    post_data = []
    for post in posts: # iterating over post data, converting into dictionaries and returning JSON response
        post_data.append({
            'title': post.title,
            'text': post.text,
            'id': post.id,
            'city_id': post.city.id,
            # 'comments': post.comments,
            'scheduled_date': post.scheduled_date.strftime("%Y-%m-%d @ %H:%M"),
            'liked_by': request.user in post.likes.all(),
            'attendants': [attendee.username for attendee in post.attendees.all()],
            'likes': post.likes.count(),
            'post_image': post.post_image.url,
            'city': post.city.name,
            'author': post.author.username,
            'created_date': post.created_date.strftime('%b %d %Y'),
        })
    return JsonResponse({'posts': post_data,})


def profile_page(request): #page to render 
    return render(request, 'climbupApp/profile_page.html' )


def load_comments(request):
    comments = Comment.objects.all().order_by('-created_on') # getting comments out of the database and ordering by most recent
    comment_data = []
    for comment in comments: # iterating over comment data, converting into dictionaries and returning JSON response 
        comment_data.append({
            'post':comment.post.id,
            'author': comment.author.username,
            'body': comment.body,
            'created_on': comment.created_on.strftime('%b %d %Y'),
        })
    return JsonResponse({'comments': comment_data})


def profile_load(request):
    profile_posts = Post.objects.filter(author=request.user).order_by('-created_date')# getting the data out of the dictionary that matches the requesting user
    profile_data = []
    for post in profile_posts:# iterating over post data, converting into dictionaries and returning JSON response
        profile_data.append({
            'title': post.title,
            'text': post.text,
            'post_image': post.post_image.url,
            'id': post.id,
            'city': post.city.name,
            'author': post.author.username,
            'created_date': post.created_date.strftime('%b %d %Y'),
        })
    return JsonResponse({'profile_posts': profile_data})


def login_page(request):
    if request.method == 'POST': 
        username = request.POST['username']#assigning UN&P to variables 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: #checking the user exists in database.
            login(request, user) # checking credentials against database and logging user in
            messages.success(request, 'login successful')
            return redirect('climbupApp:index')
        else: #displaying error message to the user
            messages.info(request, 'invalid username or password')
    return render(request, 'climbupApp/login_page.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid(): #checking form data,saving to database and informing the user of success
            user = form.save()
            profile_image = form.cleaned_data['image']
            user = authenticate(username=form.cleaned_data['username'], password = form.cleaned_data['password1'])
            messages.success(request, f'Account created for{user.username}')
            login(request, user) # logging user in and redirecting to main page
            return redirect('climbupApp:index')
        else:
            messages.error(request, f'Please try again')
            return render(request, 'climbupApp/register.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'climbupApp/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('climbupApp:index')


def post_new(request):
    city_id = request.POST['city_id'] # assigning data to variables for saving to database from request
    created_date = request.POST['created_date']
    tz = get_current_timezone()
    scheduled_date = request.POST['scheduled_date']
    scheduled_date = tz.localize(datetime.strptime(scheduled_date, "%Y-%m-%dT%H:%M"))
    post = Post(
        title = request.POST['title'],
        text = request.POST['text'],
        post_image = request.FILES['post_image'],
        city = City.objects.get(id=city_id),
        author = request.user,
        scheduled_date = scheduled_date,
    )
    post.save()
    return HttpResponse('saved')


def save_comment(request):
    post_id = request.GET['post_id']
    tz = get_current_timezone()
    comment = Comment(
    post = Post.objects.get(id=post_id),
    body = request.POST['body'],
    author = request.user,
    )
    comment.save()
    return HttpResponse('commented')


def get_cities(request):
    cities = City.objects.all() #getting city data out of database for selects on main page 
    city_data = []
    for city in cities:
        city_data.append({
            'name':city.name,
            'id': city.id,
        })
    return JsonResponse({'cities': city_data})


def add_city(request): # assigning data to variables for saving to database
    city_name = request.POST['city_add']
    city = City(
        name = city_name
    )
    city.save()
    return HttpResponse('city added')


@login_required()
def like_post(request):
    post_id = request.GET['post_id'] #assigning "liked" post to variable
    post = Post.objects.get(id=post_id)
    user = request.user
    liked_by = True
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
        liked_by = False
    else:
        post.likes.add(user)
        liked_by = True
    likes = post.likes.count()
    response = { 'likes': likes, 'liked_by': liked_by}
    return JsonResponse(response)


@login_required()
def attendants(request):
    post_id = request.GET['post_id'] #getting the post object of attended post
    post = Post.objects.get(id=post_id) #getting the post id out
    user = request.user # recording the user id
    if post.attendees.filter(id=user.id).exists(): # checking if the requesting user id exists in the database, if it does we remove the user from attending
        post.attendees.remove(user)
        attended_by = ''
    else:
        post.attendees.add(user) # or if it doesn't exisist we add the user to attending
        attended_by = user.username
    attendees = post.attendees.all() 
    attendee_data = [] # creating a variable of attendees and creating a blank list
    for user in attendees: # iterating through array of attendees, and assigning to the list
        attendee_data.append(user.username)
    response = {'attendees': attendee_data, 'attended_by': attended_by} #assigning data to a dictionary and returning it in the json response.
    return JsonResponse(response)
    

@login_required
def post_edit(request):
    post_id = int(request.POST.get('post_id')) # getting the post id out
    post = Post.objects.get(id=post_id) # using the post id to find the post in the database
    post.city_id = int(request.POST['city_id']) #assigning the id to the to a variable
    post.title = request.POST['title'] # assigning the title to the databse
    post.text = request.POST['text'] # assigning the text data to the to a variable
    post.author = request.user #reassigning the author the to a variable
    post.scheduled_date = request.POST['scheduled_date'] # assigning the scheduled date to the to a variable
    post.save() # resaving the post to the database
    return HttpResponse('edited') # returning a confirmation response
    

@login_required
def delete_post(request):
    delete_post_id = int(request.POST.get('post_id')) # getting the post id out of the response
    post = Post.objects.get(id=delete_post_id) # using the post id to get the post object out of the database
    post.delete() # using the delete function to remove the post
    return HttpResponse('deleted') # returning a confirmation response
