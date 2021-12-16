import sqlite3
import pandas as pd
import os
from flask import Flask
from sklearn.linear_model import LogisticRegression
from category_encoders import OrdinalEncoder
from sklearn.pipeline import make_pipeline


app = Flask(__name__)


def getModel():
    conn = sqlite3.connect('./heartData.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM heart_data")
    rows = cursor.fetchall()
    cols = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(data=rows, columns=cols)

    X_train = df.drop(['id', 'HeartDisease'], axis=1)
    y_train = df.HeartDisease

    pipe_ord = make_pipeline(
    OrdinalEncoder(), 
    LogisticRegression(max_iter=1000))

    pipe_ord.fit(X_train, y_train)

    return pipe_ord


@app.route('/diagnosis')
def diagnosis():
    
    model = getModel()

    data = pd.read_csv (r'./test_data.csv')   
    test_data = pd.DataFrame(data)
    # result = model.predict(test_data)
    result_tmp = model.predict(test_data)

    result = []
    for i in result_tmp:
        if i == 1:
            result.append('위험군')
        else:
            result.append('비위험군')
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
