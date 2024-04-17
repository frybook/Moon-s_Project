df = pd.read_csv(file_path, header=None) # 데이터프레임 만들때 컬럼명을 제외
df.columns = df.iloc[0] # 컬럼을 iloc 0번째로 바꾸고
print(df)
df = df.drop(0) #0번째 제거
df.set_index(df.columns[0], inplace=True) # 
print(df)