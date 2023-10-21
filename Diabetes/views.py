from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import joblib
from .utils import get_plot
def home(request):
    return render(request,"index.html")
def result(request):
    lis=[]
    name=request.GET['name']
    lis.append(request.GET['P'])
    lis.append(request.GET['G'])
    lis.append(request.GET['B'])
    lis.append(request.GET['S'])
    lis.append(request.GET['I'])
    lis.append(request.GET['BM'])
    lis.append(request.GET['D'])
    lis.append(request.GET['A'])

    datasets={'Pregnancies':lis[0],'Glucose':lis[1],'BloodPressure':lis[2],'SkinThickness':lis[3],'Insulin':lis[4],'BMI':lis[5],'DiabetesPedigreeFunction':lis[6],'Age':lis[7]}
    
    print(datasets)
    
    userinput=pd.DataFrame(datasets,index=[0])
    print(lis)
    print(userinput)
    model=joblib.load("model.sav")
    ans=model.predict(userinput)
    print(ans)
    if(ans==[0]):
        x="not diabetic"
        color='blue'
    else:
        x="Diabetic"
        color='red'
    print(x)
    chart0=get_plot(userinput,'Pregnancies',20,2,color)
    chart1=get_plot(userinput,'Glucose',220,10,color)
    chart2=get_plot(userinput,'BloodPressure',130,10,color)
    chart3=get_plot(userinput,'SkinThickness',1100,10,color)
    chart4=get_plot(userinput,'Insulin',900,50,color)
    chart5=get_plot(userinput,'BMI',70,5,color)
    chart6=get_plot(userinput,'DiabetesPedigreeFunction',3,0.2,color)
    return render(request,"result.html",{'chart0':chart0,'chart1':chart1,'chart2':chart2,'chart3':chart3,'chart4':chart4,'chart5':chart5,'chart6':chart6,'name':name,'ans':x,'preg':lis[0],'glu':lis[1],'bp':lis[2],'st':lis[3],'ins':lis[4],'bmi':lis[5],'dpf':lis[6],'age':lis[7]})
def report(request):
    lis=[]
    name=request.GET['name']
    lis.append(request.GET['P'])
    lis.append(request.GET['G'])
    lis.append(request.GET['B'])
    lis.append(request.GET['S'])
    lis.append(request.GET['I'])
    lis.append(request.GET['BM'])
    lis.append(request.GET['D'])
    lis.append(request.GET['A'])

    datasets={'Pregnancies':lis[0],'Glucose':lis[1],'BloodPressure':lis[2],'SkinThickness':lis[3],'Insulin':lis[4],'BMI':lis[5],'DiabetesPedigreeFunction':lis[6],'Age':lis[7]}
    
    print(datasets)
    
    userinput=pd.DataFrame(datasets,index=[0])
    print(lis)
    print(userinput)
    model=joblib.load("model.sav")
    ans=model.predict(userinput)
    print(ans)
    if(ans==[0]):
        x="not diabetic"
        color='blue'
    else:
        x="Diabetic"
        color='red'
    print(x)
    chart0=get_plot(userinput,'Pregnancies',20,2,color)
    chart1=get_plot(userinput,'Glucose',220,10,color)
    chart2=get_plot(userinput,'BloodPressure',130,10,color)
    chart3=get_plot(userinput,'SkinThickness',1100,10,color)
    chart4=get_plot(userinput,'Insulin',900,50,color)
    chart5=get_plot(userinput,'BMI',70,5,color)
    chart6=get_plot(userinput,'DiabetesPedigreeFunction',3,0.2,color)
    return render(request,"details.html",{'chart0':chart0,'chart1':chart1,'chart2':chart2,'chart3':chart3,'chart4':chart4,'chart5':chart5,'chart6':chart6})
