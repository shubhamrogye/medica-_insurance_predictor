
from django.shortcuts import render
import numpy as np
from numpy.core.fromnumeric import reshape
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
warnings.filterwarnings('ignore')

def home(request):
        return render(request,"home.html")


def predict(request):
    return render(request,"predict.html")        

def result(request):
   df=pd.read_csv("Health_Insurance\insurance.csv")
   df=df.drop_duplicates()
   dummies=pd.get_dummies(df.sex)
   merge=pd.concat([df,dummies],axis=1)
   df1=merge.drop(['sex','female'],axis=1)
   dummi1=pd.get_dummies(df1.smoker)
   merge1=pd.concat([df1,dummi1],axis=1)
   df2=merge1.drop(['smoker','no'],axis=1)
   dummi2=pd.get_dummies(df2.region)
   merge2=pd.concat([df2,dummi2],axis=1)
   df3=merge2.drop(['region','northeast'],axis=1)
   target_name='expenses'
   y=df3[target_name]
   x=df3.drop(target_name,axis=1)
   x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=7)
   lr=LinearRegression()
   lr.fit(x_train,y_train)
   

   var5= 0
   var7=0
   var9=0
   var10=0
   var11=0

   var1=float(request.POST['n1'])
   var2=float(request.POST['n2'])
   var3=float(request.POST['n3'])
   var4=str(request.POST['n4'])
   var6=str(request.POST['n5'])
   var8=str(request.POST['n6'])

   
       

   if(var4=="Male"):
      var5=1
   var5=0 


   if (var6=="Yes"):
       var7=1
   var7=0  

   if(var8=="Northeast"):
       var9=0 
       var10=0
       var11=0
   elif(var8=="Northwest"):
        var9=1
        var10=0
        var11=0
   elif(var8=="Southeast"):
       var9=0
       var10=1
       var11=0
   else:
       var9=0
       var10=0
       var11=1





   pred=lr.predict(np.array([var1,var2,var3,var5,var7,var9,var10,var11]).reshape(1,-1))
   pred=round(pred[0])
   price="The predicted price is " +str(pred)
   return render(request,"predict.html",{"result2":price})    