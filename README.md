# 🏔️ Terrain Prices Regression – Kaggle Competition

**Kaggle Competition:** [Terrain Prices Regression Challenge](https://www.kaggle.com/competitions/terrain-prices-reggression/overview)  
**Colab Notebook:** [View Full Notebook on Google Colab](https://colab.research.google.com/drive/1R4QBjjcqw-9KKskpdAe5PvgokdYU_9oA?usp=sharing)

---

## 📘 Overview
This project was built for the **Kaggle Terrain Prices Regression Challenge**, which focuses on predicting **terrain prices** using structured geospatial and socioeconomic data.  
The goal is to develop a regression model that accurately estimates terrain prices based on location and related features.

---

## 🎯 Objective
- Predict terrain prices from multiple features (e.g., coordinates, area, terrain type, etc.)
- Build a robust regression model optimized for RMSE (Root Mean Squared Error)
- Apply preprocessing, feature engineering, and model evaluation techniques

---

## 🧠 Workflow
### 1️⃣ Data Preprocessing
- Loaded and explored the dataset (`train.csv`, `test.csv`)
- Handled missing values, outliers, and inconsistent entries  
- Encoded categorical variables and normalized numerical ones  
- Split data into training and validation sets

### 2️⃣ Feature Engineering
- Added interaction terms and domain-specific features
- Scaled numerical columns for consistent model behavior
- Selected best features using correlation analysis and feature importance

### 3️⃣ Model Training
- Trained multiple regression models (Linear Regression, Random Forest, XGBoost)
- Used **GridSearchCV** for hyperparameter optimization
- Selected the best-performing model based on **RMSE**

### 4️⃣ Model Evaluation
- Compared predicted vs actual prices  
- Visualized performance metrics and feature importance  
- Saved the trained model using `joblib`

### 5️⃣ Inference
- Loaded the saved model to make predictions on new/unseen data
- Exported predictions to `submission.csv` for Kaggle submission

---

## 🧩 Tech Stack
- **Python** 🐍  
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**  
- **Scikit-learn**, **XGBoost**, **Joblib**

---

## 🧰 How to Run Locally

### 🔹 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/terrain-prices-regression.git
cd terrain-prices-regression
```

### 🔹 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 🔹 3. Run preprocessing and training
```bash
python preprocess.py
python train.py
```

### 🔹 4. Generate predictions
```bash
python inference.py
```

---

## 📊 Results

| Model | RMSE | Notes |
|--------|------|-------|
| Linear Regression | 2304.5 | Baseline model |
| Random Forest | 1780.2 | Improved performance |
| XGBoost | 1653.8 | Best model selected ✅ |

---

## 🧾 References
- [Kaggle Competition Page](https://www.kaggle.com/competitions/terrain-prices-reggression)
- [Colab Notebook](https://colab.research.google.com/drive/1R4QBjjcqw-9KKskpdAe5PvgokdYU_9oA?usp=sharing)

---

## 👤 Author
**Ahmed Elhaddad**  
📍 Data Science & Machine Learning Enthusiast  
🌐 [LinkedIn](https://www.linkedin.com) | 🧠 [Kaggle](https://www.kaggle.com)
