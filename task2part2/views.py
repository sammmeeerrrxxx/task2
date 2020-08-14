from django.shortcuts import render
from .models import UserProfile
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def register(request):
	if request.method == 'GET':
		return render(request, 'task2part2/register.html')

	elif request.method == 'POST':
		mess={"error": "Passwords donot match"}
		if request.POST["password1"] == request.POST["password2"]:
			try: 
				user = User.objects.get(username=request.POST["username"])
				mess={"error": "User already Exists! Try again"}
				return render(request,'task2part2/register.html', context=mess)
			except User.DoesNotExist:
				phoneno = request.POST['phoneno']
				user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['firstname'], last_name=request.POST['lastname'],
						email=request.POST['email'],password=request.POST['password1'])
				newaccount = UserProfile(phoneno=phoneno,user=user)
				newaccount.save()
				login(request,user)
				context={"username":request.POST.get('username')}
				return render(request,"task2part2/success.html",context)

				
 
		return render(request, 'task2part2/register.html',context=mess )



def login1(request):
	if request.method == 'GET':
		return render(request, 'task2part2/login.html')

	elif request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user:
			login(request,user)
			context={"username":username}
			return render(request,"task2part2/success.html",context)

		
		else:
			return render(request,"task2part2/login.html",{'error':'Invalid Credentials'})




def log(request):
    logout(request)
    return render(request,"task2part2/register.html",{"error":"You are succesully logged out! Login/Signup Again."})






