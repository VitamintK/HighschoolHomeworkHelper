import time
import unittest
from BeautifulSoup import *
import urllib
import sys

def Flashcards(chaptnum, s):
	#redeclare
	definitions = []
	terms = []
	#idnum = s.parent["onclick"]
	for line2 in s.parent.parent.contents:
		pass
	#s2 = "".join([line.strip() for line in s.parent.parent.split("\n")])
	"""whitespace in s.parent.parent, goes through as "\n" in s.parent.parent.contents
	creating extra array values.  Try to remove them.
	"""
	idnum = s.parent.parent.contents[17].contents[0]["value"]
	#opening the flash cards page
	vocabpage = urllib.urlopen("http://www.studystack.com/flashcard-"+idnum)
	vocabs = vocabpage.read()
	vocabsoup = BeautifulSoup(vocabs)
	vocabterms = vocabsoup.find(id="theTable")
	#parsing for the definitions and names
	vocabterms = "".join([line.strip() for line in vocabterms.renderContents().split("\n")])
	vocabterms = vocabterms.replace('> <', '><')
	vocabterms = BeautifulSoup(vocabterms)
	x=0
	while x< len(vocabterms.contents):
		terms.append(vocabterms.contents[x].contents[0].renderContents())
		definitions.append(vocabterms.contents[x].contents[1].renderContents())		
		x+=1
	return [terms, definitions]

def general(urll):
	definitions = []
	terms = []
	vocabpage = urllib.urlopen(urll)
	vocabs = vocabpage.read()
	vocabsoup = BeautifulSoup(vocabs)
	vocabterms = vocabsoup.find(id="theTable")
	#parsing for the definitions and names
	vocabterms = "".join([line.strip() for line in vocabterms.renderContents().split("\n")])
	vocabterms = vocabterms.replace('> <', '><')
	vocabterms = BeautifulSoup(vocabterms)
	x=0
	while x< len(vocabterms.contents):
		terms.append(vocabterms.contents[x].contents[0].renderContents())
		definitions.append(vocabterms.contents[x].contents[1].renderContents())		
		x+=1
	return [terms, definitions]

def getFlash(chaptnum):
    f = urllib.urlopen("http://www.studystack.com/users/stophammertime1290")
    body1 = f.read()
    soup1 = BeautifulSoup(body1)
    s = soup1.find(text=re.compile("AP Bio Chapter "+chaptnum))
    tempa = Flashcards(chaptnum, s)
    return tempa

import json
import requests

client_id='Nus9eQ2FBA'

def quizlet(set_id, postnum='.', splitter=': '):
    set_id=str(set_id)
    hw=''
    h = requests.get('https://api.quizlet.com/2.0/sets/'+set_id+'?client_id='+client_id)
    i = json.loads(h.text)
    counter=0
    for j in i['terms']:
        counter+=1
        term, defin = j['term'], j['definition']
        hw+=str(counter) + postnum + ' ' + term + splitter + defin + '\n'
    return hw

print quizlet('14390408')
print quizlet('14642329')
