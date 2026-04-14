import os
def DirectoryWatcher(DirectoryName):
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