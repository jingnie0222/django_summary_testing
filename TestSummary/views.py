# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from TestSummary.models import TestSummary
from TestSummary.models import SummaryDiff
from .forms import summary_form


import time
#import MySQLdb
import pymysql
import logging
from utils import mydifflib


logger = logging.getLogger("django.request")

# def index(request):
    # login_url = "https://login.sogou-inc.com/?appid=1544&sso_redirect=http://selftesting.web.sjs.ted/&targetUrl="
    # ptoken = ""
    # try:
        # ptoken = request.GET['ptoken']
    # except:
        # pass
    # if ('uid' not in request.COOKIES and ptoken is ""):
        # print ("no login and not login")
        # return HttpResponseRedirect(login_url)
    # if (ptoken != ""):#login request callback
        # message = urllib.parse.unquote(ptoken)
        # child = subprocess.Popen(['/bin/php', '/search/odin/daemon/self_testing/Django/Self_Testing/rsa_decode.php', message], shell = False, stdout = subprocess.PIPE)
        # child.wait()
        # user = child.stdout.read().decode('utf-8')
        # try:
            # json_data = json.loads(user)
            # uid = json_data['uid']
            # login_time = int(json_data['ts'])/1000 #s
        # except:
            # uid = ""
            # login_time = 0
        # now_time = time.time()
        # if (uid != "" and now_time - login_time < 60):
            # response = render(request, 'TestSummary/index.html', {'uid': uid})
            # if ('uid' not in request.COOKIES):
                # response.set_cookie("uid", uid)
        # else:
            # print ("maybe uid[%s] is empty or now_time[%d] - login_time[%d] >= 60" % (uid, now_time, login_time))
            # response = None
    # elif ('uid' in request.COOKIES):#already login
        # try:
            # uid = request.COOKIES['uid']
        # except:
            # print ("should be login, but not login")
            # uid = ""
        # if (uid != ""):
            # response = render(request, 'TestSummary/index.html', {'uid': uid})
        # else:
            # response = None
    # if (response == None):
        # print ("response is none")
        # return HttpResponseRedirect(login_url)
    # return response
    
    
    
def index(request):
    response = render(request, 'TestSummary/index.html')
    return response

