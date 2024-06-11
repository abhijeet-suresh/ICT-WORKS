
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data=pd.read_csv('winequality-red (1).csv')
data.head()
#Clipping outliers in the columns with the use of a for loop//IQR method
def iqr_clipping(data, cols):
    for col in cols:
            Q1 = data[col].quantile(0.25)
            Q3 = data[col].quantile(0.75)
            IQR = Q3 - Q1
            print("Column Name: ", col)
            print("IQR: ", IQR)
            low_lim = Q1 - 1.5*IQR
            upp_lim = Q3 + 1.5*IQR 
            print("Lower Limit: ", low_lim)
            print("Upper Limit: ", upp_lim)
            print("\n")
            data[col] = data[col].clip(lower=low_lim, upper=upp_lim)
    return data
cols ={'density','fixed acidity','volatile acidity', 'residual sugar','chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density','pH', 'sulphates', 'alcohol','quality','citric acid'}
filtered_df = iqr_clipping(data,cols)

#Defining X and Y
X=data.drop(columns=['quality'],axis=1)
y=data['quality'].apply(lambda y_value: 1 if y_value >=7 else 0)


#Split the train and test data
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=3,test_size=0.2)


##Random Forest Classifier//Selected this model as accuracy score was shown 93%
model=RandomForestClassifier()
rcmodel=model.fit(X_train, y_train)


#Accuracy score
X_test_prediction=model.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,y_test)
print('The test data accuracy is',test_data_accuracy)


# Save the model to a file
pickle.dump(model,open('redwine.pkl','wb'))