from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.POST.get('text', '')
    remove_punc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    remove_newlines = request.POST.get('removenewlines', 'off')
    remove_spaces = request.POST.get('removespaces', 'off')
    char_count = request.POST.get('charcount', 'off')

    analyzed = text

    if remove_punc == 'on':
        analyzed = ''.join(c for c in analyzed if c.isalnum() or c.isspace())

    if uppercase == 'on':
        analyzed = analyzed.upper()

    if lowercase == 'on':
        analyzed = analyzed.lower()

    if remove_newlines == 'on':
        analyzed = analyzed.replace('\n', '').replace('\r', '')

    if remove_spaces == 'on':
        analyzed = ' '.join(analyzed.split())

    result = {
        'original': text,
        'analyzed': analyzed,
        'char_count': len(analyzed) if char_count == 'on' else None,
    }

    return render(request, 'analyze.html', result)
