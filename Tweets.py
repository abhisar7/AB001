import streamlit as st
import tweepy as tw
import pandas as pd
from final_p1 import *
import PyQt5
# from app import hashtag
def get_tweets1(hashtag) :
    consumer_key = 'p3EPFVLTABmfFFdfJBZwvb05C'
    consumer_secret = 'aM6y1LMxK507zt8QBRRyIvJEARpReqbTnJZCTnkhBIl6XFQslt'
    access_token = '1577020526161465344-1FcYoDYQVYv9B6wNUD2RAmKXSLCRCm'
    access_token_secret = 'IpSxps4LKMV8LoaWjpJrvgw6wo2kV9NHLSuT1mCxsBLmO'

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tw.API(auth,wait_on_rate_limit=True)
    # hashtag = ''
    
    
    query = tw.Cursor(api.search_tweets,q=hashtag).items(1000)
       
    tweets = [{'Tweets':tweet.text}for tweet in query]
    # st.write(tweets)
    df = pd.DataFrame.from_dict(tweets)
    # st.write(df.head(5))
    df['processed_Tweets'] = np.vectorize(process_tweet)(df['Tweets'])
    tokenized_Tweets = df['processed_Tweets'].apply(word_tokenize)
    tokenized_Tweets = tokenized_Tweets.apply(lambda x: [lemmatizer.lemmatize(i) for i in x])
    for i in range(len(tokenized_Tweets)):
        tokenized_Tweets[i] = ' '.join([word for word in tokenized_Tweets[i] if word not in stop_words])  

    df['processed_Tweets'] = tokenized_Tweets
    final_vectorized_data_Tweets = count_vectorizer.transform(df['processed_Tweets'])
    predicted_naive_Tweets = model_naive.predict(final_vectorized_data_Tweets)
    df['sentiment']= predicted_naive_Tweets

    
    st.write('Percentage of Positive Sentiment Tweets ',(len(df[df['sentiment']==1])/len(df))*100,'%')
    st.write('Percentage of Negetive Sentiment Tweets ',(len(df[df['sentiment']==0])/len(df))*100,'%')
    
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # sentiments = ['Positive Sentiment', 'Negetive Sentiment'] 
    # slices = [(df['sentiment'] != 0).sum(), (df['sentiment'] == 0).sum()] 
    # colors = ['g', 'r'] 
    # plt.pie(slices, labels = sentiments, colors=colors, startangle=90, shadow = True,
    #         explode = (0, 0.1), radius = 1.5, autopct = '%1.2f%%') 
    # plt.legend()
    # st.write(st.pyplot())
    



    