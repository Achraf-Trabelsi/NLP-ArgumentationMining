
import pandas as pd
import re
import matplotlib.pyplot as plt
import nltk.tokenize 
from spacy import displacy
import spacy


#understanding data
data=pd.read_csv("train.csv")
print(data.head())
print(data.columns)
print(data.isnull().sum())

