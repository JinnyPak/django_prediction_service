from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView

from predict.models import TextData,text_to_list,text_preprocessing,padding_sequence
from tensorflow.keras.models import load_model
from config import settings
import os



import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def post(request):
        text=request.POST.get('text')
        #텍스트전처리
        text_list=text_to_list(text)
        text_pre=[text_preprocessing(x) for x in text_list]
        pad_seq=padding_sequence(text_pre)
        #모델로드 및 적용
        embedding_dim=300
        model=load_model('predict/model/lstm_all_text.h5')
        pred_cls = model.predict_classes(pad_seq)
        pred_proba=model.predict_proba(pad_seq)
        return render(request,'predict/result.html',{'pred_cls':pred_cls,'pred_proba':pred_proba})

