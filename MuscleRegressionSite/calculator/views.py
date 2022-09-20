from turtle import end_fill
from django.shortcuts import render
import pandas as pd
from math import nan
import numpy as np
from .helper import *
from io import BytesIO
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "input.html")

def calculate(request):

    weight= request.POST['weight']
    weightUnit=request.POST['WeightUnit']
    heightUnit=request.POST['HeightUnit']
    height= request.POST['height']
    sex = request.POST['sex']
    age= request.POST['age']


    try:
        x=float(weight)
        if weightUnit=="lb":
            weight=float(weight)*0.453592
            weightOutput='Weight(lb)'
        else:
            weightOutput='Weight(kg)'
        try:
            y = float(height)
            if heightUnit=="in":
                height=float(height)*2.54
                heightOutput='Height(in)'
            else:
                 heightOutput='Height(cm)'   
            try:
                z= float(age)
                Muscs=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL']
                Levs=['L4', 'L3', 'L2', 'L1', 'T12', 'T11', 'T10', 'T9', 'T8', 'T7', 'T6', 'T5', 'T4']
                CSA_O_All=[]
                Dist_O_All=[]
                Ang_O_All=[]
                for i in Muscs:
                    M=Muscle(sex,age,height,weight,i)
                    CSA_O,Dist_O,Ang_O=M.GenerateResults()
                    CSA_O_All.append(CSA_O)
                    Dist_O_All.append(Dist_O)
                    Ang_O_All.append(Ang_O)
            
                Output_SubjectInfo=pd.DataFrame([[sex,age,weight,height]],columns=[['Sex','Age','Weight','Height']])
                
                Output_CSA=np.asarray(CSA_O_All)
                Output_CSA=pd.DataFrame(Output_CSA,columns=Levs,index=Muscs)
                Output_CSA.insert(17,'Unit',['mm'])

                Output_Dist=np.asarray(Dist_O_All)
                Output_Dist=pd.DataFrame(Output_Dist,columns=Levs,index=Muscs)
                Output_Dist.insert(17,'Unit',['mm'])

                Output_Ang=np.asarray(Ang_O_All)
                Output_Ang=pd.DataFrame(Output_Ang,columns=Levs,index=Muscs)
                Output_Ang.insert(17,'Unit',['degrees'])

                with BytesIO() as b:
                    writer=pd.ExcelWriter(b,engine='xlsxwriter')
                    Output_CSA.to_excel(writer,sheet_name="CSA_Results")
                    Output_Dist.to_excel(writer,sheet_name="Distance_Results")
                    Output_Ang.to_excel(writer,sheet_name="Angle_Results")
                    Output_SubjectInfo.to_excel(writer,sheet_name="SubjectInfo",header=['Sex','Age',str(weightOutput),str(heightOutput)],startcol=0,index=False)
                    writer.save()
                    filename='MuscleValues'
                    content_type='application/vnd.ms-excel'
                    response=HttpResponse(b.getvalue(),content_type=content_type)
                    response['Content-Disposition']='attachment; filename="' +filename + '.xlsx"'
                    return response
            except ValueError:
                res='Enter a number for Age'
                return render(request,"result.html",{"result":res})
        except ValueError:
            res='Enter a number for height'
            return render(request,"result.html",{"result":res})
    except ValueError:
        res='Enter a number for weight'
        return render(request,"result.html",{"result":res})
