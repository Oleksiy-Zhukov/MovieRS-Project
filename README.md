# Movie Recommendation System using Streamlit

## Project Demo

<a href="https://youtu.be/q-WajVFMZ7A"><img src="https://github.com/Oleksiy-Zhukov/MovieRS-Project/assets/75014961/336f2168-c99d-4a46-bddc-936477f7ceea"></a>

https://youtu.be/q-WajVFMZ7A

Welcome to the Movie Recommendation System web application! This project showcases a movie recommendation system powered by data science techniques. Users can input a movie of their choice, and the system will provide recommendations based on the selected movie. The recommendations are generated using a combination of natural language processing and machine learning algorithms.

## Table of Contents
* Introduction
* Usage
* Technical Details
* Demo Video
* Installation
* Future Enhancements
* Contact Information

## Introduction
This project focuses on creating a user-friendly web application that provides movie recommendations. By leveraging the power of a Movie Recommendation System, users can discover new movies similar to the ones they already love. The recommendation engine is built using advanced data science techniques, ensuring that the suggestions are tailored to each user's preferences.

## Usage
1. Access the Movie Recommendation System web application through the following link: [Link to the Web App](https://recommendmovie.streamlit.app/)
2. Upon landing on the web page, you will encounter a user-friendly interface.
3. Enter the title of a movie you'd like to get recommendations for in the designated input field.
4. Click the "Show Recommendation" button to trigger the system to generate recommendations based on your input.
5. The system will display a list of 5 movie recommendations along with their posters and names.

## Technical Details
The Movie Recommendation System is built using the following technologies and methodologies:

* Data Collection and Preprocessing: A dataset containing 5000 movies is utilized. The dataset was meticulously cleaned and preprocessed, resulting in a structured dataset containing movie IDs, titles, and tokenized features extracted from various attributes such as descriptions, cast, crew, genres, and keywords.
* Text Vectorization: The TfidfVectorizer technique is employed to convert the tokenized features into numerical vectors. This vectorization process captures the significance of words within the context of each movie.
* Similarity Calculation: Cosine similarity is employed to compute the similarity between the vectorized representations of different movies. This similarity metric assists in identifying movies that share similar characteristics.
* Amazon S3 Integration: The computed similarity matrix is stored in an Amazon S3 bucket. This cloud-based storage solution enables the web application to access the matrix efficiently and provide real-time recommendations.

## Demo Video
To get a visual walkthrough of how the Movie Recommendation System works, please watch our demo video: [Link to Demo Video](https://youtu.be/q-WajVFMZ7A)

## Installation
To run the project locally, follow these steps:

* Clone the repository to your local machine.
* Install the required dependencies using `pip install -r requirements.txt`.
* Run the Streamlit app using the command `streamlit run app.py`.

## Future Enhancements
I am committed to improving and expanding the Movie Recommendation System. Some future enhancements include:

* Incorporating user preferences to provide personalized recommendations.
* Enhancing the user interface and overall user experience.

## Contact Information
For any inquiries or feedback, please feel free to contact us at zhukov.oleksiy@gmail.com.
