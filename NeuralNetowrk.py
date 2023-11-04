import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

files = pd.read_csv(
    './SingleDay.csv',
    names=['Date', 'Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'],
    converters={'Open': float, 'High': float, 'Low': float, 'Close': float, 'Volume': float}
)
dataset = files.copy()
print(dataset['Open'].sum())
