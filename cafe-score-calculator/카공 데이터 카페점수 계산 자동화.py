
import pandas as pd


list = []
for i in range(29):
    df= pd.read_excel("C:/Users/sbeen1840/Desktop/cagong/%d.xlsx"%(i+1),  engine = "openpyxl") 
    
    
    df['LABEL-4']= df['LABEL-3'].str.slice(13, 17) 
    df['LABEL-4']= df['LABEL-3'].map(lambda x:x[13:17])
    df['LABEL-4'] = pd.to_numeric(df['LABEL-4'])
    
    a = df['LABEL-4'].sum()
    df_cond = df[df["LABEL-2"].str.contains('좌석|청결|집중')]
    b = df_cond['LABEL-4'].sum()
    
    list.append(b/a)

cafe = pd.DataFrame()
cafe['공부환경점수']=list