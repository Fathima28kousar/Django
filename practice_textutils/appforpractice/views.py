from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {'name':'fathima','place':'Mars'}
    return render(request,'index.html',params)

def removepunc(request):
    djtext = request.POST.get('text','default')
    print(djtext)
    return HttpResponse('remove punc')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuations','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changing letters to uppercase','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if extraspaceremover == "on":
        analyzed = " ".join(djtext.split())
        params = {'purpose': 'Removes extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre",analyzed)
        params = {'purpose':'Removes newline','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

   
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

def contact(request):
    return HttpResponse("<h1>contact us page<h1>")

def about(request):
    return HttpResponse("<h1>About us page<h1>")