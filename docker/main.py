from fastapi import FastAPI
import backend.model as model

app = FastAPI()

@app.get("/predict")
def get_prediction():
  m1 = model.Model('data/rev_desc_b.csv')

  predictions = m1.get_prediction('data/manual_x.csv')
  return { f'Result predictions are: {predictions}' }

