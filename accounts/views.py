
from django.contrib.auth import login
from accounts.forms import SignupForm
from django.shortcuts import render, redirect
# from django.http import JsonResponse

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # 회원가입 완료

            id = form.cleaned_data.get('id')
            username = form.cleaned_data.get('username')
            birth = form.cleaned_data.get('birth')
            tel = form.cleaned_data.get('tel')

            login(request, user)  # 회원가입과 동시에 로그인
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
