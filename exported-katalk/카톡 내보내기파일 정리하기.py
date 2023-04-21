import os

path = "C:/Users/sbeen1840"
file_list=os.listdir(path)
file_list=[file for file in file_list if file.endswith(".txt")] 

for i in file_list:
    FileName = f"C:/Users/sbeen1840/{i}"
    
    with open(FileName, "r", encoding='UTF8') as f:
        lines = f.readlines()
        f.close()

    with open(FileName, "w",  encoding='UTF8') as f:
        for line in lines:
            f.write(line.replace('채팅방 관리자가 메시지를 가렸습니다.', ''))
        f.close()
        
    with open(FileName, "r", encoding='UTF8') as f:
        lines = f.readlines()
        f.close()

    with open(FileName, "w",  encoding='UTF8') as f:
        for line in lines:
            f.write(line.replace('[카톡작성자명]', '\n'))
        f.close()
        
    