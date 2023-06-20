import streamlit as st
import tweepy as tw
import pandas as pd
from Tweets import get_tweets1


# from app import hashtag

st.title("Twitter Sentiment Analysis App")

with st.form("1"):
    hashtag = st.text_input('Enter #Hashtag', )
    st.write('The current hashtag is', hashtag)
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        get_tweets1(hashtag)
        
# import matplotlib.pyplot as plt
# import numpy as np

# sentiments = ['Positive Sentiment', 'Negetive Sentiment'] 
# slices = [90, 10] 
# colors = ['g', 'r'] 
# plt.pie(slices, labels = sentiments, colors=colors, startangle=90, shadow = True,
#             explode = (0, 0.1), radius = 1.5, autopct = '%1.2f%%') 
# plt.legend()
# st.write(st.pyplot())

