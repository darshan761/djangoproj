from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import user,Item
from django import forms
from django.contrib import messages
from .form import LoginForm
from .form import RegisterForm
# Create your views here.
#def login(request):
#	return render(request,'login.html')


def login(request):
	form = LoginForm()
	form1 = RegisterForm()
		
	return render(request, 'login.html',{'form':form,'form1':form1})

def register(request):
	form = RegisterForm(request.POST)
	form1 = LoginForm()
	form2 = RegisterForm()
	if form.is_valid():
		form.save()
	return HttpResponseRedirect('/bigb/#toregister')

def home(request):
	if request.method=='POST':
		form = LoginForm(request.POST or none)
		if form.is_valid():
			if user.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
				u = user.objects.get(username=request.POST['username'])
				request.session['usid'] = u.id
				context={'user':u}
				return render(request, 'home.html',context)
			else:
				messages.error(request, "Username or Password doesn't Match")
		return HttpResponseRedirect('/bigb/')

def cart(request,userid):
	dict = {'Tomato':'tomato.jpg','Potato':'potato.jpg','Cabbage':'Cabbage.jpg','cauliflower':'cauliflower.jpg','Garlic':'Garlic.jpeg','Onion':'onion.jpg','Coriander':'Coriander.jpg','Lemon':'lemon.jpg','Apple':'apples.jpg','Orange':'orange.jpg','Banana':'banana.jpg','Pomegranate':'Pomegranate.gif' }
	itm = Item.objects.filter(userid_id=userid)
	no = itm.count()
	sum = 0
	for k in itm:
		sum += k.price * k.qty
	return render(request,'cart.html',{'i':itm,'d':dict, 'no':no ,'sum':sum})

def personaldet(request,userid):
	u = user.objects.get(id = userid )
	context={'user':u}
	return render(request,'MyDetails.html',context)

def logout(request):
	return HttpResponseRedirect('/bigb/')

def aboutUs(request):
	return render(request,'AboutUs.html')

def myhome(request):
	return render(request,'home.html')

def update(request):
	if request.method == "POST":
		u = user.objects.filter(id=request.POST['id']).update(name = request.POST['name'] , username = request.POST['username'] ,password = request.POST['password'] ,address = request.POST['address'] ,mobile_no = request.POST['mobile'])
		return HttpResponseRedirect('myhome')
	else:
		return HttpResponseRedirect('/myhome/')

def addtocart(request,userid):
	if request.method == 'POST':
		itm = Item(userid_id=userid,name=request.POST['item_name'],price=request.POST['option'],qty=request.POST['qty'])
		itm.save()
		return HttpResponseRedirect('/bigb/myhome')

def removefromcart(request,itemid):
	itm = Item.objects.filter(id= itemid).delete()
	return HttpResponseRedirect('/bigb/myhome')

