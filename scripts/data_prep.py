"""
One hot encoding three catagorical columns because they don't have too many unique values
"""
_ = pd.get_dummies(global_df['Rating'], drop_first=True)
global_df = pd.concat([global_df, _], axis=1)

_ = pd.get_dummies(global_df['Genre'], drop_first=True)
global_df = pd.concat([global_df, _], axis=1)

_ = pd.get_dummies(global_df['Platform'], drop_first=True)
global_df = pd.concat([global_df, _], axis=1)


"""
Drop all columns not needed to build models
"""
global_df.drop(columns=['Developer', 'Name', 'Platform', 'Rating'], inplace=True)