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

## Sample Output

Example results from the GUI:

```text
Result: spam
