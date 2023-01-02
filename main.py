import joblib
from gensim.parsing.preprocessing import strip_punctuation, remove_stopwords, strip_non_alphanum

# Load pre-trained
vectorizer = joblib.load('models/tfidf_vectorizer.abc')
LR_model = joblib.load('models/LR_1500_model.abc')
Clf_model = joblib.load('models/LR_classify_model.abc')
selector = joblib.load('models/selector_1500.abc')

labels = ['(0, 3.0]', '(3.0, 3.5]', '(3.5, 4.0]', '(4.0, 4.5]', '(4.5, 5.0]']

# Get input data
title = input('Input Book title: ')
description = input('Input Book description: ')

# Inference
X_input = ' '.join([title, description])
X_input = str.lower(X_input)
X_input = strip_punctuation(X_input)
X_input = remove_stopwords(X_input)
X_input = strip_non_alphanum(X_input)
X_input = vectorizer.transform([X_input])

y_pred_LR = LR_model.predict(selector.transform(X_input))
y_pred_clf = Clf_model.predict(X_input)

print(f'Linear Regression | Rating: {y_pred_LR[0]:.2f}')
print(f'Logistic Regression | Rating range: {labels[y_pred_clf[0]]}')