#Data Training and Prediction

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class SpamFilter:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def train_from_csv(self, path):
        #Read the CSV 
        df = pd.read_csv(path, encoding="latin1") 

        if df.shape[1] < 2:
            raise ValueError("CSV must have label and text.")

        #first column = labels, second column = text
        labels = df.iloc[:, 0].astype(str)
        texts = df.iloc[:, 1].astype(str)

        #Training
        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)

    def predict(self, text):
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]
