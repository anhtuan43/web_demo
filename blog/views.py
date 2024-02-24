from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import postForm
# Create your views here.

def blog(request):
    pF = postForm.objects.all()
    paginator = Paginator(pF, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    num_page = range(1, page_obj.paginator.num_pages + 1)
    return render(request, "blog/blog.html", {"page_obj": page_obj, "num_page":num_page})

def postDetail(request, id):
    pD = postForm.objects.get(id = id)
    return render(request, "blog/post_detail.html", {"pD":pD})
