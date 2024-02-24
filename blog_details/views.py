from django.shortcuts import render

# Create your views here.
def postDetail(request):
    return render(request, "blog_details/postDetail.html")