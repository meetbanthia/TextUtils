# i have created this file - Meet
from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request,'index.html')
def analyzer(request):
    input_text = request.POST.get('text','default')
    it = input_text
    rempunc = request.POST.get('rempunc','off')
    charcount = request.POST.get('charcount','off')
    sprem = request.POST.get('sprem','off')
    nlrem = request.POST.get('nlrem','off')
    capitalize = request.POST.get('capitalize','off')
    analyzed_text = ''
    purpose = ''

    any_checkbox = False

    length_text = 0

    if input_text == '':
        return HttpResponse('''No Text Provided<a href="http://127.0.0.1:8000/"><br>Home</a>''')
    if charcount == 'on':
        purpose = purpose + '''We will count number of characters in your input text\n'''
        length_text = len(input_text)
        any_checkbox = True
    if rempunc == 'on':
        purpose = purpose + '''We will remove punctuations\n'''
        punc_sym = string.punctuation
        for char in input_text:
            if char not in punc_sym:
                analyzed_text = analyzed_text + char
        input_text = analyzed_text
        any_checkbox = True
    if capitalize == 'on':
        purpose = purpose + '''We will capitalize all the aplhabets\n'''
        input_text = input_text.upper()
        any_checkbox = True
    if sprem == 'on':
        purpose = purpose + '''We will remove all the blank spaces\n'''
        input_text = input_text.replace(" ","")
        any_checkbox = True
    if nlrem == 'on':
        purpose = purpose + '''We will remove all the newline characters\n'''
        analyzed_text = ''
        for char in input_text:
            if char!='\n' and char!='\r':
                analyzed_text = analyzed_text + char
        input_text = analyzed_text       
        any_checkbox = True
    if any_checkbox == False:
        return HttpResponse('''No Analyzer Selected <a href="http://127.0.0.1:8000/"><br>Home</a>''')
    else:
        temp = {'text':it,'purpose':purpose,'analyzed_text':input_text,'length':length_text}
        return render(request,'analyzer.html',temp)
