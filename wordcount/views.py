from typing import List, Any

from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


# def eggs(request):
#     return HttpResponse("<h1>I love Eggs</h1>")
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedword = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    # return render(request, "count.html", {'fulltext': fulltext,'count':len(wordlist),'worddictionary':worddictionary})
    return render(request, "count.html", {'fulltext': fulltext, 'count': len(wordlist), 'worddictionary': sortedword})


def about(request):
    return render(request, 'about.html')
