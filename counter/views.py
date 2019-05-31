from django.shortcuts import render
import operator


def home(request):
    return render(request, 'counter/home.html')


def counter(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'counter/counter.html', {'fulltext': fulltext,
                                                    'count': len(wordlist),
                                                    'sortedwords': sortedwords})


def about(request):
    return render(request, 'counter/about.html')
