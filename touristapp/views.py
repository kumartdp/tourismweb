from django.shortcuts import render
from django.http import HttpResponse
from touristapp.models import Student
import sqlite3
import googletrans
from googletrans import Translator
import os
import pandas as pd

def home(request):
    return render(request,'index.html',{})
def register(request):
    if(request.method == 'POST'):

        fname=request.POST['first_name']
        lname=request.POST['last_name']
        plc=request.POST['places']
        dv=request.POST['date_of_visiting']
        dl=request.POST['date_of_leaving']
        uid=request.POST['unique']
        tr=request.POST['tourist']
        str1=request.POST['street']
        add=request.POST['additional']
        zip1=request.POST['zip']
        cou=request.POST['country']
        cd=request.POST['code']
        phn=request.POST['phone']
        emil=request.POST['your_email']
        con=sqlite3.connect('form.db')
        cr=con.cursor()
        cr.execute('insert into report values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(fname,lname,plc,dv,dl,uid,tr,str1,add,zip1,cou,cd,phn,emil))
        print('values inserted ')
        con.commit()



    return render(request,'register.html',{})
def office(request):
    if(request.method == 'POST'):
        fnme=request.POST['username']
        pswd=request.POST['pass']
        con=sqlite3.connect('form.db')
        cr=con.cursor()
        nam='admin'
        pass1='123'
        x=[]
        if fnme==nam and pswd==pass1:
            cr.execute('select * from report')
            row=cr.fetchall()

            for i in row:
                x.append(i)
            return HttpResponse(x)
    


    return render(request,'office.html',{})
def select(request):
    return render(request,'options.html',{})    

def options(request):
    lan=request.GET['choice']
    place=request.GET['place']
    translator=Translator()


    
    if(place=='hyd'):
        l1=''
        l2=''
        l3=''
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'Charminar.txt')   #full path to text.
        f1 = open(file_path , 'r')
        file_path1 = os.path.join(module_dir, 'Birla Mandir.txt')   #full path to text.
        f2 = open(file_path1 , 'r')
        file_path2 = os.path.join(module_dir, 'Golconda Fort.txt')   #full path to text.
        f3 = open(file_path2 , 'r')
        
        l4=f1.readlines()
        l5=f2.readlines()
        l6=f3.readlines()

        for i in l4:
                a=translator.translate(i,dest=lan)
                l1=l1+a.text
        for i in l5:
                a=translator.translate(i,dest=lan)
                l2=l2+a.text
        for i in l6:
                a=translator.translate(i,dest=lan)
                l3=l3+a.text
        
        return render(request,'hyd.html',{'charminar':l1,'birla':l2,'golconda':l3})
    elif (place=='war'):
        l1=''
        l2=''
        l3=''
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'Pakhal Lake.txt')   #full path to text.
        f1 = open(file_path , 'r')
        file_path1 = os.path.join(module_dir, 'Ramappa Temple.txt')   #full path to text.
        f2 = open(file_path1 , 'r')
        file_path2 = os.path.join(module_dir, 'Thousand Pillar Temple.txt')   #full path to text.
        f3 = open(file_path2 , 'r')
        
        l4=f1.readlines()
        l5=f2.readlines()
        l6=f3.readlines()

        for i in l4:
                a=translator.translate(i,dest=lan)
                l1=l1+a.text
        for i in l5:
                a=translator.translate(i,dest=lan)
                l2=l2+a.text
        for i in l6:
                a=translator.translate(i,dest=lan)
                l3=l3+a.text
        
        return render(request,'war.html',{'pl':l1,'rt':l2,'tpt':l3})
    else:
        l1=''
        l2=''
        l3=''
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'Elgandal Fort.txt')   #full path to text.
        f1 = open(file_path , 'r')
        file_path1 = os.path.join(module_dir, 'Kondagattu.txt')   #full path to text.
        f2 = open(file_path1 , 'r')
        file_path2 = os.path.join(module_dir, 'Lower Manair Dam.txt')   #full path to text.
        f3 = open(file_path2 , 'r')
        
        l4=f1.readlines()
        l5=f2.readlines()
        l6=f3.readlines()

        for i in l4:
                a=translator.translate(i,dest=lan)
                l1=l1+a.text
        for i in l5:
                a=translator.translate(i,dest=lan)
                l2=l2+a.text
        for i in l6:
                a=translator.translate(i,dest=lan)
                l3=l3+a.text
        
        return render(request,'knr.html',{'ef':l1,'k':l2,'lmd':l3})

def crop(request):
    print('hi')
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'd.csv')
    df=pd.read_csv(file_path)   
    if(request.method=='POST'):
        state=request.POST['state']
        district=request.POST['district']
        df1=df[(df['state']==state) & (df['district']==district)]
        l=df1['success_rate'].nlargest(3).index.tolist()
        l1=[df.iloc[i]['crop'] for i in l]
        print(l1)
        return render (request,'suggest.html',{'c1':l1[0],'c2':l1[1],'c3':l1[2]})
    return render (request,'boot.html',{})

def main(request):
    return render(request,'boot.html',{})


            



        

    

        


    



