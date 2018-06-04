# make class predictions for X_test_dtm
y_pred_class = logreg.predict(X_test_dtm)

# calculate predicted probabilities for X_test_dtm
y_pred_prob = logreg.predict_proba(X_test_dtm)[:, 1]
print(y_pred_prob)

# calculate accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred_class))

# calculate AUC
print("AUC:",metrics.roc_auc_score(y_test, y_pred_prob))
