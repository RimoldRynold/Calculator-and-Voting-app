from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
    return render(request,'index1.html')
     

def submitquery(request):
    q = request.POST['query']
    # return HttpResponse(q)


    # jsondict = {
    #     'q' : q
    # }
    # return JsonResponse(jsondict)

    try:
        ans = eval(q)   #eval is an inbuilt function in python which takes string as an mathematical equation then evaluates and return answer to the equation
        mydictionary = {
            'q' : q,
            'ans' : ans,
            'error' : False,
            'result' :True
        }
        return render(request,'index1.html',context=mydictionary)
    except:
        mydictionary={
            'error' : True,
            'result' :False
        }
        return render(request,'index1.html',context=mydictionary)