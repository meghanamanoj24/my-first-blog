from django.shortcuts import render

def home(request):
    return render(request, 'blog/post_list.html')  # Replace with your template
