from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./dataset/Clean_Raisin_Dataset.xlsx')

print(df.columns)

# unlabel dataset
x = df.drop('Class', axis=1)

# class column
y = df['Class']

# normalization
scaler = StandardScaler()
x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# model
model = Sequential()

# input layer
model.add(Dense(units=7, input_shape=[7], name="input_layer")) # one dimension, i.e. [a, b, ...]

# hidden layers
model.add(Dense(units=28, activation="sigmoid", name="hidden_layer_1"))
model.add(Dense(units=28, activation="sigmoid", name="hidden_layer_2"))
model.add(Dense(units=28, activation="sigmoid", name="hidden_layer_3"))

# output layer
model.add(Dense(units=1, activation="sigmoid", name="output_layer"))

model.summary()

# model compilation
model.compile(optimizer=Adam(learning_rate=0.01), loss="binary_crossentropy", metrics=["accuracy"])

# training
histogram = model.fit(x_train, y_train, epochs=4000, validation_data=(x_test, y_test))

# graphs
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.plot(histogram.history["loss"])
plt.savefig('./results/error.png')

plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.plot(histogram.history["accuracy"])
plt.savefig('./results/accuracy.png')

