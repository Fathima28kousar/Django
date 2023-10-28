from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {'name':'fathima','place':'Mars'}
    return render(request,'index.html',params)

def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse('remove punc')

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changing letters to uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose':'Removes newline','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif extraspaceremover == "on":
        analyzed = " ".join(djtext.split())
        params = {'purpose': 'Removes extra spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    



    else:
        return HttpResponse('Error')
