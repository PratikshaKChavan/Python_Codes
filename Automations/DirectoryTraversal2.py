import os
def DirectoryWatcher():
    for FolderName , SubFolderName, FileName in os.walk("Marvellous"):
        print("Folder name is:"+FolderName)

        for subf in SubFolderName:
            print("Sub Folder name is:"+subf)
            
        for fname in FileName:
            print("File name is:"+fname)
def main():
    DirectoryWatcher()
    

if __name__=="__main__":
    main()