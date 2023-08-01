import pickle
import streamlit as st
import requests


# Config
movies = pickle.load(open('movies_df.pkl','rb'))
knn_model = pickle.load(open('knn_model.pkl','rb'))
movie_list = pickle.load(open('movie_list.pkl','rb'))

X = movies.drop(['movie_id', 'title', 'tags'], axis=1).values

st.header('Movie Recommender System')
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# def recommend(movie):
#     recommended_movie_names = selected_movie
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)

#     return recommended_movie_names,recommended_movie_posters

# Find the indices of the top 5 similar movies for a given movie
def recommend(movie):
    
    #find index of given movie
    matching_entries = movie_list[movie_list == movie]
    index = matching_entries.index[0]
    
    query_movie_index = index  # Replace with the index of the movie you want to get recommendations for
    distances, indices = knn_model.kneighbors(X[query_movie_index].reshape(1, -1), n_neighbors=6)

    # 'indices' will contain the indices of the top 5 similar movies
    similar_movie_indices = indices[0][1:]

    # Get list of recommended movies
    recommended_movie_names = movies.iloc[similar_movie_indices, 1].values
    
    # Get list of movie posters
    recommended_movie_posters = []
    for movie_id in similar_movie_indices:
        recommended_movie_posters.append(fetch_poster(int(movies.loc[movie_id, 'movie_id'])))
        
    return recommended_movie_names,recommended_movie_posters
    
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    
