from django.shortcuts import render, redirect
from .models import Entry
from .forms import Post
from datetime import datetime

def entries(request):
    entries = Entry.objects.all()
    return render(request, 'entries.html', {'entries':entries})

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
    entry = Entry.objects.get(id=entry_id)
    return render(request, 'entry_detail.html', {'entry':entry})

def comment(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    comment = entry.comment_set.create(
        name = request.POST['name'],
        comment = request.POST['comment'],
        pub_date = timezone.now()
    )

def upvote(request, entry_id):
    return cast_vote(request, entry_id, +1)

def downvote(request, entry_id):
    return cast_vote(request, entry_id, -1)

def cast_vote(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    entry.votes += score
    entry.save()
    
    return redirect('home')