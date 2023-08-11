import streamlit as st
import pickle
from PIL import Image
import difflib

st.header("Anime Recommendation system")
foods = pickle.load(open("dataset", "rb"))
similar = pickle.load(open("similarity.pkl", "rb"))
foods_list = foods["title"].values

selected_value = st.selectbox("Search", foods_list)

def food_recommend(movies):
    find_close_match = difflib.get_close_matches(movies, foods_list)
    close_match = find_close_match[0]
    food_index = foods[foods['title'] == close_match].index.values[0]
    similar_score = list(enumerate(similar[food_index]))
    sorted_list = sorted(similar_score, key = lambda x:x[1], reverse = True)
    
    foods_data = []

    i = 1

    for film in sorted_list:
        index = film[0]
        title_food  = foods[foods.index == index]["title"].values[0]
        if (i<33):
            foods_data.append(title_food)
            i+=1
    return foods_data
if st.button("Show recommend"):
    food_name = food_recommend(selected_value)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader(food_name[0])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[0]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[0]].values[0])
    with col2:
        st.subheader(food_name[1])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[1]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[1]].values[0])
        
    with col3:
        st.subheader(food_name[2])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[2]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[2]].values[0])
        
    with col4:
        st.subheader(food_name[3])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[3]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[3]].values[0])

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader(food_name[4])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[4]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[4]].values[0])
    with col2:
        st.subheader(food_name[5])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[5]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[5]].values[0])
        
    with col3:
        st.subheader(food_name[6])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[6]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[6]].values[0])
        
    with col4:
        st.subheader(food_name[7])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[7]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[7]].values[0])
        
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader(food_name[8])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[8]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[8]].values[0])
    with col2:
        st.subheader(food_name[9])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[9]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[9]].values[0])
        
    with col3:
        st.subheader(food_name[10])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[10]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[10]].values[0])
        
    with col4:
        st.subheader(food_name[11])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[11]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[11]].values[0])
        
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader(food_name[12])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[12]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[12]].values[0])
    with col2:
        st.subheader(food_name[13])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[13]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[13]].values[0])
        
    with col3:
        st.subheader(food_name[14])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[14]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[14]].values[0])
        
    with col4:
        st.subheader(food_name[15])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[15]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[15]].values[0])
        
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader(food_name[16])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[16]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[16]].values[0])
    with col2:
        st.subheader(food_name[17])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[17]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[17]].values[0])
        
    with col3:
        st.subheader(food_name[18])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[18]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[18]].values[0])
        
    with col4:
        st.subheader(food_name[19])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[19]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[19]].values[0])
        
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader(food_name[20])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[20]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[20]].values[0])
    with col2:
        st.subheader(food_name[21])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[21]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[21]].values[0])
        
    with col3:
        st.subheader(food_name[22])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[22]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[22]].values[0])
        
    with col4:
        st.subheader(food_name[23])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[23]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[23]].values[0])
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader(food_name[24])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[24]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[24]].values[0])
    with col2:
        st.subheader(food_name[25])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[25]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[25]].values[0])
        
    with col3:
        st.subheader(food_name[26])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[26]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[26]].values[0])
        
    with col4:
        st.subheader(food_name[27])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[27]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[27]].values[0])
        
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader(food_name[28])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[28]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[28]].values[0])
    with col2:
        st.subheader(food_name[29])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[29]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[29]].values[0])
        
    with col3:
        st.subheader(food_name[30])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[30]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[30]].values[0])
        
    with col4:
        st.subheader(food_name[31])
        image = Image.open(foods["image_dir"][foods['title'] == food_name[31]].values[0])
        st.image(image)
        st.text(foods["genre"][foods['title'] == food_name[31]].values[0])
    
      