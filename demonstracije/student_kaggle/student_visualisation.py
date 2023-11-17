import pandas as pd


def cat_ohe_util(df_col):
    print(df_col.head())
    vS = list(set(df_col))
    print(vS)
    chc = int(input("cat 0, ohe 1 bin 2 none 3: \n"))
    if chc == 3:
        pass
    elif chc == 2:
        df_col.name = df_col.name + "_" +vS[0]
        df_col = (df_col == vS[0]).astype(int)
        print(df_col)
    elif chc == 1:
        df_col = (pd.get_dummies(df_col,prefix=df_col.name + "_")).astype(int)
        print(df_col)
    elif chc == 0:
        mapa = lambda a: {vS[i]:i for i in range(len(vS))}[a]
        df_col = df_col.map(mapa)
        print(df_col)
        print(vS)
    return df_col,vS

df = pd.read_csv("datasets/student_math_clean.csv")
new_df = pd.DataFrame()
print(df.columns)
maps = {}
i = 0
for c in df.columns:
    res,maps0 = cat_ohe_util(df[c])
    maps[c] = maps0
    if new_df.empty:
        new_df = pd.DataFrame(res)
    else:
        new_df = new_df.join(res)
    print(new_df)
    print(i/len(df.columns))
    i += 1
print(new_df)
print(maps)
with open("datasets/maps.mps", "w") as omap:
    omap.write(str(maps))
new_df.to_csv("math_data_cleaned.csv")