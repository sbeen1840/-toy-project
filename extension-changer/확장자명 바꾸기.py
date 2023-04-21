import os
import glob

files = glob.glob("C:/Users/sbeen1840/folder/*.txt") # 원하는 디렉토리 설정
for name in files: # files는 디렉토리 내의 모든 이름(파일명+확장자명)들이 집합이 됨
    src = os.path.splitext(name) #파일명+확장자명에서 파일명기준으로 나누고
    os.rename(name, src[0]+'.md') # 파일+확장자명을 파일명+새로운확장자명으로 바꿈
    
