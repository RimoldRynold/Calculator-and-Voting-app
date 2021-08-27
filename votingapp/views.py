
from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

# Create your views here.
arr=['Python','JavaScript','TypeScript','Rust','MATLAB','Arduino ','SQL','Objective-C','R','C++','PHP','Scala','Swift','Ruby','Perl','Go','Java','C']
globalcnt = dict()

def index(request):
   
    mydictionary ={
        'arr' : arr,
    }
    return render(request,'index.html',context=mydictionary)

def getquery(request):
    q=request.GET['languages']
    
    # for 1st occurence
    if q not in globalcnt:
        globalcnt[q]=1

    # if already exist,then increment the value
    else:
        globalcnt[q]=globalcnt[q]+1
    mydictionary = {
        'arr' :arr,
        'globalcnt' : globalcnt,
        
    }
    return render(request,'index.html',context=mydictionary)


    

def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True))
    mydictionary = {
        'arr' :arr,
        'globalcnt' : globalcnt
    }
    return render(request,'index.html',context=mydictionary)
    
