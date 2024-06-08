from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql

em=''
pwd=''

def login(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password='12345',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Email":
                em=value
            if key=="Password":
                pwd=value
    
        c="select * from users where email ='{}' and Password = '{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, 'error.html')
        else:
            return render(request,'welcome.html')

    return render(request, 'login_page.html')