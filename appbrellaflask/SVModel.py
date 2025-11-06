# import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# sklearn utilities
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# sklearn models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA

# TO-DO
#train-test split from database

# svm_model = SVC(kernel = 'poly')
# svm_model.fit(x_train, y_train)

#make a heatmap and will want to show on the website
# def conf_matrix_to_df(conf_matrix, target_names):
#     return pd.DataFrame(conf_matrix, columns=target_names, index=target_names)

# svm_predictions = svm_model.predict(X = x_test)
# conf_matrix = confusion_matrix(y_true = y_test, y_pred = svm_predictions)
# conf_matrix_to_df(conf_matrix, databunch.target_names)

# plt.title('Confusion Matrix Heat Map')
# plt.imshow(conf_df)
# plt.colorbar()
# plt.xlabel("True Class")
# plt.ylabel("Predicted Class")
# plt.show()