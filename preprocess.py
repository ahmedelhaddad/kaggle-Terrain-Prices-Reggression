import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import joblib

def preprocess_data(train_path='data/train.csv', test_path='data/test.csv'):
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)

    X = train.drop(columns=['price'])
    y = train['price']

    cat_features = X.select_dtypes(include=['object']).columns
    num_features = X.select_dtypes(exclude=['object']).columns

    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
    ])

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    X_train = preprocessor.fit_transform(X_train)
    X_val = preprocessor.transform(X_val)
    joblib.dump(preprocessor, 'models/preprocessor.pkl')

    return X_train, X_val, y_train, y_val

if __name__ == '__main__':
    preprocess_data()
