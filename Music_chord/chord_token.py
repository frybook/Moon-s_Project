import pandas as pd

"Ⅰ","ⅱm","ⅲm","Ⅳ","Ⅴ7","ⅵm","ⅶ"
index_name = ["Ⅰ","#Ⅰ","ⅱ","#ⅱ","ⅲ","Ⅳ","#Ⅳ","Ⅴ","#Ⅴ","ⅵ","#ⅵ","ⅶ",
          "Ⅰm","#Ⅰm","ⅱm","#ⅱm","ⅲm","Ⅳm","#Ⅳm","Ⅴm","#Ⅴm","ⅵm","#ⅵm","ⅶm",
          "Ⅰ7","#Ⅰ7","ⅱ7","#ⅱ7","ⅲ7","Ⅳ7","#Ⅳ7","Ⅴ7","#Ⅴ7","ⅵ7","#ⅵ7","ⅶ7",
          "Ⅰm7(b5)","#Ⅰm7(b5)","ⅱm7(b5)","#ⅱm7(b5)","ⅲm7(b5)","Ⅳm7(b5)","#Ⅳm7(b5)","Ⅴm7(b5)","#Ⅴm7(b5)","ⅵm7(b5)","#ⅵm7(b5)","ⅶm7(b5)",
          "ⅠmM7","#ⅠmM7","ⅱmM7","#ⅱmM7","ⅲmM7","ⅣmM7","#ⅣmM7","ⅤmM7","#ⅤmM7","ⅵmM7","#ⅵmM7","ⅶmM7",
          "Ⅰdim","#Ⅰdim","ⅱdim","#ⅱdim","ⅲdim","Ⅳdim","#Ⅳdim","Ⅴdim","#Ⅴdim","ⅵdim","#ⅵdim","ⅶdim",]

df = pd.DataFrame(index=index_name)

df['number'] = range(1, len(index_name) + 1)

df.to_csv("chord_token.csv", index_label='chord',encoding='utf-8')
chord_token = pd.read_csv("chord_token.csv", index_col='chord',encoding='utf-8')
print(df)

#%%
