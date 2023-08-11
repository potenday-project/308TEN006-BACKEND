from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import UserCreationMultiForm, ProfileUpdateForm
from django.core.files import File
from urllib.request import urlopen
from django.core.files.temp import NamedTemporaryFile
from django.contrib import messages
from .models import Profile
from urllib.parse import urljoin

## 회원가입 로직
def signup_1(request):
    if request.method == 'POST':
        selected_img = request.POST.get('selected_img')
        return redirect('signup_2', profile_img=selected_img)
    return render(request, 'signup_1.html')

def signup_2(request, profile_img):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        return redirect('signup', profile_img=profile_img, nickname=nickname)
    return render(request, 'signup_2.html', {'profile_img': profile_img})

def signup(request, profile_img, nickname):

    if request.method == 'POST':
        if request.POST['user-password1'] == request.POST['user-password2']:
            form = UserCreationMultiForm(request.POST, request.FILES)
            if form.is_valid(): 
                user = form['user'].save()
                img_url = urljoin("https://atee-s3.s3.ap-northeast-2.amazonaws.com/static/img/", profile_img)

                # 업로드된 이미지의 URL로부터 이미지 파일 가져오기
                response = urlopen(img_url)
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.read())
                img_temp.flush()
                
                profile = form['profile'].save(commit=False)
                profile.user = user

                # 이미지 파일 저장
                profile.profile_image.save(f"profile_{user.id}.png", File(img_temp))
                profile.nick = nickname
                profile.save()
                auth.login(request, user)
                return redirect('index')
            else:
                user = request.POST['user-username']
                user = User.objects.get(username=user)
                messages.info(request, '아이디가 중복됩니다.')
                return render(request, 'signup.html')
        else:
            messages.info(request, '비밀번호가 다릅니다.')
            return render(request, 'signup.html')
    return render(request, 'signup.html', {'profile_img':profile_img, 'nickname': nickname})



class Loginviews(LoginView):
    template_name = 'login.html'
login = Loginviews.as_view()


class LogoutViews(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL
logout = LogoutViews.as_view()


@login_required
def userinfo(request):
    conn_user = request.user
    conn_profile = Profile.objects.get(user=conn_user)

    if not conn_profile.profile_image:
        pic_url = ""
    else:
        pic_url = conn_profile.profile_image.url
            
    context = {
        'id' : conn_user.username,
        'nick' : conn_profile.nick,
        'profile_pic' : pic_url,
        'intro' : conn_profile.intro,
    }

    return render(request, 'mypage.html', context=context)

@login_required
def user_select_info(request, writer):
    select_profile = Profile.objects.get(nick=writer)
    select_user = select_profile.user

    if not select_profile.profile_image:
        pic_url = ""
    else:
        pic_url = select_profile.profile_image.url
            
    context = {
        'id' : select_user.username,
        'nick' : select_profile.nick,
        'profile_pic' : pic_url,
        'intro' : select_profile.intro
    }

    return render(request, 'userpage.html', context=context)

class ProfileUpdateView(View): 
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk) 


        if hasattr(user, 'profile'):  
            profile = user.profile
            profile_form = ProfileUpdateForm(initial={
                'nick': profile.nick,
                'intro': profile.intro,
                'profile_image': profile.profile_image,
            })
        else:
            profile_form = ProfileUpdateForm()

        return render(request, 'profile_update.html', { "profile_form": profile_form})

    def post(self, request):
        u = User.objects.get(id=request.user.pk)       


        if hasattr(u, 'profile'):
            profile = u.profile
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile) 
        else:
            profile_form = ProfileUpdateForm(request.POST, request.FILES)

        # Profile 폼
        if profile_form.is_valid():
            profile = profile_form.save(commit=False) 
            profile.user = u
            profile.save()

            if not profile.profile_image:
                pic_url = ""
            else:
                pic_url = profile.profile_image.url
                    
            context = {
                'id' : u.username,
                'nick' : profile.nick,
                'profile_pic' : pic_url,
                'intro' : profile.intro,
            }

            return render(request, 'mypage.html', context=context)
            
        return redirect('mypage', pk=request.user.pk) 
    