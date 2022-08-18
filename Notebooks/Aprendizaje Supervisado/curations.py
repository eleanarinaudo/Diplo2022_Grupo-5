import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.preprocessing import OneHotEncoder

def scaler_data(df, *, columns):
    df = StandardScaler().fit_transform(df)
    df = pd.DataFrame(df, columns=columns)
    return df

def encoder_categorical_data_and_scaler_some_data(df, *, cat_cols, model="general"):
    if model == "general":
        for col in cat_cols:
            df[col] = df[col].astype(str)
            df[col] = LabelEncoder().fit_transform(df[col])
        columns = df.columns
        df = scaler_data(df, columns=columns)
    elif model == "MLP":
        # One-hot encondig variable categorica tipo
        cols = ['Deck_of_spaceship']
        df[cols] = df[cols].astype(str)
        ohe = OneHotEncoder(sparse=False)
        ohe.fit(df[cols])
        encoded = ohe.categories_
        col = cols[0]
        labels = [col + '_' + a for a in encoded]
        encoded = ohe.transform(df[['Deck_of_spaceship']])
        #Crea df con las columnas del encoding
        encoded_df = pd.DataFrame(encoded, columns=labels[0])

        # One-hot encondig variable categorica tipo
        cols = ['Port_or_Starboard']
        df[cols] = df[cols].astype(str)
        ohe = OneHotEncoder(sparse=False)
        ohe.fit(df[cols])
        encoded = ohe.categories_
        col = cols[0]
        labels = [col + '_' + a for a in encoded]
        encoded = ohe.transform(df[['Port_or_Starboard']])
        #Crea df con las columnas del encoding
        encoded_df_2 = pd.DataFrame(encoded, columns=labels[0])

        cat_cols.remove('Deck_of_spaceship')
        cat_cols.remove('Port_or_Starboard')
        for col in cat_cols:
            df[col] = df[col].astype(str)
            df[col] = LabelEncoder().fit_transform(df[col])
        df = pd.concat([df, encoded_df, encoded_df_2], axis=1)
        df = df.drop(['Deck_of_spaceship', 'Port_or_Starboard'], axis=1)
        columns = df.columns
        some_cat_cols = [
            'Deck_of_spaceship_A', 
            'Deck_of_spaceship_B', 
            'Deck_of_spaceship_C',
            'Deck_of_spaceship_D', 
            'Deck_of_spaceship_E', 
            'Deck_of_spaceship_F',
            'Deck_of_spaceship_G', 
            'Deck_of_spaceship_T', 
            'Port_or_Starboard_P',
            'Port_or_Starboard_S'
        ]
        columns_to_scaler = [ col for col in columns if col not in some_cat_cols]
        df = scaler_data(df, columns=columns_to_scaler)
    return df
    