import pandas as pd
import numpy as np
# from operator import itemgetter
from sentence_transformers import SentenceTransformer

print('111')
df = pd.read_csv('results/data.gov.lt.csv')[:200]
df['id'] = df.index
corpus = list(df['Name of the dataset'].values)

model = SentenceTransformer('bert-base-nli-mean-tokens')
sentence_embeddings = model.encode(corpus)

