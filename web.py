import pickle
import streamlit as st
import requests
import boto3
import toml

# # Load AWS credentials from secrets.toml
# secrets = toml.load(".streamlit/secrets.toml")
# aws_access_key = secrets['aws']['AWS_ACCESS_KEY_ID']
# aws_secret_key = secrets['aws']['AWS_SECRET_ACCESS_KEY']
# aws_region = secrets['aws']['AWS_DEFAULT_REGION']


# def load_data_from_s3():
#     bucket_name = "movieprojectbucket"
#     s3 = boto3.resource(
#         's3',
#         aws_access_key_id=aws_access_key,
#         aws_secret_access_key=aws_secret_key,
#         region_name=aws_region
#     )
    
#     # Load movies data
#     movies_obj = s3.Object(bucket_name, 'movies_df_1.pkl')
#     movies = pickle.loads(movies_obj.get()['Body'].read())
    
#     # Load movie_list data (assuming it's a list of movie names)
#     similarity_obj = s3.Object(bucket_name, 'similarity.pkl')
#     similarity = pickle.loads(similarity_obj.get()['Body'].read())
    
#     return movies, similarity

# # Load data from S3
# movies, similarity = load_data_from_s3()


movies = pickle.load(open('movies_df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
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

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

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
    
