from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.

	#item = ls.item_set.get(id=1)
	#ls = TodoList.objects.get(name=name)
	#item = ls.item_set.get(id=3)
	#return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))

#def index(response, id):
#	return HttpResponse("<h1>%s</h1>" % id)

#def index(response, id):
#	ls = TodoList.objects.get(id=id)
#	return HttpResponse("<h1>%s</h1>" % ls.name)

#def index(response, name):
#	ls = TodoList.objects.get(name=name)
#	item = ls.item_set.get(id=1)
#	return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))

def index(response, id):
	ls = TodoList.objects.get(id=id)
	return render(response, "main/list.html", {"ls":ls})

def home(response):
	return render(response, "main/home.html", {})