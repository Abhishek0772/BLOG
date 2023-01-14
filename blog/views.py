from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
# Create your views here.
def home(request):
    data = Post.objects.all().values()
    # template = loader.get_template("index.html")
    print(f'hello my name is {data}')
   
    return render(request,'index.html',{"data":data})

# %