import os
import pandas as pd
from wakati import wakati_text

path = './files_csv'
files = []

for x in os.listdir(path):
    files.append(x)

#print(files)

word_model_df = pd.DataFrame()

for i in range(len(files)):
    df = pd.read_csv('./files_csv/'+files[i])
    detail = ""
#    print(df)

    for j in range(len(df)):
        detail += df.iloc[j, 1]
        # print(df.iloc[j,1])
    text = pd.Series([df.iloc[0,0], wakati_text(detail)], index=["県名", "分かち書きテキスト"])
    # print(text)
    word_model_df = word_model_df.append([text], ignore_index=True)

# print(word_model_df)

word_model = word_model_df.to_csv('word_model.csv', index=False)