#vImports 
import streamlit as st 
import json 
import uv as v 

# set up the Application 

st.set_page_config(page_title="Library Manager", layout="wide")

st.markdown("""
    <style>
        body {
            background-color: #000000;
            font-family: 'Poppins', sans-serif;
            background-image: url('https://static.vecteezy.com/system/resources/previews/022/574/913/non_2x/abstract-blurred-public-library-interior-space-blurry-room-with-bookshelves-by-defocused-effect-use-for-background-or-backdrop-in-abstract-blurred-publicbusiness-or-education-concepts-generative-ai-photo.jpg');
            background-size: cover;
            background-attachment: fixed;
        }
        .main-title {
            font-size: 50px;
            font-weight: bold;
            color: #4B6884;
            text-align: center;
            margin-bottom: 30px;
        }
        .card {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            margin-bottom: 20px;
        }
        .book-title {
            font-size: 24px;
            color: #2C3A47;
            font-weight: bold;
        }
        .book-meta {
            color: #7B8EA0;
            font-size: 16px;
        }
        .stTextInput>div>input {
            border-radius: 5px;
            padding: 10px;
            border: 1px solid #4B6584;
        }
        .card:hover {
            transform: scale(1.02);
            transition: 0.3s;
            }    
    </style>
""", unsafe_allow_html=True)




# Load Books from JSON 

def load_books():
    try:
        with open("books.json" , "r") as file:
            return json.load(file)
    except FileNotFoundError: return []    


#  Save Books to JSON 

def save_books(books):
    with open("books.json" , "w") as file :
        json.dump(books, file, indent=4)

books = load_books


# UI Header 
st.markdown(' <div class="main-title"> 📚 -BOOK NEST </div>' ,unsafe_allow_html=True )

# Display Books 

st.subheader("📚 Your Book Collection")

for book in books():
    st.markdown(f"""
                <div class="card">
                <div class="book-title">{book['title']}</div>
                <div class="book-meta">Author:{book['author']}</div>
                <div class="book-meta">Genre:{book['genre']}</div>
                <div class="book-meta">Status:{book['status']}</div>
                </div>
                """ , unsafe_allow_html=True)
    