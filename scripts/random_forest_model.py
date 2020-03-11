regr = RandomForestRegressor(max_depth=2, random_state=0)
regr.fit(X_train, y_train)

y_pred_train = regr.predict(X_train)
y_pred_test =  regr.predict(X_test)

train_mse = mean_squared_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)

train_mae = mean_absolute_error(y_train, y_pred_train) 
test_mae = mean_absolute_error(y_test, y_pred_test)

print(f"""
Train Mean Squarred Error: {train_mse}
Test Mean Squarred Error: {test_mse}

Train Mean Absolute Error: {train_mae}
Test Mean Absolute Error: {test_mae}

""")

fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(5, 20))
_ = regr.feature_importances_

ax[0].scatter(y_train, y_pred_train)
ax[1].scatter(y_pred, train_res)

ax[2].barh(y=X_train.columns, width=_)
ax[2].set_title('Most important feature in prediction')

plt.tight_layout();