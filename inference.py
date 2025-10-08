import pandas as pd
import joblib

def predict(test_path='data/test.csv', output_path='submission.csv'):
    test = pd.read_csv(test_path)
    model = joblib.load('models/trained_model.pkl')
    preprocessor = joblib.load('models/preprocessor.pkl')
    X_test = preprocessor.transform(test)
    preds = model.predict(X_test)
    submission = pd.DataFrame({'Id': test.index, 'price': preds})
    submission.to_csv(output_path, index=False)
    print(f'Submission file saved as {output_path}')

if __name__ == '__main__':
    predict()
