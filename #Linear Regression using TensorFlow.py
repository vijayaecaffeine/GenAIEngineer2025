#Linear Regression using TensorFlow

#Installed sklearn (scikit-learn)

from __future__ import absolute_import,division,print_function,unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import tensorflow as tf

dftrain = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
dfeval = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/eval.csv")

print(dftrain.head())

y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')


dftrain.shape
dftrain.age.hist(bins=20)