'''
def add(request):
    # login_url = "https://login.sogou-inc.com/?appid=1544&sso_redirect=http://selftest.web.sjs.ted/&targetUrl="
    # try:
        # user = request.COOKIES['uid']
    # except:
        # return HttpResponseRedirect(login_url)

    test_svn = str_dos2unix(request.POST['test_svn'])
    base_svn = str_dos2unix(request.POST['base_svn'])
    newconfip = str_dos2unix(request.POST['newconfip'])
    newconfuser = str_dos2unix(request.POST['newconfuser'])
    newconfpassw = str_dos2unix(request.POST['newconfpassw'])
    newconfpath = str_dos2unix(request.POST['newconfpath'])
    newdataip = str_dos2unix(request.POST['newdataip'])
    newdatauser = str_dos2unix(request.POST['newdatauser'])
    newdatapassw = str_dos2unix(request.POST['newdatapassw'])
    newdatapath = str_dos2unix(request.POST['newdatapath'])

    testitem = 0
    print ("aaa")
   
    pvscheck = 0
    dmfgl = 0
    performance = 0

 
    try:
        pvscheck = str_dos2unix(request.POST['pvscheck'])
        print ("pvscheck: ", pvscheck)
        logger.debug("pvscheck: %s" %pvscheck)
        testitem += int(pvscheck)*1000
    except:
        pass
    try:
        dmfgl = str_dos2unix(request.POST['dmfgl'])
        print ("dmfgl: ", dmfgl)
        testitem += int(dmfgl)*100
    except:
        pass
    try:
        performance = str_dos2unix(request.POST['performance'])
        print ("performance: ", performance)
        testitem += int(performance)*10
    except:
        pass

    print ("testitem: ", testitem)
    remarks = str_dos2unix_space(request.POST['remarks'])

   
    data = testcache.objects.create(create_time=get_now_time(), user=user, testitem=int(testitem), testsvn=test_svn, basesvn=base_svn, newconfip=newconfip, newconfuser=newconfuser, newconfpassw=newconfpassw, newconfpath=newconfpath, newdataip=newdataip, newdatauser=newdatauser, newdatapassw=newdatapassw, newdatapath=newdatapath, remarks=remarks)

 

    task_id = data.id
    print ('task_id: ', task_id)

    database_host="datatest01.web.sjs.ted"
    database_data="static_check_history"
    database_user="root"
    database_pass=""

    svn_key = 'uYSlU9TFCCkk7mqxrmZi5TxKkiEZqjYPiZN2mhXe'
    orxstr = stringxor('New$oGou4U!', svn_key)
    print ("whatwhatwhat")
    try:
        if int(pvscheck) == 1:
            print  ("herehere")
            db = pymysql.connect(database_host,database_user,database_pass,database_data, charset="utf8")
            cursor = db.cursor()


            print  ("herehere2")
            if int(dmfgl) == 0 and int(performance) == 0:
                need_update_selftest = 1

            else:
                need_update_selftest = 0
            

            print  ("herehere3")
            sql = "INSERT INTO pvs_checktask (module_name, baseline_code, test_code, yum_request, author, ostype, self_test_id, chk_username, chk_pwd_encrypt, need_update_selftest) VALUES('cache', '%s', '%s', ' ', '%s@sogou-inc.com', '0', '%s', 'qa_svnreader', '%s', %s)" %(base_svn, test_svn, user, task_id, orxstr, need_update_selftest)
            logger.debug("pvs_sql: %s" %sql)
            print ("pvs_sql: %s" %sql)


            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
                print
                db.close()
                return HttpResponse("Db Error<br><b>Maybe Chinese charactor</b><br>" + user +'<br>' + test_svn + '<br>' + base_svn + '<br>')
    except:
        pass

    return HttpResponseRedirect('/testcache/task_queue')
'''


def add(request):
    if request.method == "POST":
        task_params = summary_form(request.POST)
        #print(str(task_params).encode('utf-8').decode('unicode_escape'))
        if task_params.is_valid():
            #print(task_params.cleaned_data)
            params_data = task_params.cleaned_data
            data = TestSummary.objects.create(create_time = get_now_time(), remarks = params_data['remark'],
                   testsvn = params_data['test_svn'], basesvn = params_data['base_svn'], 
                   newconfip = params_data['new_conf_ip'], newconfpath = params_data['new_conf_path'],
                   newconfuser = params_data['new_conf_user'], newconfpassw = params_data['new_conf_passwd'],
                   newdataip = params_data['new_data_ip'], newdatapath = params_data['new_data_path'],
                   newdatauser = params_data['new_data_user'], newdatapassw = params_data['new_data_passwd'],
                   testitem = params_data['test_item'])
                   
            return HttpResponseRedirect('/TestSummary/task_queue')
            
           
    elif request.method == "GET":
        task_params = summary_form()
    else:
        task_params = summary_form()
    
    return render(request, 'TestSummary/index.html', {'task_params': task_params})
    
