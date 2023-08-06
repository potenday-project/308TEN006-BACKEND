from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import PostForm
from django.contrib import messages
from .models import Memos, Comment, Tag, Tag2
from member.models import Profile
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.db.models import Q

def index(request, tag=None, tag2=None):
    memo = Memos.objects.all()
    return render(request, 'index.html', {'memo': memo})

def post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid(): 
            post = form.save(commit = False)
            post.name = User.objects.get(username = request.user.get_username())
            post.generate()
            post.tag_save()
            post.tag_save2()
            post.save()
            return redirect('index')
    else:
        form = PostForm() 
        return render(request, 'post.html', {'form' : form})

def detail(request, memo_id):
    memo = get_object_or_404(Memos, pk=memo_id)
    return render(request, 'detail.html', {'memo': memo})

@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user 
        memo_id = request.POST.get('pk', None)
        memo = Memos.objects.get(pk = memo_id)

        if memo.likes.filter(id = user.id).exists():
            memo.likes.remove(user) 
            message = '좋아요 취소'
        else:
            memo.likes.add(user)
            message = '좋아요!'

    context = {'likes_count' : memo.total_likes, 'message' : message}
    return HttpResponse(json.dumps(context), content_type='application/json')

@login_required
def comment_write(request, memokey):
    if request.method =='POST':
        post = get_object_or_404(Memos, pk=memokey)

        context = {'post': post,}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = Profile.objects.get(user=conn_user)

        if not content:
            messages.info(request, '댓글을 입력해 주세요')
            return redirect('detail', memokey)

        Comment.objects.create(post=post, comment_writer=conn_profile, comment_contents=content)
        return redirect('detail', memokey)

@login_required
def comment_delete(request, memo_pk, pk):
    post = get_object_or_404(Memos, pk=memo_pk)
    comment = get_object_or_404(Comment, pk=pk)
        
    context = {'post': post,}
    content = request.POST.get('content')

    conn_user = request.user
    conn_profile = Profile.objects.get(user=conn_user)


    if conn_profile == comment.comment_writer:
        comment.delete()
        return redirect('detail', memo_pk)
    else:
        return render(request, 'warning.html')