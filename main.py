import pickle
import json
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
loaded_model = pickle.load(open('finalized_model2.sav', 'rb'))
def predict_cutoff(a):
	clg=loaded_model.predict([a])
	return clg
