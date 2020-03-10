clean_df = video_game_df.copy()

# Drop observations with no name
clean_df.dropna(axis=0, how='any', thresh=None, subset=['Name'], inplace=True)

# Drop all platforms with less than 20 games released
_ = clean_df['Platform'].value_counts()
clean_df = clean_df[clean_df.isin(_.index[_ >= 20]).values]

# Drop all games released after 2016
_ = clean_df[clean_df['Year_of_Release'] >= 2017].index
clean_df.drop(_, inplace=True)

#Drop all publisher with null or unknown if the developer column isn't in the unique list of publisher
_  = clean_df['Publisher'].unique()
_ = ~clean_df[clean_df['Publisher'].isin([np.nan, 'Unknown'])]['Developer'].isin(_)
clean_df.drop(_[_ == True].index, inplace=True)

#Find all publisher with null or unknown.  If the developer column is in the unique list of publishers, make the publisher this value
clean_df['Publisher'] = np.where(clean_df['Publisher'].isin([np.nan, 'Unknown']), clean_df['Developer'], clean_df['Publisher'])

#If there are any nan values left drop the,
clean_df.dropna(axis=0, how='any', thresh=None, subset=['Publisher'], inplace=True)

# Drop high interaction columns NA/EU/JP/OTHER Sales
clean_df.drop(['NA_Sales','EU_Sales', 'JP_Sales', 'Other_Sales'], axis=1, inplace=True)

# Drop high user/critic score/count columns as well as Developer
clean_df.drop(['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating'], axis=1, inplace=True)

# Drop all nan year of release rows
clean_df.dropna(axis=0, how='any', thresh=None, subset=['Year_of_Release'], inplace=True)

# Convery years to int..
clean_df['Year_of_Release'] = clean_df['Year_of_Release'].astype(int)

clean_df['Name_Character_Length'] = clean_df['Name'].map(lambda name : len(name))

clean_df['Name_Word_Count'] = clean_df['Name'].map(lambda name : len(name.split()))