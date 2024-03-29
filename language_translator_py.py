# -*- coding: utf-8 -*-
"""Language_Translator.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VYi3duW5sbvZF84nTEYp9IbGCzrpCbYC
"""

#NAME: NAVEED
#EMAIL: mn815325@gmail.com
#Python Mini Project

#First, we will install Pip into it

!pip install transformers

#Install Sentence Piece Library

!pip install sentencepiece

#Secondly, we  will import required liabraries

from transformers import MarianMTModel, MarianTokenizer

#Create a function to translate text from English to a target language using a pre-trained model:

def translate(text, target_language):
    model_name = f'Helsinki-NLP/opus-mt-en-{target_language}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(inputs, num_beams=4, max_length=50, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return translated_text

#Use the translation function to translate text from English to the desired target language

input_text = "Hello, Naveed how are you?"
target_language = 'it'
translated_text = translate(input_text, target_language)
print(translated_text)

