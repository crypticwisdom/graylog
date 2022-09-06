from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    request.graylog["user"] = request.user.user_name
    request.graylog.info("Rendered homepage for {user}", user=request.user.user_name)
    print(request.graylog)
    return HttpResponse("Hello")