import pickle
import pandas as pd
import streamlit as st

# Load the Dataset
data = pickle.load(open('C:\\Users\\layek\\ML Projects\\Project 3\\movie_dict.pkl', mode='rb'))
movies = pd.DataFrame(data)

# Load the Similarity
similarity = pickle.load(open('C:\\Users\\layek\\ML Projects\\Project 3\\similarity.pkl', mode='rb'))

# Final Function 
def recommend(movie):
    recommended = []

    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movie_list:
        recommended.append(movies.iloc[i[0]].title)

    return recommended

# Streamlit web app
st.title('Movie Recommendation System')
selected_movie = st.selectbox("Select a movie to get a movie recommendation", movies['title'].values)
btn = st.button('Recommendation')

if btn:
    recommended_movies = recommend(selected_movie)

    if recommended_movies[0] == "Movie not found in the database.":
        st.write(recommended_movies[0])
    else:
        for movie in recommended_movies:
            st.write(movie)
