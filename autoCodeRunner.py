# AUTHOR: MOHTI BK

# importing required modules
import subprocess
from rich.console import Console
console=Console()

# required function defination:
def isSupported(filename, suppoetedFileType):
    fileExt=filename.split(".")[-1]
    if fileExt in suppoetedFileType:
        return fileExt
    else:
        return False

def isValid(fileName):
    try:
        file=open(fileName,"rt")
        return file
    except:
        return False


def jsRun(filename):
    try:
        initialRun=subprocess.run(f"node {filename}")
        return True
    except:
        console.print(f"Error while running {filename}" , style="bold red on white")
        
      
def pyRun(filename):
    try:
        initialRun=subprocess.run(f"python {filename}")
        return True
    except:
        console.print(f"Error while running {filename}" , style="bold red on white")
       

def run(fileExtension):
    if fileExtension=='js':
        jsRun(fileName)
    elif fileExtension=='py':
        pyRun(fileName)
    else:
        pass

# supported file type :
suppoetedFileType=['js','py']

# file validating: 
fileName=input("Enter File Name : ")
fileExtension=None
filePrimary=None
while True:
    _isSupported=isSupported(fileName,suppoetedFileType)
    _isValid=isValid(fileName)
    if _isValid==False:
        console.print("File Not Found...",style="bold red on white")
        fileName=input("Enter File Name : ")
    else:
        if _isSupported==False:
            console.print("File Type is Not Supported...", style="bold red on white")
            fileName=input("Enter File Name : ")
            
        else:
            fileExtension=_isSupported
            filePrimary=_isValid
            break


# reading the data and storing :
primaryData=[]
for line in filePrimary:
    if line=='\n':
        continue;
    primaryData.append(line)

# initial program running:
console.print("Program Started...",style="bold white on cyan")
run(fileExtension)
console.print("Program Finished...\n",style="bold white on green")

# auto running system:
while True:
    secondaryData=[]
    fileSecondary=isValid(fileName)
    if filePrimary==False:
        console.print("File Not Found...",style="bold red on white")
        break
    else:
        for line in fileSecondary:
            if line=='\n':
                continue
            else:
                secondaryData.append(line)
        
    if secondaryData != primaryData:
        primaryData=secondaryData
        console.print("Program Started...",style="bold white on cyan")
        run(fileExtension)
        console.print("Program Finished...\n",style="bold white on green")
    else:
        pass