#import requests
#import json
from dictionary import *

def parse_glos(file1):
    with open(file1,'r') as p:
        terms = {}
        currentname = ''
        current = ''
        onelineterm = False
        for line in p:
            if len(line) < 3:
                #letter headings
                pass
                #print [line]
            elif line.split()[0].isupper():
                if onelineterm is False:
                    #term is continuation of previous line
                    pass
                else:
                    #new term
                    #print currentname + ": " + current
                    terms[currentname.lower().strip()] = current
                    current = ''
                    currentname = ''
                onelineterm = False
                #(first word is caps)
                lowered = False
                for word in line.split():
                    if word == 'A' or not word.isupper():
                        onelineterm = True
                        lowered = True
                        current+=word+' '
                    elif lowered is False:
                            currentname+=word+' '
                
            else:
                #same term
                current += line.strip('\n')+' '
    return terms

def vocab_ui(file1):
    glos = parse_glos(file1)
    while True:
        term = raw_input('Enter the first vocab term: ').lower()
        try:
            print glos[term]
        except:
            print 'sorry, term is not found or the program sucks.'

def homeworkify_ui(file1):
    #1 by 1
    terms = []
    term= 'none'
    print 'type q after you are finished'
    while True:
        term = raw_input('Enter term (last term was ' +term + '): ')
        if term == 'q':
            break
        terms.append(term.strip())
    return homeworkify(file1,terms)

def homeworkify_ui_batch(file1):
    terms = raw_input('Enter terms separated by commas: ')
    terms = [term.strip() for term in terms.split(',')]
    return homeworkify(file1,terms)

def homeworkify(file1,terms,prenum = '', postnum = '.', splitter = ': '):
    glos = parse_glos(file1)
    i= 0
    homework_str = ''
    for term in (term.lower() for term in terms):
        i+=1
        try:
            defin = get_def(term)
            if defin is None:
                raise TypeError
        except:
            print term + ' not found'
            from random import randint
            #defin = glos.items()[randint(0,len(glos))][1] <- gets random def
            tried = []
            while set(tried) != set(terms):
                term = terms[randint(0,len(terms)-1)]
                try:
                   # defin = glos[term]
                    defin = get_def(term)
                    if defin is None:
                        raise TypeError
                    break
                except:
                    tried.append(term)
                    defin = 'all terms not found'
        homework_str+=str(i) + postnum + ' ' + term + splitter + defin + '\n'
    return homework_str
        
"""def get_google_def(word):
    r = requests.get("http://www.google.com/dictionary/"
                     "json?callback=dict_api.callbacks.id100&q="+word+
                     "&sl=en&tl=en&restrict=pr%2Cde&client=te")
    print r.text
    print json.load(r.text)"""
