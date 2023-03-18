from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from .models import User
# Create your views here.


def login_view(request):
    msg = "_"
    if request.method == "POST":
#        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            print("인증성공")
            msg = "로그인성공"
            login(request, user)
        else:
            print("인증실패")
            messages.info(request, "입력이 잘못되었습니다.")
            msg = "입력실패"
            
    return render(request, "users/login2.html",{'msg':msg})#20230312김정현

def logout_view(request):
    logout(request)
    return redirect("user:login")

def signup_view(request):
    msg = "_"
    if request.method == "POST":
        username =request.POST["username"]
        password =request.POST["password"]
        firstname =request.POST["firstname"]
        lastname =request.POST["lastname"]
        email =request.POST["email"]
        student_id =request.POST["student_id"]

        if len(username)*len(password)*len(firstname)*len(lastname)*len(email)*len(student_id) != 0: 
            print(request.POST)
            user = User.objects.create_user(username, email, password)
            user.last_name = lastname
            user.first_name = firstname
            user.student_id = student_id
            user.save()
            return redirect("user:login")
        else:
            print("빈칸오류")
            msg = "빈칸을 모두 채워주세요"
            # messages.info(request, "빈칸을 모두 채워주세요")
    return render(request, "users/signup.html",{'msg':msg})

def GetNagoya(request):
    return render(request, "users/Nagoya.html")
def GetTakayama(request):
    return render(request, "users/Takayama.html")
def GetToyama(request):
    return render(request, "users/Toyama.html")
def GetGero(request):
    return render(request, "users/Gero.html")
def GetBacktoLogin():
    return redirect("user:login")