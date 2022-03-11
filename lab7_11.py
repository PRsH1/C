import os
dict=input("작업할 디렉터리 입력:")
os.chdir(dict)
image=open("DSC_0104.jpg","rb")

imgread=image.read()

newdict=input("복사할 디렉터리를 입력하세요:")

os.chdir(newdict)
image2=open("DSC-0104_2.jpg","wb")
image2.write(image.read())
image.close()
image2.close()

