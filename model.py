#pip install -r requirements.txt
#Uncomment above line to install dependencies for this project

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import tensorflow
import re
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

def process_title(title):
    new_title = title.lower() #lower casing 
    new_title = re.sub(r'\$[^\s]+', 'dollar', new_title) # substituting $100 or $ 30 with dollar
    new_title = re.sub(r'[^a-z0-9\s]', '', new_title) # removing punctuation marks
    new_title = re.sub(r'[0-9]+', 'number', new_title) # substituting 0-9 with number
    new_title = new_title.split() # splitting sentences into words
    new_title = list(map(lambda x: ps.stem(x), new_title))  # steming
    new_title = list(map(lambda x: x.strip(), new_title))  # striping
    return new_title

tokenizer = Tokenizer(num_words=17785)

model=load_model('./model.h5')
model.load_weights('./model.h5')

import pickle

# Load titles
with open('titles.pkl', 'rb') as f:
    titles = pickle.load(f)

def model_prediction(text):
    text=str(text)
    text=[text]
    text = [process_title(t) for t in text]
    tokenizer.fit_on_texts(titles)
    sequenc = tokenizer.texts_to_sequences(text)
    padded_in=pad_sequences(sequenc, maxlen=42)
    prediction = model.predict(padded_in)
    threshold = 0.5  # Decision boundary
    
    # Check the prediction and print the appropriate result
    if prediction[0][0] >= threshold:
        result = "🟩 Genuine & Real News"
    else:
        result = "🟥 Misleading & Fake News"
    
    
    # Return the result as well
    return result