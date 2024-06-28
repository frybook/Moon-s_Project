import os
import pandas as pd


#%%
def csv_text():
    # 폴더 경로 설정
    folder_path = "분석코드/"
    
    # 폴더 내의 모든 파일 이름 가져오기
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    # 사전 형태로 데이터프레임 저장
    dataframes = {}
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        # Remove the file extension from the filename to use it as a variable name
        variable_name = os.path.splitext(file_name)[0]
        df = pd.read_csv(file_path, encoding='euc-kr')
        dataframes[variable_name] = df
        
    return dataframes

#%%
