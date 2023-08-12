from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import PostForm
from django.contrib import messages
from .models import Memos, Comment, Tag
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
import re

def splash(request):
    return render(request, 'splash.html')

def category(request, category_name=None):
    if category_name == "전체":
        memo = Memos.objects.all()
    else:
        memo = Memos.objects.filter(category=category_name)

    # 해당 카테고리에 속한 메모들의 태그들 가져오기
    related_tags = Tag.objects.filter(memos__category=category_name).distinct()

    return render(request, 'category.html', {'memo': memo, 'related_tags': related_tags, 'category_name': category_name})

def index(request, tag=None):
    if tag:
        memo = Memos.objects.filter(tag_set__tag_name=tag)
    else:
        memo = Memos.objects.all()
    return render(request, 'index.html', {'memo': memo})

def post(request):
    print(request.POST)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid(): 
            post = form.save(commit=False)
            post.name = User.objects.get(username=request.user.get_username())
            post.images = request.FILES.get('images')  # KeyError를 피하기 위해 get()을 사용합니다
            post.generate()
            post.tag_save()
            post.save()
            return redirect('index')
        else:
            print(form.errors)  # 폼의 오류 메시지 출력
            return HttpResponse("폼이 유효하지 않습니다")
    else:
        form = PostForm() 
        return render(request, 'post.html', {'form': form})
    
def detail(request, memo_id):
    memo = get_object_or_404(Memos, pk=memo_id)
    conn_profile = Profile.objects.get(user=memo.name)
    
    tag_text = memo.tag_text
    tags_with_hashes = re.findall(r'#\w+', tag_text)
    tag_all = [tag for tag in tags_with_hashes]
    
    return render(request, 'detail.html', {'memo': memo, 'conn_profile': conn_profile, 'tag_all': tag_all})

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
    if request.method == 'POST':
        post = get_object_or_404(Memos, pk=memokey)

        context = {'post': post,}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = Profile.objects.get(user=conn_user)

        if not content:
            messages.info(request, '댓글을 입력해 주세요')
            return redirect('detail', memokey)

        comment = Comment.objects.create(post=post, comment_writer=conn_profile, comment_contents=content)

        # 새로운 댓글 인스턴스가 생성된 후 해당 댓글 작성자의 프로필 이미지를 comment_writer_img에 저장
        comment.comment_writer_img = conn_profile.profile_image
        comment.save()

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