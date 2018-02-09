from django.shortcuts import redirect,render,HttpResponse
from app1 import models
from console import sshconnet


# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        if request.POST.get('denglu'):
            u=request.POST.get('USER')
            p=request.POST.get('PASSWORD')
            obj=models.userInfo.objects.all().filter(username=u,passwd=p).first()
            print(obj,u,p)
            if obj:
                request.session['username']=u
                request.session['islogin']=True
                return redirect('/index/')

            else:
                return render(request,'login.html')
           #      i=''
           #      return render(request,'login2.html',{'i':i})
              #  return redirect('/login2.html/')
        # elif request.POST.get('zhuce'):
        #     u = request.POST.get('USER')
        #     p = request.POST.get('PASSWORD')
        #     obj = models.userInfo.objects.create(username=u,passwd=p)
        #     return redirect('/index/')

    else:
        return redirect('/login/')
def index(request):
    if request.method=='GET':
        return render(request,"index.html")
def hostlist(request):
    if request.method == 'GET':
        host=models.HostInfo.objects.all().values('HostIP','Hostname','version','id','app__proline')
        return render(request, "hostlist.html", {'host':host})
def addhost(request):
    if request.method=='GET':
        appname=models.appInfo.objects.all().values('proline').exclude(proline='idle')
        # b=models.appInfo.objects.get(proline='ios')
        # f=b.hostinfo_set.all().values('app')
        # print(f)
        return render(request,"addhost.html",{'app':appname})
    if request.method=='POST':
        ip=request.POST['IP']
        hostname=request.POST['Hostname']
        version=request.POST['version']

        app2=request.POST['app']
        obj = models.HostInfo(Hostname=hostname,HostIP=ip,version=version,app=models.appInfo.objects.get(proline=app2))
        obj.save()

        # b = models.appInfo.objects.get(proline=app2)
        # f=b.hostinfo_set.all().values('app')
        # print(f)
        # app2=list(f)[0]['app']
        #models.HostInfo.objects.create(Hostname=hostname,HostIP=ip,version=version,app_id=1)
    return redirect('/hostlist/')
def delhost(request,nid):
     models.HostInfo.objects.filter(id=nid).delete()
     return redirect('/hostlist/')
def edithost(request,nid):
    if request.method=='GET':
        v=models.HostInfo.objects.filter(id=nid).values('id','HostIP','Hostname','version','app__proline')
        applist =models.appInfo.objects.all().values('proline').exclude(proline='idle')
        return render(request,'edithost.html',{'item':v ,'applist':applist})
    elif request.method=='POST':
        ip = request.POST['IP']
        hostname = request.POST['Hostname']
        version = request.POST['version']

        app2 = request.POST['app']
        print(nid)
        models.HostInfo.objects.filter(id=nid).update(Hostname=hostname, HostIP=ip, version=version,
                              app=models.appInfo.objects.get(proline=app2))
        return redirect('/hostlist/')
def console(request):
    if request.method=='GET':
        return render(request,'consloe.html')
    elif request.method=='POST':
        command1=request.POST['command']
        result= sshconnet.connectssh(hostname='bogon', port='22', username='root', password='Ji@ye2016', command=command1)
        return render(request,'consloe.html',{'i':result})
def host_connect(request,nid):
    import time, hmac, hashlib, json
    user =nid
    print(user)
    gateone_server = "https://172.1.0.102"
    secret ="ODUwMTk5ZGNhNmYwNGViZTk0MGNlNTk3N2Y5YmY4ODM5Z"
    api_key ="YWZjY2ZlMjZkM2U4NGQ0ZGJkZDllMzUxYTMzOGFlZWZkZ"
    authobj = {
        'api_key': api_key,
         'upn': user,
        'timestamp': str(int(time.time() * 1000)),
        'signature_method': 'HMAC-SHA1',
        'api_version': '1.0'
    }
    my_hash = hmac.new(bytes(secret,'utf-8'),digestmod=hashlib.sha1)

    my_hash.update((authobj['api_key'] + authobj['upn'] + authobj['timestamp']).encode('utf-8'))

    authobj['signature'] = my_hash.hexdigest()
    print(authobj)
    # auth_info_and_server = {"url": gateone_server, "auth": authobj}
    # valid_json_auth_info = json.dumps(auth_info_and_server)
    valid_json_auth_info = json.dumps(authobj)
    if request.method=='GET':
        v = models.HostInfo.objects.filter(id=nid).values('id', 'HostIP', 'Hostname', 'version', 'app__proline','admin','passwd')
        return render(request,'shell.html',{'item':v,'auth_info':valid_json_auth_info})


# def generate_gate_one_auth_obj(request):
#     import time, hmac, hashlib, json
#
#     user = request.user.username
#
#     gateone_server = GATEONE_SERVER // 替换成对应的部署gateone的server的ip地址
#
#     secret = GATEONE_API_SECRET // 替换成对应的api
#     secret ，该信息
#     存放在gateone的配置文件30api.conf中
#
#     api_key = GATEONE_API_KEY // 替换成对应的api
#     key ，该信息
#     存放在gateone的配置文件30api.conf中
#
#     authobj = {
#
#         'api_key': api_key,
#
#         'upn': user,
#
#         'timestamp': str(int(time.time() * 1000)),
#
#         'signature_method': 'HMAC-SHA1',
#
#         'api_version': '1.0'
#
#     }
#
#     my_hash = hmac.new(secret, digestmod=hashlib.sha1)
#
#     my_hash.update(authobj['api_key'] + authobj['upn'] + authobj['timestamp'])
#
#     authobj['signature'] = my_hash.hexdigest()
#
#     auth_info_and_server = {"url": gateone_server, "auth": authobj}
#
#     valid_json_auth_info = json.dumps(auth_info_and_server)
#
#     # return HttpResponse(valid_json_auth_info)

