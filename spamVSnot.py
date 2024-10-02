import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

path = "D:\Study\Summer\Spam VS non Spam\SMSSpamCollection.csv"

data = pd.read_csv(path,sep="\t",names=["label","text"])

sn=SnowballStemmer("english")
Stop=stopwords.words('english')
print(Stop)