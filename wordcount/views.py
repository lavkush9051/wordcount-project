from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,'about.html')

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist= fulltext.split()

    worddictionary={}

    for word in wordlist:
        #increase
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            #add to dictionary
            worddictionary[word] = 1

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist)})
