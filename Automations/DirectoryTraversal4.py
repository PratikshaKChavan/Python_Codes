import os
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

    for FolderName , SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder name is:"+FolderName)

        for subf in SubFolderName:
            print("Sub Folder name is:"+subf)
            
        for fname in FileName:
            print("File name is:"+fname)
def main():
    print("Enter the name of directory that you wan to travel:")
    DirName = input()
    DirectoryWatcher(DirName)
    

if __name__=="__main__":
    main()