import pandas as pd
import datetime
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

start_time = datetime.datetime.now()

df = pd.read_csv("final_df.csv")

X = df[['session_frequency','Dur. (ms)','total_traffic','experience_score']]
y = df['satisfaction_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)

end_time = datetime.datetime.now()

joblib.dump(model, "model.pkl")

log = {
    "code_version": "v1.0",
    "start_time": str(start_time),
    "end_time": str(end_time),
    "data_source": "final_df.csv",
    "model": "LinearRegression",
    "parameters": "default",
    "r2_score": r2,
    "rmse": rmse,
    "artifact": "model.pkl"
}

log_df = pd.DataFrame([log])

file_exists = os.path.isfile("model_tracking.csv")

log_df.to_csv(
    "model_tracking.csv",
    mode='a',
    header=not file_exists,
    index=False
)

print("Model tracking completed!")
