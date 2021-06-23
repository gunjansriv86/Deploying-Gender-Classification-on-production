# Deploying-Gender-Classification-on-production
Deploying a gender classification model using Flask

1. Gender classification_git.pdf - Refer the PDF first to understand the approach.
2. Preprocessing_gender_classification.ipynb - Use this to explore the understand the EDA, model selection
3. features.py - Created my own module for cleaning names and extracting features. This is useful while deploying model with pipeline feature.
4. Gender Prediction_all.ipynb - Assembling all at one place. This is the main code which saves the model file( pickle/joblib)
5. Load Gender Classification.py - Flask code that calls the model file for prediction
6. home.html - HTML page this is used to service the requests.
