"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render


def index1(request):
    return render(request, 'index.html')


def analyse(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    titlecase = request.POST.get('titlecase', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed}
        djtext = analysed

    if fullcaps == "on":
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'ChangeToUpperCase', 'analysed_text': analysed}
        djtext = analysed

    if newlineremover == "on":
        analysed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed = analysed + char
        params = {'purpose': 'New Line Remover', 'analysed_text': analysed}
        djtext = analysed

    if extraspaceremover == "on":
        analysed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char
        params = {'purpose': 'Remove Extra Space', 'analysed_text': analysed}
        djtext = analysed

    if charcount == 'on':
        params = {'purpose': 'Number of characters in the line ', 'analysed_text': len(djtext)}
        djtext = analysed

    if titlecase == "on":
        analysed = djtext.title()
        params = {'purpose': 'ChangeToTitleCase', 'analysed_text': analysed}
        djtext = analysed

    if (
            removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on" and titlecase != "on"):
        return HttpResponse("Please Select Any Operation")
    return render(request, 'analyse.html', params)


def contactus(request):
    return render(request, 'contactus.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def translator(request):
    engtohindi = request.POST.get('engtohindi', 'off')
    hinditoeng = request.POST.get('hinditoeng', 'off')
    djtext = request.POST.get('txt', 'Enter Your Text ')
    if engtohindi=="on":
        text1 = djtext
        from translate import Translator
        translator = Translator(from_lang='hi', to_lang="en")
        translation = translator.translate(text1)
        print(translation)
        from gtts import gTTS
        mytext = translation
        language = 'en-us'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("C:\\Users\\vivek\\Desktop\\translate.mp3")
        params = {'purpose': 'Translation', 'trans_text':mytext, 'original_text':djtext}
        return render(request, 'translate.html', params)
    elif hinditoeng=="on":
        text1 = djtext
        from translate import Translator
        translator = Translator(from_lang='en', to_lang="hi")
        translation = translator.translate(text1)
        print(translation)
        from gtts import gTTS
        mytext = translation
        language = 'en-us'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("C:\\Users\\vivek\\Desktop\\translate.mp3")
        params = {'purpose': 'Translation', 'trans_text':mytext, 'original_text':djtext}
        return render(request, 'translate.html', params)
    else:
        params = {'purpose': 'TRANSLATION'}
        return render(request, 'translate.html', params)
