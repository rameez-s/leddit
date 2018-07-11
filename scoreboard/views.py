# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect as rd
from django.http import HttpResponse, HttpResponseRedirect
from .models import User

import urllib
import json

# Create your views here.

client_id = CLIENTID                                                    # Provided by LinkedIn API
client_secret = CLIENTSECRET                                            # Provided by LinkedIn API
redirect = "http://localhost:8000/score/getAuth/"
auth = ""
tok = ""

def index(request):
    return render(request, 'scoreboard/index.html')                             # Render landing page

def getAuth(request, *args, **kwargs):
    global auth
    a = dict(request.GET.iterlists())                                           # Parse HTTP response as dictionary
    if "code" in a.keys():                                                      # if authentication worked
        auth = str(a['code'][0])                                                # get authorization code
        params = {
                      'grant_type': 'authorization_code',
                      'code': auth,
                      'redirect_uri': redirect,
                      'client_id': client_id,
                      'client_secret': client_secret,
        }
        params = urllib.urlencode(params)
        info = urllib.urlopen("https://www.linkedin.com/uas/oauth2/accessToken", params)    # POST request for access token
        tok = json.load(info)['access_token']
        data = urllib.urlopen("https://api.linkedin.com/v1/people/~:(id,first-name,last-name,headline,public-profile-url,picture-url)?oauth2_access_token="+tok+"&format=json")
        # get request for user data
        data = json.load(data)
        try:                                                                    # Check to see if user already in database
            User.objects.get(id_num = data["id"])
        except User.DoesNotExist:                                               # If new user
            u = User(id_num = data["id"], name = data["firstName"] + " " + data["lastName"])
            if("headline" in data.keys()):
                u.headline = data["headline"]                                   # Get as much public data, the user's permission's allow
            if("publicProfileUrl" in data.keys()):
                u.profile = data["publicProfileUrl"]
            if("pictureUrl" in data.keys()):
                u.dp = data["pictureUrl"]
            u.save()
        return HttpResponseRedirect("/score/main/")
    else:
        # print "Second HIT"
        return render(request, 'scoreboard/index.html')                         # If authentication failed return back to landing page

def main(request):
    userList = User.objects.order_by('-pub_date')[:10]                          # Generate 10 most recent users
    context = {'user_list': userList}
    return render(request, 'scoreboard/main.html', context)

def upvote(request, id):
    u = User.objects.get(id_num = id)
    u.score += 1                                                                # increment user's score in database
    u.save()
    return HttpResponseRedirect("/score/main/")

def downvote(request, id):
    u = User.objects.get(id_num = id)
    u.score -= 1                                                                # decrement user's score in database
    u.save()
    return HttpResponseRedirect("/score/main/")
