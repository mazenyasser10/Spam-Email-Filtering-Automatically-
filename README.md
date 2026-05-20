# Spam Email Filter

## Overview

This project is a GUI-based **Spam Email Detection System** developed using machine learning.  
The system allows users to enter an email message, then automatically predicts whether the email is **spam** or **ham**.

The project was created for the **CSE263 Machine Learning and Pattern Recognition** course. It focuses on applying text preprocessing, feature extraction, machine learning classification, and GUI integration to solve a real-world email filtering problem.

## Problem Description

Spam emails are unwanted messages that may include advertisements, scams, phishing attempts, or harmful content.  
Manually detecting and removing spam emails is inefficient and unreliable.

This project aims to automate spam email detection by training a machine learning model on labeled email data and using it to classify new email messages.

## Features

- Classifies emails as **spam** or **ham**
- Uses a trained machine learning model
- Converts email text into numerical features
- Provides a simple GUI for user input
- Displays the prediction result instantly
- Supports manual testing with custom email text

## Machine Learning Approach

The system follows a simple machine learning pipeline:

1. **Data Collection**
   - Uses emails labeled as spam or ham.

2. **Data Preprocessing**
   - Converts text to lowercase
   - Removes punctuation
   - Handles missing values
   - Removes duplicates
   - Cleans empty entries

3. **Feature Extraction**
   - Uses `CountVectorizer` to convert email text into numerical feature vectors.

4. **Model Training**
   - Uses `Multinomial Naive Bayes`, which is suitable for text classification tasks.

5. **Prediction**
   - The trained model predicts whether a new email is spam or ham.

## Technologies Used

- Python
- Tkinter
- Pandas
- NumPy
- Scikit-learn
- CountVectorizer
- Multinomial Naive Bayes
- Visual Studio Code

## Project Interface

The project includes a simple graphical user interface where the user can paste or type an email message.  
After clicking the check button, the system displays the classification result as either:

- `spam`
- `ham`

## Screenshots / Results

### Spam Email Detection Result

The system correctly classifies a promotional email as spam.

<img width="542" height="456" alt="image" src="https://github.com/user-attachments/assets/870a7344-80c0-4a16-b8d4-2a3293342397" />


### Ham Email Detection Result

The system correctly classifies a normal message as ham.

<img width="524" height="454" alt="image" src="https://github.com/user-attachments/assets/7afe7adf-a98b-43d2-b53d-40a49663d646" />

## Advantages

- Simple and easy to use
- Fast prediction
- Suitable for text classification
- Uses a lightweight machine learning model
- Helps improve email management and security

## Limitations

- The model depends on the quality and size of the training dataset.
- It works best with English email text.
- CountVectorizer counts word occurrences but does not fully understand the full meaning of the sentence.
- The model may miss spam emails that use hidden, tricky, or unusual language.

## Future Improvements

- Use a larger dataset to improve accuracy.
- Add more preprocessing techniques.
- Try other classifiers such as Logistic Regression or XGBoost.
- Add model evaluation metrics such as accuracy, precision, recall, and F1-score.
- Improve the GUI design.
- Save and load the trained model automatically.

## Team Members

- Mazen Yasser
- Marwan Ehab
- Jasmine Ali
- Sandy Atef

## Task Assignment

- Mazen Yasser — Implementation and Model Design
- Sandy Atef — Data Preparation and Preprocessing
- Jasmine Ali — Evaluation and Analysis
- Marwan Ehab — Documentation and Report Formatting

## Course Information

**Course:** CSE263 - Machine Learning and Pattern Recognition  
**Department:** Computer Systems Engineering  
**Term:** Fall 2025  
**University:** MSA University / University of Greenwich  

## Conclusion

The Spam Email Filter project demonstrates how machine learning can be used to solve a practical classification problem.

By using text vectorization and Multinomial Naive Bayes, the system can analyze email text and predict whether it is spam or ham through a simple GUI.