'''
def task_queue(request):
    try:
        page = int(request.GET['page'])
    except:
        page = int(1)
    item_on_page = int(15)
    task_list_t =  testcache.objects.order_by('id')[::-1]
    total = len(task_list_t)

#### if total == 0 return another html


    print (total)
    total_page = total/item_on_page + 1
    if (total % item_on_page == 0):
        total_page -= 1
    if (page > total_page):
        page = total_page
    task_list = []
    
    begin = int((page-1)*item_on_page)
    end = int(page*item_on_page)
    if (end > total):
        end = int(total)
    
    for item in task_list_t[begin:end]:
        s_time = ""
        run_stat = ""
        c_time = str(item.create_time)
        s_time = str(item.start_time)
        user = item.user

        testitem = 0
        testitem = item.testitem
        test_item = ""
        print ("testitem:", testitem)

        if (int((int(testitem)/1000) % 10) == 1):
            test_item = "pvscheck "
            print ("test_item1: ", test_item)

        if (int((int(testitem)/100) % 10) == 1):
            test_item += "dmfgl "
            print ("test_item2: ", test_item)

        if (int((int(testitem)/10) % 10) == 1):
            test_item += "performance "
            print ("test_item3: ", test_item)


        print ("test_item:", test_item)
        remarks = item.remarks
        
#        task_list.append({'create_time': c_time, 'user': user, 'status': item.status, 'start_time': s_time, 'task_id': str(item.id), 'test_item':test_item, 'remarks': remarks})
        task_list.append({'create_time': c_time, 'user': user, 'status': item.status, 'start_time': s_time, 'task_id': str(item.id), 'test_item':test_item, 'remarks': remarks})
    page_list = []
    print ("total page: %d" % total_page)
    for i in range(int(total_page)):
        page_list.append(i+1)
    try:
        uid = request.COOKIES['uid']
    except:
        uid = ''
    return render(request, 'TestSummary/task_queue.html', {'task_list': task_list_t, 'page_list': page_list, 'page': page, 'uid': uid})
'''

def task_queue(request):
    try:
        page = int(request.GET['page'])
    except:
        page = int(1)
        
    item_on_page = int(15)
    task_list_t =  TestSummary.objects.order_by('-id')
    total = len(task_list_t)
    total_page = int(total/item_on_page) + 1
    
    if total % item_on_page == 0:
        total_page -= 1    
    if page > total_page:
        page = total_page
    
    begin = int((page-1) * item_on_page)
    end = int(page * item_on_page)
    if end > total:
        end = int(total)
    
    task_list = []   
    for t in task_list_t[begin:end]:
        task_list.append(t)
    
    page_list = []
    for i in range(int(total_page)):
        page_list.append(i+1)    
       
    return render(request, 'TestSummary/task_queue.html', {'task_list': task_list, 'page_list': page_list, 'page': page})
    
    
def task_detail(request):
    task_id = int(request.GET['id'])
    data = TestSummary.objects.get(id=task_id)
    if (data == None):
        return HttpResponseRedirect('/TestSummary/task_queue')
    #(creat_time, user, status, start_time, errlog, runningIP, test_qps, base_qps, diff, testitem, testsvn, onlinesvn ,newdatapath, querydata) = data

    errlog_list = data.errorlog.split('\n')
    #errlog_list = data.errorlog.decode('utf-8').split('\n')
    c_time = ""
    s_time = ""
    c_time = str(data.create_time)
    s_time = str(data.start_time)

    testitem = data.testitem[1:-1].replace("'", "").split(", ")
    print(testitem)

    #用于在run again对话框中标识所选测试项
    test_item_mark = {}
    test_item_mark['performance'] = 1 if 'performance' in testitem  else 0
    test_item_mark['gcov'] = 1 if 'gcov' in testitem  else 0
    test_item_mark['difftest'] = 1 if 'difftest' in testitem  else 0

    try:
        uid = request.COOKIES['uid']
    except:
        uid = ''
    
    task_detail = {'create_time': c_time, 'start_time': s_time, 'status': data.status, 'user': data.user, 'task_id': str(task_id), 'runningIP': data.runningIP, 'testitem': testitem, 'testsvn': data.testsvn.split('\n'), 'onlinesvn': data.basesvn.split('\n'), 'newconfip': data.newconfip, 'newconfuser': data.newconfuser, 'newconfpassw': data.newconfpassw, 'newconfpath': data.newconfpath, 'newdataip': data.newdataip, 'newdatauser': data.newdatauser, 'newdatapassw': data.newdatapassw, 'newdatapath': data.newdatapath, 'remarks': data.remarks}
    
    diff_res_num = SummaryDiff.objects.filter(task_id=task_id).count()
    
    return render(request, 'TestSummary/task_detail.html', {'task_detail': task_detail, 'test_item_mark': test_item_mark, 'errlog': errlog_list, 'test_cost': data.performance_test.split('\n'), 'base_cost': data.performance_base.split('\n'), 'result_gcov': data.code_gcov_result, 'diff_res_num': diff_res_num, 'pvscheck_result_link': 'link','uid': uid})



