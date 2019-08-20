# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#import MySQLdb
import time
#import urllib
import urllib.parse
import base64
import subprocess
import json

import logging

logger = logging.getLogger("django.request")

def home(request):
    login_url = "https://login.sogou-inc.com/?appid=1544&sso_redirect=http://selftesting.web.sjs.ted/&targetUrl="
    ptoken = ""
    try:
        ptoken = request.GET['ptoken']
    except:
        pass
    if ('uid' not in request.COOKIES and ptoken is ""):
        print ("no login and not login")
        return HttpResponseRedirect(login_url)
    if (ptoken != ""):#login request callback
        message = urllib.parse.unquote(ptoken)
        child = subprocess.Popen(['/bin/php', '/search/odin/daemon/self_testing/Django/Self_Testing/rsa_decode.php', message], shell = False, stdout = subprocess.PIPE)
        child.wait()
        user = child.stdout.read().decode('utf-8')
        try:
            json_data = json.loads(user)
            uid = json_data['uid']
            login_time = int(json_data['ts'])/1000 #s
        except:
            uid = ""
            login_time = 0
        now_time = time.time()
        if (uid != "" and now_time - login_time < 60):
            response = render(request, 'home/home.html', {'uid': uid})
            if ('uid' not in request.COOKIES):
                response.set_cookie("uid", uid)
        else:
            print ("maybe uid[%s] is empty or now_time[%d] - login_time[%d] >= 60" % (uid, now_time, login_time))
            response = None
    elif ('uid' in request.COOKIES):#already login
        try:
            uid = request.COOKIES['uid']
        except:
            print ("should be login, but not login")
            uid = ""
        if (uid != ""):
            response = render(request, 'home/home.html', {'uid': uid})
        else:
            response = None
    if (response == None):
        print ("response is none")
        return HttpResponseRedirect(login_url)
    return response

def logout(request):
    response = HttpResponseRedirect('https://login.sogou-inc.com/logout.jsp?appid=1544&sso_redirect=http://selftesting.web.sjs.ted&targetUrl=')
    if ('uid' in request.COOKIES):
        response.delete_cookie("uid")
    return response
