class variable:
    name=''
    value=0
    def __init__(self,name,value):
        self.value=value
        self.name=name

    def getValue(self):
        return self.value
    def incrValue(self):
        self.value+=1
        print('Value of '+self.name+' incremented to '+str(self.value))
        return self.value
    def decrValue(self):
        if self.value>0:
            self.value-=1
            print('Value of '+self.name+' decremented to '+str(self.value))
            return self.value
        else:
            print('ERROR: Must use only positive integers')
            return -1
    def resetValue(self):
        self.value=0
        return self.value
    def getName(self):
        return self.name

def getValueFromArr(arr, search):
    count=0
    found=False
    for each in arr:
        if(each.getName()==search):
            found=True
            return count
        else:
            count+=1
    if(found==False):
        return 10000000000

def whileLoopBreak(arr,val,var):
    tempInt=getValueFromArr(var, arr[0][val])
    tempStr1=str(arr[1][val])
    tempStr2=str(var[tempInt].getValue())
    if(tempStr1==tempStr2):
        return 'break'
    else:
        return arr[3][val]
def main():
    variables=[]
    breakVar=False
    i= 0
    whileTracker=[[],[],[],[]]     #[variable,value,condition,start]
    fileName='barebones.txt'    #For Testing
    #file=str(input('What Barebones (txt) file would you like to run \n>>>'))
    file=open(fileName)
    instructions=file.readlines()
    instructions.append("JE SUIS FINIS;")
    while breakVar==False:
            currentInstruction=instructions[i].strip()
            if(currentInstruction[-1:]!=';'):       #check for syntax error
                #print('Syntax Error, missing ";" on line '+str(i+1))
                breakVar=True;
                i+=1
            elif currentInstruction=="JE SUIS FINIS;":
                breakVar=True
                print('Successful Ending')
            elif(currentInstruction=='end;'):       #end program/break while loop
                if(len(whileTracker[0])==0):
                    print('Successful Ending')
                    breakVar=True
                else:                               #Break the while loop
                    if(whileLoopBreak(whileTracker,len(whileTracker[0])-1,variables)=='break'):
                        whileTracker[0].pop()
                        whileTracker[1].pop()
                        whileTracker[2].pop()
                        whileTracker[3].pop()
                        i+=1
                    else:
                        i=whileLoopBreak(whileTracker,len(whileTracker[0])-1,variables)
            elif(currentInstruction[:5]=='clear'):  #declaring variables/clearing
                searchCheck=getValueFromArr(variables,currentInstruction[6:currentInstruction.find(';')])
                if(searchCheck==10000000000):
                    variables.append(variable(currentInstruction[6:currentInstruction.find(';')],0))
                    print('Declared variable',currentInstruction[6:currentInstruction.find(';')])

                else:
                    print('Resetting variable '+ variables[searchCheck].getName())
                    variables[searchCheck].resetValue()

                i+=1

            elif(currentInstruction[:4]=='incr'): #incrementing
                try:
                    variables[getValueFromArr(variables,currentInstruction[5:currentInstruction.find(';')])].incrValue()
                    i+=1
                except IndexError:
                    print("ERROR: You haven't declared this variable")
                    breakVar=True
            elif(currentInstruction[:4]=='decr'): #decrementing
                try:
                    if(variables[getValueFromArr(variables,currentInstruction[5:currentInstruction.find(';')])].decrValue()!=-1):
                        i+=1
                    else:
                        BreakVar=True
                        i+=1

                except IndexError:
                    print("ERROR: You haven't declared this variable")
                    breakVar=True
            elif(currentInstruction[:5]=='while'):  #while loop
                try:
                    i+=1
                    print('beginning while loop')
                    tempString=currentInstruction[6:]
                    whileTracker[0].append(tempString[:tempString.find(' ')])
                    tempString=tempString[tempString.find(' ')+1:]
                    whileTracker[2].append(tempString[:tempString.find(' ')])
                    tempString=tempString[tempString.find(' ')+1:]
                    whileTracker[1].append(tempString[:tempString.find(' ')])
                    whileTracker[3].append(i)
                except IndexError:
                    print("ERROR: You haven't declared this variable")
                    breakVar=True
            else:
                print('ERROR: Unrecognised code')
                breakVar=True
main()
