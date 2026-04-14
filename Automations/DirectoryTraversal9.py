import os
import sys

def DirectoryWatcher(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)
    
    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag==False):
        print("Path is valid but not a directory")
        exit()

    print("Absolute path is: "+DirectoryName)
    TotalCount = 0
    EmptyCount = 0

    for FolderName , SubFolderName, FileName in os.walk(DirectoryName):    
        for fname in FileName:
            TotalCount = TotalCount + 1
            if (os.path.getsize(os.path.join(FolderName,fname))==0):
                EmptyCount = EmptyCount + 1
                print("File name is:"+fname)
                os.remove(os.path.join(FolderName,fname))
    print("Total number of files scanned:",TotalCount)
    print("Total number of empty file deleted:",EmptyCount)
            

def main():
    Border = "-"*54
    print(Border)
    
    print("-----------Marvellous Automation--------")
    print(Border)
    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h") or (sys.argv[1]=="--H"):
            print("This application is used to perform-----")
            print("This is the automation script")

        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("Use the given script as")
            print("ScriptName.py  NameOfDirectory")
            print("Please provide valid absolute path")
        else:
            DirectoryWatcher(sys.argv[1])
    else:
        print("Invalid number of line arguments")
        print("Use the given flags as:")
        print("--h : Used to display help")
        print("--u : Used to display usage")

    print(Border)
    
    print("----Thank you for using our script-------")
    print("---------Marvellous Infosystem----------")
    
    print(Border)

    

if __name__=="__main__":
    main()