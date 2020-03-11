base_lr = LinearRegression()
base_lr.fit(X_train, y_train)

y_pred_train = base_lr.predict(X_train)
y_pred_test =  base_lr.predict(X_test)

train_mse = mean_squared_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)

train_r2 = r2_score(y_train, y_pred_train)
test_r2 = r2_score(y_test, y_pred_test)

n = X_train.shape[0]
p = X_train.shape[1]
train_adjusted_r2 = 1 - ((1 - train_r2)*((n-1)/(n-p-1)))
test_adjusted_r2 = 1 - ((1 - test_r2)*((n-1)/(n-p-1)))

train_res = y_train - y_pred_train 
test_res = y_test - y_pred_test

#R-squared values are negative baseline model fails to capture shape of data.
print(f"""
Train Mean Squarred Error: {train_mse}
Test Mean Squarred Error: {test_mse}

Train r2 score: {train_r2}
Test r2 score: {test_r2}

Train Adjusted r2 score: {train_adjusted_r2}
Test Adjusted r2 score: {test_adjusted_r2}
""")

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 10))
ax[0].scatter(y_train, y_pred_train)
ax[1].scatter(y_pred, train_res);