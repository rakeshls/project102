import cv2
import dropbox
import time
import random
starttime = time.time()
def takesnapshot():
    number = random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        imagename = 'image'+str(number)+'.png'
        cv2.imwrite(imagename,frame)
        starttime = time.time()
        result=False
    return imagename
    print('snapshottaken')  
    videocaptureobject.release()
    cv2.destroyAllWindows()
def upload_file(imagename):  
    access_token='sl.AyhJYMgynrQ7nswuVddkxeO-MUxuMSCds5UBwkyXog7YSlz1_rZPL9Zq34Izdj-_4ghHtLlTTYkEqvHiaq1svxY_9mfqjILsDVvnTy_6UPLrF6pmWxyQ2NjffThs1NZnIUjoIrY0LAWv'
    filename = imagename
    file_from = filename
    file_to = '/automation/'+imagename
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')
def main():
    while(True):
        if((time.time()-starttime)>200):
            name=takesnapshot()
            upload_file(name)
main()                    