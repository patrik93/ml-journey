import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import HashingVectorizer


class Model:
    # Initializing the model from DecisionTreeClassifier
    model = DecisionTreeClassifier()

    # Initializing the hashing vectorizer
    vectorizer = HashingVectorizer()

    def __init__(self, dataset=None):
        # Prepare the data for the initial train
        X, y = self.prepare_train(dataset)

        # Debug to check the initial preparation with the data
        # print(f'from init: X: {X}, \n y: {y}')

        # Initial training of the model
        self.train(X, y)

        # Create predictions from the test input
        # predictions = model.predict(X_test)
    def get_prediction(self, file):
        input = pd.read_csv(file)
        return self._predict(input)
    def _predict(self, X):
        X = X['Description']
        X = self.vectorizer.transform(X)
        prediction = self.model.predict(X)
        #print(f'Prediction from the class object: \n{prediction}')
        return prediction

    def train(self, X, y):
        # Splitting up the dataset into test and train
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Fit the train data
        self.model.fit(X_train, y_train)

    def prepare_train(self, dataset=None):
        # Create the initial train dataset if no data given in parameter
        if dataset is None:
            dataset = pd.read_csv('rev_desc.csv')
        else:
            dataset = pd.read_csv(dataset)

        X = dataset.drop(columns=['Category'])
        y = dataset['Category']

        # Creating the vectorized features from the Description column
        X = self.vectorizer.transform(X['Description'])
        return X, y