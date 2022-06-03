import pickle
import json
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
def predict_cutoff(a):
	clg=loaded_model.predict([a])
	return clg
