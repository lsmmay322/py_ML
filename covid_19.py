import pandas as pd
import numpy as np
import datetime as dt
import requests
import sys
from itertools import chain
import pycountry
import pycountry_convert as pc
import plotly_express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics
import xgboost as xgb
from xgboost import XGBRegressor
from xgboost import plot_importance, plot_tree
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/gasak/OneDrive/바탕 화면/big data/covid19 data/data/covid_19_data.csv')
df_train = pd.read_csv('C:/Users/gasak/OneDrive/바탕 화면/big data/covid19 data/data/train.csv')
df_test = pd.read_csv('C:/Users/gasak/OneDrive/바탕 화면/big data/covid19 data/data/test.csv')

df.rename(columns={'ObservationDate':'Date','Province/State':'Province_State',
                   'Country/Region':'Country_Region','Confirmed':'ConfirmedCases',
                   'Deaths':'Fatalities'},inplace=True)
df.loc[df['Country_Region']=='Mainland China','Country_Region']='China'
df['Date'] = pd.to_datetime(df['Date'],format='%m/%d/%Y')
df['Day'] = df.Date.dt.dayofyear
df['cases_lag_1'] = df.groupby(['Country_Region','Province_State'])['ConfirmedCases'].shift(1)
df['deaths_lag_1'] = df.groupby(['Country_Region','Province_State'])['Fatalities'].shift(1)
df['Daily Cases'] = df['ConfirmedCases'] - df['cases_lag_1']
df['Daily Deaths'] = df['Fatalities'] - df['deaths_lag_1']

print(1)