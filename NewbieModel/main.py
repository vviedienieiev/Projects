import pickle
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import pymorphy2


class NewbiesModel:

    def __init__(self):
        self.clf = None
        self.vectorizer = None
        self.morph = pymorphy2.MorphAnalyzer()
        self.trigger_words = ["помогите", "помощь", "курс", "новичок", "новенький", "книг", "совет", "учить", "учеба"]

    def teach_model(self, path_to_df: str):
        df = pd.read_csv(path_to_df)
        all_x = df["text"].apply(lambda x: x.replace("?", " question_mark")).values
        all_x = [self.morph.parse(word)[0].normal_form for word in all_x]
        all_y = df["class"].values
        self.vectorizer = CountVectorizer(encoding='KOI8-R', lowercase=True, stop_words=stopwords.words('russian'),
                                          ngram_range=(1, 2), analyzer='word')
        text_transformed = self.vectorizer.fit_transform(all_x)
        x_train, x_test, y_train, y_test = train_test_split(text_transformed, all_y, test_size=0.3, stratify=all_y)
        self.clf = MultinomialNB().fit(x_train, y_train)
        predicted = self.clf.predict(x_test)
        print(metrics.confusion_matrix(predicted, y_test))
        print("MultinomialNB Accuracy:", metrics.accuracy_score(y_test, predicted))

    def save_model(self, path: str):
        if (self.clf is None) | (self.vectorizer is None):
            raise ValueError("You need to teach the model first")
        else:
            with open(path, "wb") as f:
                pickle.dump([self.clf, self.vectorizer], f)

    def upload_model(self, path: str):
        with open(path, "rb") as f:
            self.clf, self.vectorizer = pickle.load(f)

    def predict_senctence(self, text: str) -> int:
        triggers = [word for word in self.trigger_words if word in text]
        if len(triggers) == 0:
            return 0
        else:
            if (self.clf is None) | (self.vectorizer is None):
                raise ValueError("You need to teach the model first")
            else:
                new_word = [self.morph.parse(word)[0].normal_form for word in [text]]
                new_text_counts = self.vectorizer.transform(new_word)
                return self.clf.predict(new_text_counts)[0]


if __name__ == "__main__":
    model = NewbiesModel()
    # model.teach_model("csv_files/classification_short.csv")
    # model.save_model("model_clf.pickle")
    model.upload_model("model_clf.pickle")
    model.predict_senctence("Скиньте, пожалуйста, курсы или книги по пайтону")
