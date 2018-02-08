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
    if request.method=='GET':
        v = models.HostInfo.objects.filter(id=nid).values('id', 'HostIP', 'Hostname', 'version', 'app__proline','admin','passwd')



        return render(request,'shell.html',{'item':v})
