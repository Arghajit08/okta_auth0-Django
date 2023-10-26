from django.shortcuts import render
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout as django_logout
from decouple import config
# Create your views here.
def index(request):
    return render(request,'index1.html')

def profile(request):
    user=request.user
    auth0_user=user.social_auth.get(provider='auth0')
    user_data={
        'user_id':auth0_user.uid,
        'name':auth0_user.firstname,
        'picture':auth0_user.extra_data['picture']   
    }
    context={
        'user_data':json.dumps(user_data,indent=4),
        'auth0_user':auth0_user
    }

    return HttpResponse("Fuck U!!")

def logout(request):
    django_logout(request)
    domain=config('APP_DOMAIN')
    client_id=config('APP_CLIENT_ID')
    return_to='http://127.0.0.1:8000'
    return HttpResponseRedirect(f"https://diabetes-rh73.onrender.com/")
