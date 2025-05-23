import h5py
from model import model_prediction
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI(title='News Classifier')

class RequestState(BaseModel):
    text: str

@app.post('/result')
def endpoint(request: RequestState):
    response=model_prediction(request.text)
    if response is None:
        raise HTTPException(status_code=500, detail="Model prediction failed")
    return {'Result':response}


if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,host='127.0.0.1',port=8889)

#Run following command in cmd:
#python backend.py
