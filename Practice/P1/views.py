from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def analyze(request):
    djtext = (request.POST.get('text','default'))
    removepuns = request.POST.get('removepuns','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    if removepuns =='on':
        punctuations = '''!@#$%^&*(){}:";'<>?,./\|-_+=~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
    
    if fullcaps =='on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose':'UPPERCASE','analyzed_text':analyzed}
        djtext = analyzed
    
    if newlineremover =='on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char !='\r':
                analyzed += char
        params = {'purpose':'New line remover','analyzed_text':analyzed}
        djtext = analyzed
    
    if extraspaceremover =='on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1] == " "):
                analyzed += char
            
        params = {'purpose':'Extra space remover','analyzed_text':analyzed}
        djtext = analyzed
    
    if (removepuns!= 'on' and  fullcaps!= 'on' and newlineremover !='on' and extraspaceremover!='on'):
        return HttpResponse('please select any operator and try again')
    
    return render(request,'analyze.html',params)

def home(request):
    params = {'name':'fathima','place':'Lalit Ashok'}
    return render(request,'home.html',params)