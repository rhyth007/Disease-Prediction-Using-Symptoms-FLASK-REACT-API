# import pandas as pd
# import pickle
# from  sklearn.preprocessing import  StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
#
# df = pd.read_csv('training.csv')
#
# X = df.drop(columns=['prognosis'])
# y = df['prognosis']
#
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1,random_state=50)
#
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test =sc.transform(X_test)
# classifier = RandomForestClassifier()
# classifier.fit(X_train,y_train)
#
#
# # predictions = classifier.predict(X_test)
# # score=accuracy_score(y_test,predictions)
# # print(score)

import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
df = pd.read_csv("Training.csv")
X  = df.drop(columns=['prognosis'])
y = df['prognosis']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.7)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
pickle.dump(model,open("modely.pkl","wb"))
# print(y)
predictions = model.predict(X_test)
score=accuracy_score(y_test,predictions)
print(score)