lasso = Lasso() # Lasso is also known as the L1 norm 
lasso.fit(X_train, y_train)


y_pred_train = lasso.predict(X_train)
y_pred_test =  lasso.predict(X_test)

train_mse = mean_squared_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)

train_res = y_train - y_pred_train 
test_res = y_test - y_pred_test

print('Train Mean Squarred Error:', train_mse)
print('Test Mean Squarred Error:', test_mse)
print('Train r2 score:', lasso.score(X_train, y_train))
print('Test r2 score:', lasso.score(X_test, y_test))

fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(5, 20))

ax[0].scatter(y_train, y_pred_train)
ax[1].scatter(y_pred, train_res)

ax[2].barh(y=X_train.columns, width=lasso.coef_)
ax[2].set_title('How feature effected results[Over/Under shoot actual value]')

plt.tight_layout()