import pandas as pd
def load_data():
    df = pd.read_csv('files/olympics.csv',skiprows = 1)
    for column in df.columns:
        if '01' in column:
            df.rename(inplace=True, columns = {column:column.replace("01 !","Gold")})
        elif '02' in column:
            df.rename(inplace=True, columns = {column:column.replace("02 !","Silver")})
        elif '03'in column:
            df.rename(inplace=True, columns = {column:column.replace("03 !","Bronze")})
        else:
            pass
    country_names = [x.split('\xc2\xa0(')[0] for x in df.iloc[:,0]]
    df.set_index(pd.Series(country_names), inplace=True)
    df.rename(columns={"Unnamed: 0" : "Country"},inplace = True)
    df.iloc[:,0] = country_names
    df.drop(['Totals'],axis=0, inplace= True)
    return df

def first_country(df):
    return df.iloc[0,:]

def gold_medal(df):
    return df['Gold'].argmax()

def biggest_difference_in_gold_medal(df):
    return (df['Gold']-df['Gold.1']).argmax()

def get_points(df):
    df['Points'] = 3*df.iloc[:,12] + 2*df.iloc[:,13] + df.iloc[:,14]
    return df.loc[:,'Points']

# df = load_data()
# print(first_country(df)["# Summer"])
# print(gold_medal(df))
# print(biggest_difference_in_gold_medal(df))
# print(get_points(df))
