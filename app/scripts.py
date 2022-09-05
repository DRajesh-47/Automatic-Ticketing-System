from json import encoder
import joblib
from preprocessing import clean_text, translate
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import numpy as np
import tkinter as tk
from tkinter import messagebox

model = load_model('models/rnn_final.h5')
tokenizer = joblib.load('models/tokenizer.pkl')
encoder = joblib.load('models/label_encoder.pkl')



def predict(short, desc):

    raw = short.get() + " " + desc.get("1.0", tk.END)

    clean = translate(clean_text(raw))

    sequence = tokenizer.texts_to_sequences([clean])

    entry = pad_sequences(sequence, padding='post',maxlen=300)

    pred = np.argmax( model.predict(entry))


    pred_str = encoder.inverse_transform([pred])[0]

    print(pred_str)

    messagebox.showinfo("Group", pred_str)



