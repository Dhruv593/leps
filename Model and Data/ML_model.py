import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import pickle as pkl

data = pd.read_csv(r"D:\Dhruv College Coding + Lab Manual + Projects\Dhruv DE Projects\Loan Eligibility Prediction System\Loan\Model and Data\loan-train.csv")

# data.info()

data['Gender'] = data['Gender'].fillna(data['Gender'].mode()[0])
data['Dependents'] = data['Dependents'].fillna(data['Dependents'].mode()[0])
data['Married'] = data['Married'].fillna(data['Married'].mode()[0])
data['Loan_Amount_Term'] = data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0])
data['LoanAmount'] = data['LoanAmount'].fillna(data['LoanAmount'].mode()[0])
data['Self_Employed'] = data['Self_Employed'].fillna('Yes')
data['Credit_History'] = data['Credit_History'].fillna(1.0)

# print(data.apply(lambda x: sum(x.isnull()),axis=0))

X = data.iloc[:, 1: 12].values
y = data.iloc[:, 12].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# for taining set

labelencoder_X = LabelEncoder()
for i in range(0, 5):
    X_train[:,i] = labelencoder_X.fit_transform(X_train[:,i])
X_train[:,10] = labelencoder_X.fit_transform(X_train[:,10])

labelencoder_y = LabelEncoder()
y_train = labelencoder_y.fit_transform(y_train)


# for testing set
labelencoder_X = LabelEncoder()
for i in range(0, 5):
    X_test[:,i] = labelencoder_X.fit_transform(X_test[:,i])
X_test[:,10] = labelencoder_X.fit_transform(X_test[:,10])

labelencoder_y = LabelEncoder()
y_test = labelencoder_y.fit_transform(y_test)


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# print('The accuracy of Logistic Regression is: ', metrics.accuracy_score(y_pred, y_test))

classifier.fit(X_train, y_train)
filename = 'finalized_model.sav'
pkl.dump(classifier, open(filename, 'wb'))