#One hot encode the catagorical 
_ = ['Platform', 'Genre']
prep_df = pd.get_dummies(clean_df, columns=_, drop_first=True)

prep_df['Platform'] = clean_df['Platform']
prep_df['Genre'] = clean_df['Genre']

# Drop names, it will not help the model
prep_df.drop('Name', axis=1, inplace=True)

# Scale the years to a time frame
prep_df['Year_of_Release_Scaled'] = prep_df['Year_of_Release'] - prep_df['Year_of_Release'].min()

X = prep_df
y = prep_df['Global_Sales']
log_y = np.log(y)

X_train, X_test, y_train, y_test = train_test_split(X, log_y, test_size= 0.2)

X_train = feature_extract_mean_count_median(X_train, ['Platform','Genre', 'Publisher', 'Year_of_Release'], 'Global_Sales')
X_test = feature_extract_mean_count_median(X_test, ['Platform','Genre', 'Publisher', 'Year_of_Release'], 'Global_Sales')

X_train.drop(['Year_of_Release', 'Publisher', 'Global_Sales', 'Platform', 'Genre'], axis=1, inplace=True)
X_test.drop(['Year_of_Release', 'Publisher', 'Global_Sales', 'Platform', 'Genre'], axis=1, inplace=True)