from typing import Literal
import joblib
from pydantic import BaseModel, Field
import numpy as np
import pandas as pd

from enum import Enum

from fastapi import FastAPI
import uvicorn


class jobType(str, Enum):
    admin = 'admin.'
    blue_collar = 'blue-collar'
    entrepreneur = 'entrepreneur'
    housemaid = 'housemaid'
    management = 'management'
    retired = 'retired'
    self_employed = 'self-employed'
    services = 'services'
    student = 'student'
    technician = 'technician'
    unemployed = 'unemployed'
    unknown = 'unknown'

class maritalType(str, Enum):
    divorced = 'divorced'
    married = 'married'
    single = 'single'
    unknown = 'unknown'

class educationType(str, Enum):
    basic_4y = 'basic.4y'
    basic_6y = 'basic.6y'
    basic_9y = 'basic.9y'
    high_school = 'high.school'
    illiterate = 'illiterate'
    professional_course = 'professional.course'
    university_degree = 'university.degree'
    unknown = 'unknown'

class defaultType(str, Enum):   
    no = 'no'
    yes = 'yes'
    unknown = 'unknown' 

class contactType(str, Enum):
    cellular = 'cellular'
    telephone = 'telephone'
    unknown = 'unknown'

class poutcomeType(str, Enum):
    failure = 'failure'
    nonexistent = 'nonexistent'
    success = 'success'


class Customer(BaseModel):
    age: int = Field(...)
    duration: int = Field(...)
    campaign: int = Field(...)
    emp_var_rate: float = Field(...)
    cons_conf_idx: float = Field(...)
    euribor3m: float = Field(...)
    nr_employed: float = Field(...)
    job: jobType = Field(..., description='Job Type')
    marital: maritalType = Field(..., description='Marital Status')
    education: educationType = Field(..., description='Education Level')
    default: defaultType = Field(..., description='Default Status')
    contact: contactType = Field(..., description='Contact Type')
    poutcome: poutcomeType = Field(..., description='Previous Outcome')

class PredictResponse(BaseModel):
    default_probability: float
    default: bool


app = FastAPI(title="bank-marketing-automation")

pipeline = joblib.load('./best_model.pkl')


def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)


@app.post("/predict")
def predict(customer: Customer) -> PredictResponse:
    prob = predict_single(customer.model_dump())

    return PredictResponse(
        default_probability=prob,
        default=prob >= 0.57
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)