from django.db import models

import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class TextData(models.Model):
    text=models.TextField(null=True)

    def __str__(self):
        return self.text
#### 입력받은 텍스트를 리스트로 변환해주는 함수
def text_to_list(text):
    text='\"'+text+'\"'
    # 리스트형태로 입력받음
    text_list=[text]
    return text_list

#### 텍스트 전처리 수행 함수
def text_preprocessing(document):
    # 소문자 변환
    document = document.lower()
    document = document.replace('\\xa0',' ')
    document = document.replace('•\\t',' ') 
    # 특수문자 제거
    pattern = '[{}]'.format(string.punctuation)
    document = re.sub(pattern, ' ', document)
    # stopword 제거, stemming
    sw = stopwords.words('english')+['may']
    word_token=nltk.word_tokenize(document)
    stemmer = PorterStemmer()

    result_token=[ stemmer.stem(word) for word in word_token if word not in sw]
    #문자열로 변환 후 반환
    return ' '.join(result_token)

### sequence 생성 함수

def padding_sequence(data):
    max_features=10000
    maxlen=500

    tokenizer = Tokenizer(num_words=max_features)
    tokenizer.fit_on_texts(data)
    
    sequences=tokenizer.texts_to_sequences(data)
    pad_sequence_data=pad_sequences(sequences,maxlen=maxlen)

    return pad_sequence_data