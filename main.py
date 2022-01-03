
import os
from posixpath import join
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            # enumerate local files recursively 
        
        for root, dirs, files in os.walk(file_from):
            
            for filename in files:
                # construct the full local path 
            local_path = os.path.join(root, filename)
                  

                # construct the

def main():
    access_token = '5gk9Wq3BNNoAAAAAAAAAAfOiMQzTZUvVHLPWnXQxIHeYzxIxKFE5yvyxR-5aCddw'
    transferDataobject = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferDataobject.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()