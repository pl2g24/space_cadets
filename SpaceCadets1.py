#--------------imports-----------
import urllib.request
from multiprocessing import Process
#-------------starting variables---
pageNo=7

titles=['Adrian']
latestFound=0
finished=False
names=[]
emails=[]
#-----------------subroutines-------
def getPage(pageNo):
    url = "https://www.southampton.ac.uk/people?page="+str(pageNo)
    text = urllib.request.urlopen(url).read()
    text=text.decode("utf8")
    return text
def addNames(string):
    global names
    global duplicateHandler
    if(duplicateHandler==3):
        names.append(string)
        duplicateHandler=0
    else:
        duplicateHandler+=1
   

def breakUpNames(name):
    tempString=""
    breakVar=False
    addCap=True
    spaceCounter=0
    for x in name:
        if(breakVar==False):
            if(addCap):
                tempString+=x.upper()
                addCap=False
            elif(x=='-'):
                addCap=True
                tempString+=' '
            else:
                tempString+=x
            
    addNames(tempString)
    return tempString

def findEmail(txt):
    global emails
    if(txt.find('mailto:')>=0):
        findEmail(txt[txt.find('mailto:')+1:])
        tempString=txt[txt.find('mailto:')+1:]
        emails.append(tempString[6:tempString.find('.uk')+3])
        
def findName(txt):
    global names
    search='/people/'
    if(txt.find(search)>=0):
        findName(txt[txt.find(search)+15:])
        tempString=txt[txt.find(search)+15:txt.find(search)+60]
        tempString=tempString[:tempString.find('"')]
        addNames(breakUpNames(tempString))
def main(lowerRange, upperRange):
    global duplicateHandler
    for x in range(lowerRange,upperRange):
        duplicateHandler=0
        findName(getPage(x))
        findEmail(getPage(x))
        print('By Page'+str(x)+' weve got '+str(len(names))+' names and '+str(len(emails))+' emails')
        
#-----------main------------------
main(437)       #Since I don't know threading/multiprocessing yet the program is a bit slow. 
i=0             #However I do think if I did it would be simple to implement
for each in names:
    print(str(i+1))
    print(each+'\t\t'+emails[i])
    i+=1
