from django.shortcuts import render, redirect
from .models import signup_table
from operator import itemgetter
import mysql.connector
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method=="POST":
        table=signup_table()
        table.email=request.POST['email']
        table.name=request.POST['name']
        table.pswd=request.POST['pswd']
        table.rpswd=request.POST['rpswd']
        con=mysql.connector.connect(host="localhost",user="root",passwd="1973",database="blog")
        cursor=con.cursor()
        sql_em="select email from signup_signup_table"
        cursor.execute(sql_em)
        r=[]
        for i in cursor:
            r.append(i)
        res=list(map(itemgetter(0),r))
        if (table.pswd !=table.rpswd) or (table.email in res):
            return redirect('signup')
        else:
            table.save()
            global em
            em=table.email
            print("data has been saved")
            return redirect('homearticle')
    else:     
        return render(request,'signup.html')


def login(request):
    con1=mysql.connector.connect(host="localhost",user="root",passwd="1973",database="blog")
    cursor1=con1.cursor()
    con2=mysql.connector.connect(host="localhost",user="root",passwd="1973",database="blog")
    cursor2=con2.cursor()
    sql_em="select email from signup_signup_table"
    sql_pswd="select pswd from signup_signup_table"
    cursor1.execute(sql_em)
    cursor2.execute(sql_pswd)
    r=[]
    p=[]
    for i in cursor1:
        r.append(i)
    for j in cursor2:
        p.append(j)
        
    res1=list(map(itemgetter(0),r))
    res2=list(map(itemgetter(0),p))

    if request.method=="POST":
        email=request.POST['email']
        pswd=request.POST['pswd']
        i=0
        k=len(res1)
        global em
        em=email
        while i<k:
            if res1[i]==email and res2[i]==pswd:
                print("okay")
                return redirect('homearticle')
            i = i+1
        return render(request,'login.html')    
    else:     
        return render(request,'login.html')

def get_email():
    return em 