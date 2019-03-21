 # -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:27:03 2019

@author: gaurav
"""


from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def mzak(request):
    return render(request, 'mzak.html')


def count(request):
    fulltext = request.GET['fulltext']
    
    wordlist = fulltext.split()
    
    worddictionary = {}
    
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1
            
    sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)   
        
    
    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
