from this import s
from django.shortcuts import render
from Articles.models import article_table
from Signup.models import signup_table
from Signup.views import *
from django.db.models import Q
from datetime import date

# Create your views here.

def homearticle(request):
    if request.method=="POST":
        t_g=request.method['topic']
        global s
        s=t_g
    else: 
        query_results = article_table.objects.all()
        return render(request, 'homearticle.html',{'article_table':query_results})

def contentpage(request,title):
    print(str(title))
    postdetails = article_table.objects.filter(Q(title=str(title)))
    return render(request,'contentpage.html', {'postdetails' : postdetails})

def myblog(request):
    info=get_email()
    postdetails = article_table.objects.filter(Q(email=info))
    return render(request,'myblog.html', {'personalarticle' : postdetails})

def create(request):
    if request.method=="POST":
        table=article_table()
        table.email=get_email()
        table.name=request.POST['name']
        table.title=request.POST['title']
        table.content=request.POST['content']
        table.date= date.today()
        table.genre=request.POST['genre']
        table.save()
        print("data has been saved")
        return redirect('homearticle')
    else:     
        return render(request,'create.html')

def search(request):
    con1=mysql.connector.connect(host="localhost",user="root",passwd="1973",database="blog")
    cursor1=con1.cursor()
    con2=mysql.connector.connect(host="localhost",user="root",passwd="1973",database="blog")
    cursor2=con2.cursor()
    sql_g="select genre from articles_article_table"
    sql_t="select title from articles_article_table"
    cursor1.execute(sql_g)
    cursor2.execute(sql_t)
    r=[]
    p=[]
    for i in cursor1:
        r.append(i)
    for j in cursor2:
        p.append(j)
    res1=list(map(itemgetter(0),r))
    res2=list(map(itemgetter(0),p))
    i=0
    k=len(res1)
    while i<k:
        if res1[i]==s:
            searcharticle = article_table.objects.filter(Q(genre=s))
            return render(request,'search.html', {'searcharticle' : searcharticle})
        elif res2[i]==s:
            searcharticle = article_table.objects.filter(Q(title=s))
            return render(request,'search.html', {'searcharticle' : searcharticle})
        i = i+1
    query_results = article_table.objects.all()
    return render(request, 'homearticle.html',{'article_table':query_results})