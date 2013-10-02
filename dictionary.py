"""
Uses the unofficial google dictionary API
Author:Sridarshan Shetty (India)
Twitter: http://twitter.com/sridarshan
Website: http://sridarshan.co.cc
"""
import urllib,ast,sys
def check(string):
	return string.replace("&#39","'")
def get_def(word):
	if len(sys.argv)!=1:
		words=sys.argv[1:]
		word=""
		for i in words:
			word+=i
			word+=" "
	else:
		try:
			pass#word=raw_input("Enter a word:")
		except KeyboardInterrupt:
			print '\nIO Error'
			return	
	try:
		url="http://www.google.com/dictionary/json?callback=s&q="+word+"&sl=en&tl=en&restrict=pr,de&client=te"
		obj=urllib.urlopen(url);
	except:
		print "Please check your internet connection and try again"
		return
	content=obj.read()
	obj.close()
	content=content[2:-10]
	dic=ast.literal_eval(content)
	if dic.has_key("webDefinitions"):
		webdef=dic["webDefinitions"]
		webdef=webdef[0]
		webdef=webdef["entries"]
		index=1
		index_list=["01","02","03","04","05","06","07","08","09","10"]
		for i in webdef:
			if index==2: #changed from 11 to 2.
				break
			#print word#," :",
			index+=1
		
			if i["type"]=="meaning":
				ans=i["terms"]
				op=ans[0]['text']
				split=op.split(';')
				return check(split[0].strip())
				count=0
				for i in split:
					if count!=0:
						pass #print "      "+check(i) #this prints example sentences.
					count+=1
	else:
		pass#print "Description unavailable for " + word<--debug messages were getting annoying
			
#if __name__=="__main__":get_def()
	

