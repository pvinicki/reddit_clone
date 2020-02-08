from django.shortcuts import render, redirect
from .models import Entry
from .models import Comment
from .forms import Post
from datetime import datetime
from django.contrib.auth.decorators import login_required

def entries(request):
    entries = Entry.objects.all()
    return render(request, 'entries.html', {'entries':entries})
    
@login_required(login_url="accounts:login:view")
def make_entry(request):
    if request.method == "POST":
        post = Entry()
        post.text = request.POST['text']
        post.title = request.POST['title']
        post.pub_date = datetime.now()
        post.save()

        return redirect('home')

    form = Post()
    return render(request, 'post.html', {'form':form})

def entry_detail(request, entry_id):
    form = Post()
    entry = Entry.objects.get(id = entry_id)
    comments = Comment.objects.filter(entry = entry_id)
    return render(request, 'entry_detail.html', {'entry':entry, 'comments':comments, 'form': form})

@login_required(login_url="accounts:login_view")
def make_comment(request, entry_id):
    if request.method == "POST":
        entry = Entry.objects.filter(id = entry_id)
        comment = Comment()
        if request.user.is_authenticated:
            comment.name = request.user.username
        comment.entry = entry[0]
        comment.text = request.POST['text']
        comment.pub_date = datetime.now()
        comment.save()

    return redirect(request, 'home')

def upvote(request, entry_id):
    return cast_vote(request, entry_id, +1)

def downvote(request, entry_id):
    return cast_vote(request, entry_id, -1)

def cast_vote(request, entry_id, score):
    entry = Entry.objects.filter(id = entry_id)
    entry = entry[0]
    entry.votes += score
    entry.save()
    
    return redirect('home')

    