def diff_detail(request):

    if request.method == 'GET':
        task_id = int(request.GET['id'])
        data = SummaryDiff.objects.filter(task_id=task_id)
        
        diff = mydifflib.HtmlDiff(wrapcolumn=100)
        diff_result = []
        for el in data:
            diff_data = diff.make_file(
                            el.base_res.splitlines(keepends=True),
                            el.test_res.splitlines(keepends=True)
                            ).replace('nowrap="nowrap"', '')

            diff_result.append(diff_data)
        

        return render(request, 'TestSummary/diff_detail.html', {'li':diff_result})



def re_add(request):
    # login_url = "https://login.sogou-inc.com/?appid=1544&sso_redirect=http://selftesting.web.sjs.ted&targetUrl="
    # try:
        # user = request.COOKIES['uid']
    # except:
        # return HttpResponseRedirect(login_url)
    user = ""
    testitem_lst = []
    
    mission_id = int(request.POST['mission_id'])   
    data = TestSummary.objects.get(id=mission_id) 


    try:
        difftest = str_dos2unix(request.POST['difftest'])
        if difftest == '1':
            testitem_lst.append('difftest')
    except:
        pass
        
    try:
        gcov = str_dos2unix(request.POST['gcov'])
        if gcov == '1':
            testitem_lst.append('gcov')
    except:
        pass
        
    try:
        performance = str_dos2unix(request.POST['performance'])
        if performance == '1':
            testitem_lst.append('performance')
    except:
        pass

    remarks = str_dos2unix_space(request.POST['remarks'])
    
    testitem = str(testitem_lst)
    
    data_re_add = TestSummary.objects.create(create_time=get_now_time(), user=user, testitem=testitem, testsvn=data.testsvn, basesvn=data.basesvn, newconfip=data.newconfip, newconfuser=data.newconfuser, newconfpassw=data.newconfpassw, newconfpath=data.newconfpath, newdataip=data.newdataip, newdatauser=data.newdatauser, newdatapassw=data.newdatapassw, newdatapath=data.newdatapath, remarks=remarks)

    return HttpResponseRedirect('/TestSummary/task_queue')



def set_cancel(request):
    mission_id = int(request.GET['id'])
    print ("mission_id: ", mission_id)
    item = TestSummary.objects.get(id=mission_id)
    item.status = 6
    item.save()
    return HttpResponse("")

def logout(request):
    response = HttpResponseRedirect('https://login.sogou-inc.com/logout.jsp?appid=1544&sso_redirect=http://selftesting.web.sjs.ted&targetUrl=')
    if ('uid' in request.COOKIES):
        response.delete_cookie("uid")
    return response

def get_now_time():
    timeArray = time.localtime()
    return  time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

def str_dos2unix(input):
    return input.replace('\r\n', '\n').replace(' ', '')

def str_dos2unix_space(input):
    return input.replace('\r\n', '\n')

def stringxor(str1, str2):
    orxstr=""
    for i in range(0,len(str1)):
        rst=ord(list(str1)[i])^ord(list(str2)[i])
        orxstr=orxstr+ chr(rst)
    return orxstr

svn_key = 'uYSlU9TFCCkk7mqxrmZi5TxKkiEZqjYPiZN2mhXe'

