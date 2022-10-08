import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model

diabetes=datasets.load_diabetes()
# ['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])

diabetes_x1=diabetes.data[:,np.newaxis,2]
# print(diabetes_x1)
diabetes_x1_train=diabetes_x1[:-30]
diabetes_x1_test=diabetes_x1[-30:]
diabetes_y1_train=diabetes.target[:-30]
diabetes_y1_test=diabetes.target[-30:]
model=linear_model.LinearRegression()
model.fit(diabetes_x1_train,diabetes_y1_train)
diabetes_y1_pr=model.predict(diabetes_x1_test)
# print("mean squred error is : ",mean_squared_error(diabetes_y1_test,diabetes_y1_pr))
print("weights: ",model.coef_)
print("intercepts: ",model.intercept_)
plt.scatter(diabetes_x1_test,diabetes_y1_test)
plt.plot(diabetes_x1_test,diabetes_y1_pr)

plt.show()
