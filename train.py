import joblib
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from preprocess import preprocess_data

def train_model():
    X_train, X_val, y_train, y_val = preprocess_data()
    model = xgb.XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=6, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_val)
    rmse = mean_squared_error(y_val, preds, squared=False)
    print(f'Validation RMSE: {rmse:.2f}')
    joblib.dump(model, 'models/trained_model.pkl')

if __name__ == '__main__':
    train_model()
